import utils, syntax, platform
from time import sleep
from termcolor import colored
class MythCompiler:
	def __init__(self, filetype):
		if platform.system() == "Linux" or platform.system() == "Darwin":
			print(colored("Initializing Myth Compiler...", "blue"))
		else:
			print("Initializing Myth Compiler...")
		if filetype=="python":
			if platform.system() == "Linux" or platform.system() == "Darwin":
				print(colored("Hey! Don't try using Python here!!! Myth may have been written in Python, but you can't run Python from Myth. Or can you...", "red"))
			else:
				print("Hey! Don't try using Python here!!! Myth may have been written in Python, but you can't run Python from Myth. Or can you...")
			
		elif filetype=="standard/.mth":
			if platform.system() == "Linux" or platform.system() == "Darwin":
				print(colored("Loading compiler for FileType \".MTH Myth source file\"", "blue"))
			else:
				print("Loading compiler for FileType \".MTH Myth source file\"")
			sleep(1)
	def Run(self, filename, *args, **kwargs):
		for ar in args:
			if ar == "debug" or "dbg":
				dbg = True
			else:
				dbg = False
		else:
			dbg = False
		try:
			open(filename, 'r')
		except:
			print("An error occured while parsing the file. Maybe your file path is wrong?")
		if platform.system() == "Linux" or platform.system() == "Darwin":
			print(colored("Running program...", "green"))
		else:
			print("Running program...")
		sleep(0.5)
		utils.clear()
		syntax.check(filename, dbg)