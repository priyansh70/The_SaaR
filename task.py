import os

print("\n\t\t------Priyansh Project------")

while True:
	print("""
	Press 1 : For Know About All Sessions
	Press 2 : For Know Cloud Sessions
	Press 0 : Exit
	""")
	
	choice = int(input("Enter Your Choice : "))
	if choice == 1:	
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
			Press 14: For Know Summary of Session 14
			Press 15: For Know Summary of Session 15/16
			Press 16: For Know Summary of Session 15/16
			Press 17: For Know Summary of Session 17
			Press 18: For Know Summary of Session 18
			Press 19: For Know Summary of Session 19
			Press 20: For Know Summary of Session 20
			Press 21: For Know Summary of Session 21
			Press 22: For Know Summary of Session 22
			Press 0 : For Exit
			""")
		
			choice = int(input("Enter your Choice : "))
		
			if choice == 1:
				print("\n\t\t\t----Session 1 Summary----")
				session = os.system("cat Session/Session1")
	
			elif choice == 2:
				print("\n\t\t\t----Session 2 Summary----")
				session = os.system("cat Session/Session2")
	
			elif choice == 3:
				print("\n\t\t\t----Session 3 Summary----")
				session = os.system("cat Session/Session3")
	
			elif choice == 4:
				print("\n\t\t\t----Session 4 Summary----")	
				session = os.system("cat Session/Session4")
	
			elif choice == 5:
				print("\n\t\t\t----Session 5 Summary----")
				session = os.system("cat Session/Session5")
	
			elif choice == 6:
				print("\n\t\t\t----Session 6 Summary----")
				session = os.system("cat Session/Session6")

			elif choice == 7:
				print("\n\t\t\t----Session 7 Summary----")
				session = os.system("cat Session/Session7")

			elif choice == 8:
				print("\n\t\t\t----Session 8 Summary----")
				session = os.system("cat Session/Session8")
	
			elif choice == 9:
				print("\n\t\t\t----Session 9 Summary----")
				session = os.system("cat Session/Session9")
	
			elif choice == 10:
				print("\n\t\t\t----Session 10 Summary----")
				session = os.system("cat Session/Session10")
	
			elif choice == 11:
				print("\n\t\t\t----Session 11 Summary----")
				session = os.system("cat Session/Session11")
	
			elif choice == 12:
				print("\n\t\t\t----Session 12 Summary----")
				session = os.system("cat Session/Session12")
	
			elif choice == 13:
				print("\n\t\t\t----Session 13 Summary----")
				session = os.system("cat Session/Session13")
		
			elif choice == 14:
				print("\n\t\t\t----Session 14 Summary----")
				session = os.system("cat Session/Session14")
	
			elif choice == 15 or choice == 16:
				print("\n\t\t\t----Session 15/16 Summary----")
				session = os.system("cat Session/Session15-16")
		
			elif choice == 17:
				print("\n\t\t\t----Session 17 Summary----")
				session = os.system("cat Session/Session17")

			elif choice == 18:
				print("\n\t\t\t----Session 18 Summary----")
				session = os.system("cat Session/Session18")
		
			elif choice == 19:
				print("\n\t\t\t----Session 19 Summary----")
				session = os.system("cat Session/Session19")

			elif choice == 20:
				print("\n\t\t\t----Session 20 Summary----")
				session = os.system("cat Session/Session20")

			elif choice == 21:
				print("\n\t\t\t----Session 21 Summary----")
				session = os.system("cat Session/Session21")
		
			elif choice == 22:
				print("\n\t\t\t----Session 22 Summary----")
				session = os.system("cat Session/Session22")

			elif choice == 0:
				os.system("exit")
				break	

			else:
				print("Invalid Choice")

	elif choice == 2:
		print("\n\t\tAll Cloud Summary ->")
		session = os.system("cat All_Cloud_Summary.txt")
	
	elif choice == 0:
		os.system("exit")
		break

	else:
		print("Invalid Choice")
