import sqlite3

# Connect to SQLite database (creates file if it doesn't exist)
db = sqlite3.connect("ayurveda.db")
cr = db.cursor()

# Create the medicine table
cr.execute("""
CREATE TABLE IF NOT EXISTS medicine (
    id INTEGER PRIMARY KEY,
    category TEXT,
    problem TEXT,
    details TEXT,
    image TEXT,
    link TEXT
)
""")

# Sample data (same as MySQL but fixed for SQLite)
sample_data = [
    (1, 'skin', 'pimples', 'Turmeric has anti-inflammatory...', 'turmeric1.jpg', 'https://www.youtube.com/watch?v=6_M2Pj7uYL4'),
    (2, 'hair', 'hairfall', 'Cut off a fresh leaf from aloe vera...', 'alovera1.jpg', 'https://www.youtube.com/watch?v=LrTfLphOfCA'),
    (3, 'skin', 'oily skin', 'Aloe Vera Treatment...', 'alovera.jpg', 'https://www.youtube.com/watch?v=w8WAXvVSxj8'),
    (4, 'skin', 'dry skin', 'Neem Leaves are great for dry skin...', 'neem.jpg', 'https://www.youtube.com/watch?v=H-dweqlx2hY'),
    (5, 'hair', 'frizzy hair', 'Mash banana and add honey...', 'banana1.jpg', 'https://www.youtube.com/watch?v=HX5WbnmzWjc'),
    (6, 'hair', 'dandruff', 'Amla is great for dandruff...', 'amla.jpg', 'https://www.youtube.com/watch?v=PAvNi0kT0lk'),
    (7, 'hair', 'hair growth', 'Reetha helps hair growth...', 'ritha.jpg', 'https://www.youtube.com/watch?v=qs51klBSLPI'),
    (8, 'skin', 'blackheads', 'Use tomato paste for blackheads...', 'tomato.jpg', 'https://www.youtube.com/watch?v=qOVfY5Zs_Xc'),
    (9, 'skin', 'skin tan', 'Sandalwood remedy for skin tan...', 'sandle.jpg', 'https://www.youtube.com/watch?v=tHSIJzpDGzA'),
    (10, 'hair', 'hair growth', 'Brahmi Bringaraj Taila for hair growth...', 'bringraj.jpg', 'https://www.youtube.com/watch?v=BZMzEHfJkmM')
]

# Insert data into the table if it's empty
cr.execute("SELECT COUNT(*) FROM medicine")
if cr.fetchone()[0] == 0:
    cr.executemany("INSERT INTO medicine (id, category, problem, details, image, link) VALUES (?, ?, ?, ?, ?, ?)", sample_data)

# Commit changes and close database
db.commit()
db.close()

print("Database and sample data created successfully!")
