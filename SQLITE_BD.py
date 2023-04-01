import sqlite3

conn = sqlite3.connect('datas_bd.db')
print("Base de données ouverte avec succès")

conn.execute('CREATE TABLE datas (entree TEXT, resultat TEXT)')
print("Table de base de données créee avec succès")
conn.close()