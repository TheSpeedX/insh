import subprocess
from random import choice
import sys
import os
import ctypes
import tempfile

def color(text,colour='W'):
	if os.name is 'nt':
		colord={'W': 15,'B': 9,'G': 10,'C': 11,'R':12}
		if not colour in colord:
			colour='W'
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.SetConsoleTextAttribute(handle, colord[colour])
		print(text)
		ctypes.windll.kernel32.SetConsoleTextAttribute(handle, colord['W'])
	else:
		colord={'W': '\033[0m','B': '\033[1;34m','G': '\033[1;32m','C': '\033[1;36m','R':'\033[1;31m'}
		if not colour in colord:
			colour='W'
		print(colord[colour]+text+colord['W'])
def help():
	print("\n\nThis is A Simple Module That insults you at wrong code...")
	print("\n\nUsage:  insh <command>")
	print("Author: SpeedX")

def main():
	messages = [
			"You type like I drive.",
			"You speak an infinite deal of nothing",
			"I wish to make a complaint.",
			"What kind of mutant ninja are you ?",
			"DAMN !!! And you call yourself a PRO!",
			"(╯°□°）╯",
			"What, what, what, what, what, what, what, what, what, what?",
			"Are you on drugs?",
			"Your mind just hasn't been the same since the electro-shock, has it?",
			"Commands, random gibberish, who cares!",
			"My cat can type better than you?",
			"Try using your brain the next time!",
			"I fart in your general direction!",
			"What if... you type an actual command the next time!",
			"Are you always this stupid or are you making a special effort today?!",
			"I am _seriously_ considering 'rm -rf /'-ing myself...",
			"This is not a search engine.",
			"stty: unknown mode: doofus",
			"Perhaps computers is not for you...",
			"There must be cure for it!",
			"Where did you learn to type?",
			"What do you think you are doing, idiot?",
			"Why are you doing this to me?!",
			"Please step away from the keyboard!",
			"If I wanted to kill myself I'd climb your ego and jump to your IQ.",
			"Wrong!  You cheating scum!",
			"Hold it up to the light --- not a brain in sight!",
			"What if I told you... it is possible to type valid commands.",
			"I bet your brain feels as good as new, seeing that you never use it.",
			"So, I'm just going to go ahead and run rm -rf / for you.",
			"You do that again and see what happens...",
			"Bailing out, you are on your own. Good luck! ",
			"error code: 1D10T",
			"I'd like to see things from your point of view but I can't seem to get my head that far up my ass.",
			"buh, buh, buh... Get to it, idiot!",
			"I'm not saying I hate you, but I would unplug your life support to charge my phone.",
			"I think ... err ... I think ... I think you must go home",
			"ERROR_INCOMPETENT_USER",
			"Speak English you fool --- there are no subtitles in this scene.",
			"The keyboard is not a touch screen!",
			"I've seen penguins that can type better than that.",
			"Incompetence is also a form of competence",
			"It can only be attributed to human error.",
			"Did someone dropped you while you were a baby, eh?",
			"Take a stress pill and think things over."]
	if len(sys.argv)==1:
		help()
		exit()
	try:
		result = subprocess.run(sys.argv[1:],shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	except:
		color(choice(messages)+"\n",'R')
		color(sys.argv[1]+" : command not found",'B')
		exit()
	out = result.stdout.decode('utf-8')
	err = result.stderr.decode('utf-8')
	if err:
		color(choice(messages)+"\n",'R')
		color(err,'B')
	else:
		color("So Glad To See It Worked !!!!!\n\n",'G')
		print(out)
