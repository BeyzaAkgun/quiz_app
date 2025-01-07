import sqlite3

# Veritabanı bağlantısını aç
conn = sqlite3.connect('database.db')

# Tabloyu oluştur
conn.execute('''CREATE TABLE IF NOT EXISTS scores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    score INTEGER NOT NULL
                );''')

# Bağlantıyı kapat
conn.close()

print("Database and table created successfully!")
