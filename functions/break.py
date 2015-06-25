# it's a program that reminds the user to take a break

import webbrowser
import time

# pr started
print "Break Program just started", time.ctime()

# loop three times a day
for i in range(0, 3):
	# delay
	time.sleep(10)
	print "you have to take a break it's", time.ctime(), "now!"
	# open Janis Joplin song
	webbrowser.open("https://www.youtube.com/watch?v=rX8hOw31wCQ")