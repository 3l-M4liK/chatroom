import socket
import threading
import time


pseudo = input('pseudo : ')
host = input('server\'s ip : ')
port = int(input('port : '))
print("ltfg !")
time.sleep(2.0)
pso = f"\033[1;33;40m<{pseudo}>>\033[0;37;40m"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
now = time.localtime(time.time())
tim = time.strftime("%y/%m/%d %H:%M", now)
print('\033c')
print(f"|{tim}| your name is \033[1;33;40m{pseudo}\033[0;37;40m, the server is {host}@{port}\n")
def send(s):
	s.send(pseudo.encode('utf-8'))
	while True:
		now = time.localtime(time.time())
		tim = time.strftime("%y/%m/%d %H:%M", now)
		tac = input('')
		if tac == "exit":
				print("bye..")
				time.sleep(2.0)
				s.send("exit".encode('utf-8'))
				time.sleep(1.0)
				s.close()
				break
		else:
			s.send(f"{pso}{tac}".encode('utf-8'))

def r(s):
	while True:
		try:
				re = s.recv(1024).decode('utf-8')
				if re != '':
					if re == "!Tban!":
						print("on vous a kick !\nvous pouvez encor écrire un ultime message !!!! (suppliez le peut etre que..)")
						break
					else:
						print(f"|{tim}| {re}")
				else:
					break
		except Exception:
			break
th = threading.Thread(target=r, args=(s, ))
th.start()
send(s)
print("\033c")
