#!/user/bin/python
# -*- coding: utf-8 -*-

import sys 
import MySQLdb as db

user="root"
pwd="Cr0semont_9" 
host="localhost" 
connexion=None 
nom_base="comptes_linux"
try: 
	print "connexion..." 
	# connexion 
	connexion=db.connect(host=host,user=user,passwd=pwd,db=nom_base) 
	# suivi 
	print "Connexion a MySQL reussie sous l'identite host={0},user={1},passwd={2},db={3}".format(host,user,pwd,nom_base) 
except db.OperationalError,message: 
	print "Erreur : {0}".format(message)
	sys.exit()
cursor = connexion.cursor()
for ligne in open("/etc/passwd"):
	ligne=ligne.rstrip()
	cursor.execute("""INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s)""", ligne.split(":"))
connexion.commit()
connexion.close()
