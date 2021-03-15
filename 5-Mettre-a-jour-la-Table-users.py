#!/usr/bin/python
# -*- coding=utf-8 -*- 

import sys 		
import MySQLdb 		# import du module MySQLdb 


# connexion à une base MySql 

nom = raw_input("Tappez le nouvel nom de usager: ")
#print "User {0}".format(nom)
user="root" 
pwd="Cr0semont_9" 
host="localhost" 
connexion=None 		# utilisateur vide 
nom_base="comptes_linux"      
nom_passwd="x"
try: 
	print "connexion..." 
	connexion 
	connexion=MySQLdb.connect(host=host,user=user,passwd=pwd,db=nom_base) 
	print "Connexion a MySQL reussie sous l'identite host={0},user={1},passwd={2}".format(host,user,pwd) 
except MySQLdb.OperationalError,message: 

	print "Erreur : {0}".format(message) 
	sys.exit()
cursor = connexion.cursor()
	#if nom:
#	cursor.execute('SELECT * from users')
cursor.execute('SELECT * from users WHERE username=%s',(nom,))
records = cursor.fetchall()
if len(records) > 0:
	print("L'usager {0} déjà existé.".format(nom))	
	#	for l in records: print "|%-20s | %-1s | %-6s | %-6s | %-30s | %-20s | %-20s |" % l
	#	connexion.close()	
else:
	print("Usager {0} n'est existe pas".format(nom))


#prog varchar(50));
	uid = raw_input("Tappez l'uid de usager: ")
	if uid.isdigit() and uid > 1000:
		cursor.execute('SELECT * from users WHERE uid=%s',(uid,))
		records = cursor.fetchall()
		if len(records) > 0:
			print "Le valeur de uid a déjà utilisé"
			sys.exit()
		else:
			gid = raw_input("Tappez le gid de usager: ")
			if gid.isdigit() and gid > 1000:
				cursor.execute('SELECT * from users WHERE uid=%s',(gid,))
				records = cursor.fetchall()
				if len(records) > 0:
					print "Le valeur de gid a déjà utilisé"
					sys.exit()
				else:
					gecos = raw_input("Tappez le gecos de usager: ")
					if gecos:
						homedir = raw_input("Tappez le homedir de usager, par exemple /home/{0}: ".format(nom))
						if homedir:
							cursor.execute('SELECT * from users WHERE homedir=%s',(homedir,))
							records = cursor.fetchall()
							if len(records) > 0:
								print "Le valeur de homedir a déjà utilisé"
								sys.exit()
							else:
								prog = raw_input("Tappez le programme de usager, par exemple /bin/bash: ")
								if prog:
									print("Creation de utilisateur {0} a commencé: ".format(nom))
									sql = "INSERT INTO users (username, x, uid, gid, gecos, homedir, prog) VALUES (%s, %s, %s, %s, %s, %s, %s)"
									val = (nom, nom_passwd, uid, gid, gecos, homedir, prog)
									cursor.execute(sql, val)
									connexion.commit()
									#print(cursor.rowcount)
									#connexion.close()
									if cursor.rowcount > 0:		
										print("L'usager {0} a été créé avec succes".format(nom))		
										connexion.close()	
									else:
										print("L'usager {0} n'a pas été créé avec succes".format(nom))
						else:
							print "Le valeur de homedir est vide"
					else:
						print "Le valeur de gecos est vide"
			else:
				print "Le valeur de gid ne pas bon"
	else:
		print "Le valeur de uid ne pas bon"
#else:	
#	print("Vous specifiez pas bonne critère.")


