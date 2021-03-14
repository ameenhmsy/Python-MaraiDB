#!/user/bin/python
# -*- coding: utf-8 -*-

import sys 
import MySQLdb as db
import os
import HTML

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

sql="SELECT * FROM users"
cursor = connexion.cursor()
try: 
	print "connexion..." 
	# connexion 
	connexion=db.connect(host=host,user=user,passwd=pwd,db=nom_base) 
	# suivi 
	print "Connexion a MySQL reussie sous l'identite host={0},user={1},passwd={2},db={3}".format(host,user,pwd,nom_base) 
except db.OperationalError,message: 
	print "Erreur : {0}".format(message)
	sys.exit()

fic=open("page.html","w")
fic.write('<html><head><title>Python et Mysql</title></head>')
fic.write('<body><h2>Liste des utilisateurs</h2>')
entete = ["User Name","Uid","Gid","Gecos","Rep_Connexion","Programme"]
table_data = [  entete ]
sql="SELECT * FROM users"
cursor = connexion.cursor()
try:
   cursor.execute(sql)
   results = cursor.fetchall()
   for row in results:
        table_data.append([row[0],row[2],row[3],row[4],row[5],row[6]])
except:
   print "Erreur : aucune donnée disponible"


# disconnect from server
connexion.close()
htmlcode = HTML.table(table_data)
fic.write(htmlcode)
fic.write('</body></html>')
fic.close()
os.system("firefox  page.html")
