import webbrowser
import time

total_breaks = 3
break_count = 0

#time.ctime() --- print the current time
print ("This program started on" + time.ctime())

while break_count < total_breaks:
    time.sleep(10)   #wait 10 seconds to operate the rest
    webbrowser.open('http://www.baidu.com')
    break_count +=1