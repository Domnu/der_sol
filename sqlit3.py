import sqlite3

# Connectez-vous à la base de données (ou créez-la si elle n'existe pas)
conn = sqlite3.connect('db.sqlite3')

# Créez un curseur pour exécuter des commandes SQL
cursor = conn.cursor()

# Exécutez des commandes SQL, par exemple, créer une table
cursor.execute('CREATE TABLE IF NOT EXISTS artik_article (id INTEGER PRIMARY KEY, nom TEXT, age INTEGER)')

# Insérez des données dans la table
# cursor.execute('INSERT INTO utilisateurs (nom, age) VALUES (?, ?)', ('John Doe', 30))
# cursor.execute('INSERT INTO utilisateurs (nom, age) VALUES (?, ?)', ('Jane Smith', 25))

# Validez les modifications
conn.commit()

# Sélectionnez des données
# cursor.execute('SELECT * FROM artik_article')
cursor.execute('SELECT title FROM artik_article')
data = cursor.fetchall()
for row in data:
    print(row)

# Fermez la connexion
conn.close()
