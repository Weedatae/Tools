# coding : utf-8
# author : Wilson | Weedatae <3
# require : CURL and REQUESTS module
import os
import requests
import colorama
import time
from colorama import Style, Fore
colorama.init()
print(Fore.CYAN + "\nHi welcome to my script..." + Style.RESET_ALL)
website = input("Enter the website (http/https) : ")
print(Fore.MAGENTA + "The website is : " + website + Style.RESET_ALL)
print(Fore.BLUE + "[1] : VIEW HEADER (curl)" + Style.RESET_ALL)
print(Fore.BLUE + "[2] : VIEW ROBOTS.TXT  " + Style.RESET_ALL)
choice = input("Choice : ")

if choice == "1":
	print("\n")
	os.system("curl -I " + website)
if choice == "2":
	print("\n")
	req = requests.get(website + "/robots.txt")
	if "User-agent:" in req.text:
		print(req.text)
	else:
		print("ROBOTS.TXT NOT FOUND")
		time.sleep(3)
elif choice != "1" or choice != "2":
	print(Fore.CYAN + "exit...." + Style.RESET_ALL)
	time.sleep(2)


