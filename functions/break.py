# it's a program that reminds the user to take a break

import webbrowser
import time


# loop three times a day
for i in range(0, 3):
	# delay
	time.sleep(10)
	# open Janis Joplin song
	webbrowser.open("https://www.youtube.com/watch?v=rX8hOw31wCQ")