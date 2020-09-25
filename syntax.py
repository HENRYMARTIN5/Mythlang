from time import *
from termcolor import cprint as cpr
import platform
from var import *
import sys
def check(filepath, dbg):
	variables = {}
	clrImport = False
	f = open(filepath)
	for line in f:
		if line.startswith("out "):
			print(line.split("out ")[1])
		elif line == "exit":
			sys.exit()
		elif line.startswith("delay "):
			try:
				sleep(float(line.split("delay ")[1]))
			except ValueError:
				if platform.system() == "Linux" or platform.system() == "Darwin":
					cpr("ERROR - Time to wait cannot be string", 'red')
					break
				else:
					print("ERROR - Time to wait cannot be string.")
					break
				if dbg:
					if platform.system() == "Linux" or platform.system() == "Darwin":
						cpr("EXACTerror:",'red')
						sleep(int(line.split("delay ")[1]))
						break
					else:
						print("EXACTerror:")	
						sleep(int(line.split("delay ")[1]))
						break
		elif line.startswith("-gray out "):
			cpr(line.split("-gray out ")[1], "gray")
		elif line.startswith("-red out "):
			cpr(line.split("-red out ")[1], "red")		
		elif line.startswith("-green out "):
			cpr(line.split("-green out ")[1], "green")
		elif line.startswith("-yellow out "):
			cpr(line.split("-yellow out ")[1], "yellow")
		elif line.startswith("-blue out "):
			cpr(line.split("-blue out ")[1], "blue")
		elif line.startswith("-magenta out "):
			cpr(line.split("-magenta out ")[1], "magenta")
		elif line.startswith("-cyan out "):
			cpr(line.split("-cyan out ")[1], "cyan")		
		elif line.startswith("-white out "):
			cpr(line.split("-white out ")[1], "white")		
		elif line.startswith("-"):
			cpr("Confused very I am...\nColor does not exist. Sry :(", "red")		
			break							
		elif line.startswith("~"):
			pass
		elif line[0:3] == "var":
			c = line[4:]
			for i in c:
				p = 0
				if c == "=":
					variable_name = c[0:p]
					p += 1 
					value = c[p:]
					eval("variables."+variable_name+" = "+value)
				else:
					p +=1
		elif line[0:6] == "outvar":
			q = line[7:]
			print(variables)
			print(variables.get(q,))
			
