import os

print("\n\t\t------Priyansh Project------")

while True:
	print("""
	Press 1 : For Know Summary of Session 1	
	Press 2 : For Know Summary of Session 2
	Press 3 : For Know Summary of Session 3
	Press 4 : For Know Summary of Session 4
	Press 5 : For Know Summary of Session 5
	Press 6 : For Know Summary of Session 6
	Press 7 : For Know Summary of Session 7
	Press 8 : For Know Summary of Session 8
	Press 9 : For Know Summary of Session 9
	Press 10: For Know Summary of Session 10
	Press 11: For Know Summary of Session 11
	Press 12: For Know Summary of Session 12
	Press 13: For Know Summary of Session 13
	Press 0 : For Exit
	""")

	choice = int(input("Enter your Choice : "))
	
	if choice == 1:
		print("\n\t\t\t----Session 1 Summary----")
		print("""
		In Session 1 I learn about How can we
		Launch Our Linux Operating System By AWS

		We make Small HTML program that can be
		accessible by Anyone.

		Learn Some Commands for Example :-
		""")
		date = os.system("date")
		print(date)

	elif choice == 2:
		print("\n\t\t\t----Session 2 Summary----")
		print("""
		In Session 2 I learn about How Launch Our 
		Linux Operating via Virtual Box

		We know that Suppose we have 500gb Hard Disk but it display
		only 465 Gb Where Remains 35 Gb 

		""")

	elif choice == 3:
		print("\n\t\t\t----Session 3 Summary----")
		print("""
		In Session 3 I learn about Git and Github
		
		We know Many Commands of Git
		And also know Why we should use Github.
		""")

	elif choice == 4:
		print("\n\t\t\t----Session 4 Summary----")
		print("""
		In Session 3 I learn about Many Linux Commands
		Example : ls,cal,date.......etc
		
		And i also Create one Command which name i give devil
		""")

	elif choice == 5:
		print("\n\t\t\t----Session 5 Summary----")
		print("""
		In Session 5 I learn about -
		What is Cookies?
		Some Commands of Github
		Some commands of Linux
		""")

	elif choice == 6:
		print("\n\t\t\t----Session 6 Summary----")
		print("""
		In Session 6 I learn about -
		What is Process?
		What is Program?
		Difference between Process & Program.
		How to check process & program and kill it on linux Commands

		Linux Commands :-
		For Processing :- ps -aux
		For Killing :- kill processID(ex- 5645)
		""")

	elif choice == 7:
		print("\n\t\t\t----Session 7 Summary----")
		print("""
		In Session 7 - I Learn About
		Rahul Sir Organize Revision Game based on 
		He taught us in previous 6 sessions.

		and in this game I ranked 2nd out of 10.

		and also I present my screen and taught other
		members to how to download Virtual Box and Creat 
		Launch or Linux OS.
		""")

	elif choice == 8:
		print("\n\t\t\t----Session 8 Summary----")
		print("""
		In Session 8 I learn about espeak Command
		and we see the intro of upcoming Cloud Sessions
		""")

	elif choice == 9:
		print("\n\t\t\t----Session 9 Summary----")
		print("""
		In Session 9 - I Learn About
		What is Cloud?
		What is need of Cloud?
		What is AWS?
		What is need of AWS?
		Types of Cloud.
		What Services Cloud Provide us.
		How to create Account in AWS
		""")

	elif choice == 10:
		print("\n\t\t\t----Session 10 Summary----")
		print("""
		In Session 10 - I Learn About
		Why we should use Twitter, LinkedIn & Github
		What is importance of Twitter, LinkedIn & Github
		What is network?
		How we Launch our Linux OS by AWS.
		""")

	elif choice == 11:
		print("\n\t\t\t----Session 11 Summary----")
		print("""
		In Session 11 - I Learn About
		What is Protocols?
		Types of Protocols.
		SSH(Secure Shell Protocol)		
		RDP(Remote Desktop Protocol)
		ICMP(Internet Control Message Protocol)
		What is Port Number?
		Download Putty & Puttygen
		""")

	elif choice == 12:
		print("\n\t\t\t----Session 12 Summary----")
		print("""
		In Session 12 - I Learn About
		What is Interpreter and which language support it.
		learn Command :- echo $?
		Interaction between OS and Programming Language.		
		""")

	elif choice == 13:
		print("\n\t\t\t----Session 13 Summary----")
		print("""
		In Session 13 - I Learn About
		What is Server?
		What is Client?
		What is webserver
		Download httpd
		What is need of Webserver
		How to Configure WebServer
		""")	

	elif choice == 0:
		os.system("exit")
		break

