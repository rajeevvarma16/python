#!/usr/bin/env python
import webbrowser
import time
current_time = time.ctime()
print ("Start time is " + current_time)
i = 0
while(i<3):
	time.sleep(10)
	webbrowser.open("https://youtube.com")