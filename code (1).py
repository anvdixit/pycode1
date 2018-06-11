import time
import os
import webbrowser

# displaying choices
x='''
press 1: check date and time
press 2: create a file
press 3: create a directory
press 4: to search something on google
press 5: logout to your system
press 6: shut down your OS
press 7: check internet connection in your laptop
press 8: login whatsapp on browser
press 9: to check all connected IP in your network
'''
print x

#variable to store user's choice
choice=int(raw_input("enter your choice"))

#using ctime function of time library to display date and time
if choice==1 :
	print "date and time is", time.ctime()

#using os library to use linux commands, here touch command is used
elif choice==2 :
	 os.system('touch file.txt')

#using linux command 'mkdir' to make a new directory/folder using os library 
elif choice==3 :
	 os.system('mkdir new_directory')

# using webbrowser library to access google.com
elif choice==4 :
	msg=raw_input("type what to search")
	webbrowser.open_new_tab('https://www.google.com/search?q=' +msg)

# to logout from the system
elif choice==5 :
	os.system('pkill -KILL -u root')	

# to reboot systemusing os library
elif choice==6 :
	os.system('reboot')

# to check if internet is connected or not 
elif choice==7 :
	os.system('ping www.google.com')

# to connext to whatsapp web
elif choice==8 :
	webbrowser.open_new_tab('https://web.whatsapp.com/')

# to see how many IP are connected to your laptop 
elif choice==9 :
	os.system('ping 182.64.47.44 arp -a')

else :
	print "invalid choice"



