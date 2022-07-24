# from mcrcon import MCRcon as r
# with r('localhost','beepboop') as mcr:
#     resp = mcr.command('/list')
# print(resp) #there are 0/20 players online: - This will be different for you.

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex(('127.0.0.1',25565))
if result == 0:
   print ("Port is open")
else:
   print ("Port is not open")
sock.close()