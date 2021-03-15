#!/usr/bin/python
# -*- coding=utf-8 -*- 

import sys 

import MySQLdb 		# import du module MySQLdb 


# l'identité de l'utilisateur est (vide,vide) 
crit = raw_input("Tapez d’un critère nom, uid, gid ou programme: ")
if crit == "nom" or crit == "uid" or crit == "gid" or crit == "programme":
	critval = raw_input("Tapez valeur pour " + crit + ": ")
	if critval:
    	    	user="root" 
		pwd="Cr0semont_9" 
		host="localhost" 
		connexion=None 
		nom_base="comptes_linux"      #  A changer eventuellemet
		try: 
			print "connexion..." 
			# connexion 
			connexion=MySQLdb.connect(host=host,user=user,passwd=pwd,db=nom_base) 
			print "Connexion a MySQL reussie sous l'identite host={0},user={1},passwd={2}".format(host,user,pwd) 
		except MySQLdb.OperationalError,message: 
			print "Erreur : {0}".format(message) 
			sys.exit()
		cursor = connexion.cursor()
		if crit == "nom":
			cursor.execute('SELECT * from users WHERE username=%s',(critval,))
		if crit == "uid":
			if critval.isdigit():
				cursor.execute('SELECT * from users WHERE uid=%s',(critval,))
			else:
				print "Le valeur {0} ne pas numerique".format(critval)
				sys.exit()
		if crit == "gid":
			if critval.isdigit():
				cursor.execute('SELECT * from users WHERE gid=%s',(critval,))
			else:
				print "Le valeur {0} ne pas numerique".format(critval)
				sys.exit()
		if crit == "programme":
			cursor.execute('SELECT * from users WHERE prog=%s',(critval,))
		records = cursor.fetchall()
		if len(records) > 0:		
			for l in records: print "|%-20s | %-1s | %-6s | %-6s | %-30s | %-20s | %-20s |" % l
			connexion.close()	
		else:
			print "Usager n'est existe pas"
else:	
	print("Vous specifiez pas bonne critère.")
