import os
import ctypes
import insh.config as C
from openai import OpenAI


class INSH:
    def __init__(self) -> None:
        if os.name == "nt":
            self.os_name = "windows"
            self.init_windows()
        else:
            self.os_name = "linux"
            self.init_linux()

        shell = os.path.split(os.environ.get("SHELL"))[-1]
        if not shell:
            self.color("The shell you are using is not supported.", "R")
            exit(1)
        self.shell = shell

    def color_windows(self, text, colour="W"):
        if not colour in self.color_map:
            colour = "W"
        handle = ctypes.windll.kernel32.GetStdHandle(-11)
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, self.color_map[colour])
        print(text)
        ctypes.windll.kernel32.SetConsoleTextAttribute(handle, self.color_map["W"])

    def color_linux(self, text, colour="W"):
        if not colour in self.color_map:
            colour = "W"
        print(self.color_map[colour] + text + self.color_map["W"])

    def init_windows(self):
        self.color_map = {"W": 15, "B": 9, "G": 10, "C": 11, "R": 12}
        self.color = self.color_windows

    def init_linux(self):
        self.color_map = {
            "W": "\033[0m",
            "B": "\033[1;34m",
            "G": "\033[1;32m",
            "C": "\033[1;36m",
            "R": "\033[1;31m",
        }
        self.color = self.color_linux

    def init_openai(self):
        self.openai_api_key = self.read_api_key()
        if self.openai_api_key is None:
            self.color(
                "OpenAI API key not found. Please run `insh --config` to set the API key.",
                "R",
            )
            exit(1)
        self.openai = OpenAI(api_key=self.openai_api_key)

    def set_api_key(self, api_key):
        with open(C.API_SAVE_PATH, "w") as f:
            f.write(api_key)

    def read_api_key(self):
        if not os.path.exists(C.API_SAVE_PATH):
            return None
        with open(C.API_SAVE_PATH, "r") as f:
            return f.read()

    def activate(self):
        BASHRC_PATH = os.path.join(os.path.expanduser("~"), ".bashrc")
        if os.path.exists(BASHRC_PATH):
            with open(BASHRC_PATH, "r") as f:
                bashrc = f.read()
            rc_lines = bashrc.splitlines()
            already_configured = False
            for index, line in enumerate(rc_lines):
                if "source ~/.insh.bashrc" in line:
                    already_configured = True
                    rc_lines[index] = "export INSH_ENABLED=1;source ~/.insh.bashrc"
            if not already_configured:
                rc_lines.append("export INSH_ENABLED=1;source ~/.insh.bashrc")
        else:
            rc_lines = ["export INSH_ENABLED=1;source ~/.insh.bashrc"]
        with open(BASHRC_PATH, "w") as f:
            f.write("\n".join(rc_lines))
        self.color(
            "insh configured successfully. Restart your shell to activate insh.", "G"
        )

    def deactivate(self):
        if os.path.exists(C.BASHRC_PATH):
            with open(C.BASHRC_PATH, "r") as f:
                bashrc = f.read()
            rc_lines = bashrc.splitlines()
            for index, line in enumerate(rc_lines):
                if f"source {C.INSH_BASHRC_PATH}" in line:
                    rc_lines[
                        index
                    ] = f"export INSH_ENABLED=0;source {C.INSH_BASHRC_PATH}"
        else:
            rc_lines = [f"export INSH_ENABLED=0;source {C.INSH_BASHRC_PATH}"]
        with open(C.BASHRC_PATH, "w") as f:
            f.write("\n".join(rc_lines))
        self.color(
            "insh deactivated successfully. Restart your shell to deactivate insh.", "G"
        )

    def is_configured(self):
        return os.environ.get("INSH_ENABLED") is None


    def config(self):
        self.color("Enter your OpenAI API key: ", "G")
        api_key = input()
        self.set_api_key(api_key)

        if self.shell == "bash" or self.shell == "bash.exe":
            with open(C.INSH_BASHRC_PATH, "w") as f:
                f.write(
                    C.BASH_CONFIGURATION
                )
            self.color("Do you want to activate insh shell? (y/n): ", "G")
            choice = input()
            if choice == "y":
                self.activate()
        else:
            self.color("The shell you are using is not supported.", "R")
            exit(1)

    def generate_insh_response(self, command, error_sentence, exit_code):
        self.init_openai()
        if self.openai_api_key is None:
            self.color(
                "OpenAI API key not found. Please run `insh --config` to set the API key.",
                "R",
            )
            exit(1)
        prompt = C.GPT_USER_PROMPT.format(
            command=command, error_sentence=error_sentence, exit_code=exit_code
        )
        response = self.openai.chat.completions.create(
            model=C.GPT_MODEL,
            messages=[
                {"role": "system", "content": C.GPT_SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            temperature=1,
            top_p=1,
            presence_penalty=0.5,
        )
        response = response.choices[0].message.content
        return response

    def ask(self, question):
        self.init_openai()
        response = self.openai.chat.completions.create(
            model=C.GPT_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": C.GPT_ASK_SYSTEM_PROMPT.format(
                        os=self.os_name, shell=self.shell
                    ),
                },
                {"role": "user", "content": question},
            ],
            top_p=1,
            temperature=1,
        )
        response = response.choices[0].message.content
        return response
