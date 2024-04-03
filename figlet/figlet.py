from pyfiglet import Figlet
figlet = Figlet()

import sys
import random

error = "Invalid usage"
if len(sys.argv) != 1 and len(sys.argv) != 3:
	sys.exit(error)
elif len(sys.argv) == 1:
	text = input("Input: ")
	randtext = random.choice(figlet.getFonts())
	figlet.setFont(font = randtext)
	print("Output: ", figlet.renderText(text))

elif len(sys.argv) == 3:
	if (sys.argv[1] == '-f' or sys.argv[1] == '--f') and sys.argv[2] in figlet.getFonts():
		text = input("Input: ")
		figlet.setFont(font = sys.argv[2])
		print("Output: ", figlet.renderText(text))
	else:
		sys.exit(error)
