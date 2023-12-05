

import argparse
import sys

from insh.shell import INSH


def main():
    parser = argparse.ArgumentParser(
        prog="insh",
        usage="Generate shell commands from GPT with a pinch of humor",
        description="""Ask GPT questions for generating shell commands and let 
                    it correct you with some witty humor""",
        epilog="NOTE: You need to add OpenAI API keys",
    )
    parser.add_argument(
        "-on",
        "--activate",
        dest="activate",
        action="store_true",
        help="Activate shell integration",
    )
    parser.add_argument(
        "-off",
        "--deactivate",
        dest="deactivate",
        action="store_true",
        help="Deactivate shell integration",
    )
    parser.add_argument(
        "-k", "--api-key", dest="api_key", help="Set the OpenAI API Key"
    )
    parser.add_argument(
        "-a", "--ask", help="Ask a custom question to get a shell command"
    )
    parser.add_argument(
        "--config", "--configure", action="store_true", help="Configure insh"
    )

    args = parser.parse_args()

    insh = INSH()

    if args.activate and args.deactivate:
        insh.color("You can't activate and deactivate at the same time", "R")
        exit(1)

    if args.activate or args.deactivate:
        if insh.is_configured():
            insh.color(
                "You need to configure insh first. Run `insh --config` to configure.",
                "R",
            )
            exit(1)

    if args.activate:
        insh.activate()
    elif args.deactivate:
        insh.deactivate()
    elif args.api_key:
        insh.set_api_key(args.api_key)
    elif args.ask:
        response = insh.ask(args.ask)
        insh.color(response, "G")
    elif args.config:
        insh.config()
    else:
        input_text = sys.stdin.read().splitlines()
        last_command, error_sentence, exit_code = (
            input_text[0],
            "\n".join(input_text[1:-1]),
            input_text[-1],
        )
        response = insh.generate_insh_response(last_command, error_sentence, exit_code)
        response = response.splitlines()
        insh.color("\n".join(response[0:-2]), "R")
        insh.color(response[-2], "W")
        insh.color(response[-1], "G")

