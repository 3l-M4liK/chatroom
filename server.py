import socket
import time
import threading
import re
port = int(input('port : '))
print('\033c')
print(f"you are \033[1;33;40mroot\033[0;37;40m and the port is {port}")
host = ''
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
ban = dict()
clients = []
def write():
	while True:
		now = time.localtime(time.time())
		tim = time.strftime("%y/%m/%d %H:%M", now)
		msg = input('')
		if msg == "!history":
			f = open("logs.txt", "a")
			f.write(f"|{tim}| \033[1;33;40mroot\033[0;37;40m a afficher les logs\n")
			f.close()
			f = open("logs.txt", "r")
			print(f.read())
			f.close()
		if msg == "!history in public":
			f = open("logs.txt", "a")
			f.write(f"|{tim}| \033[1;33;40mroot\033[0;37;40m a afficher les logs et les envoyer a tout les mondes dans le serveur\n")
			f.close()
			f = open("logs.txt", "r")
			history = f.read()
			print(history)
			send(history)
			f.close()
		if msg[0:4] == "!ban":
			qui = re.split("!ban ", msg)
			ban[qui[1]].send("!Tban!".encode("utf-8"))
			ban[qui[1]].close()
			clients.remove(ban[qui[1]])
			send(f"\033[1;33;40m<root>>\033[0;37;40m a bannis {qui[1]}")
			f = open("logs.txt", "a")
			f.write(f"|{tim}| \033[1;33;40mroot\033[0;37;40m a kick {qui[1]}")
			f.close()
			del ban[qui[1]]
		if msg == "!ip":
			f = open("ip", "a")
			f.write(f"|{tim}| \033[1;33;40mroot\033[0;37;40m a afficher les logs ip\n")
			f.close()
			f = open("ip.txt", "r")
			ips = f.read()
			print(ips)
			f.close()
		if msg == "!ip in public":
			f = open("ip.txt", "a")
			f.write(f"|{tim}| \033[1;33;40mroot\033[0;37;40m a afficher les logs ip et les envoyer a tout\n")
			f.close()
			f = open("ip.txt", "r")
			ips = f.read()
			print(ips)
			send(ips)
			f.close()
		else:
			send(f"\033[1;33;40m<root>>\033[0;37;40m{msg}")
def send(msg):
	for client in clients:
		client.send(msg.encode('utf-8'))
def a(s):
	while True:
		now = time.localtime(time.time())
		tim = time.strftime("%y/%m/%d %H:%M", now)
		co, ad = s.accept()
		name = co.recv(1024).decode('utf-8')
		print(f'|{tim}|{name} vient de se connecter {ad}')
		f = open("ip.txt", "a")
		f.write(f"|{tim}| {name} s'est coonecter ! {ad}\n")
		f.close()
		ban[name] = co
		clients.append(co)
		thre = threading.Thread(target=r, args=(co,))
		thre.start()
def r(co):
	while True:
		try:
			now = time.localtime(time.time())
			tim = time.strftime("%y/%m/%d %H:%M", now)
			msg = co.recv(1024).decode('utf-8')
			if msg == "exit":
				clients.remove(co)
				co.close()
			if msg == '':
				pass
			else:
				send(f"{msg}")
				print(f"|{tim}| {msg}")
				file = open("logs.txt", "a")
				file.write(f"{msg}\n")
				file.close()
		except Exception:
			pass
th1 = threading.Thread(target=write)
th1.start()
a(s)
