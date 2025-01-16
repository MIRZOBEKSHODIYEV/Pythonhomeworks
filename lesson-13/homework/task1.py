import sqlite3

# Database Creation
conn = sqlite3.connect('roster.db')
cursor = conn.cursor()

# Define the Roster table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
)
''')

# Insert Data
cursor.executemany('''
INSERT INTO Roster (Name, Species, Age) 
VALUES (?, ?, ?)
''', [
    ("Benjamin Sisko", "Human", 40),
    ("Jadzia Dax", "Trill", 300),
    ("Kira Nerys", "Bajoran", 29)
])

# Update Data
cursor.execute('''
UPDATE Roster 
SET Name = ? 
WHERE Name = ?
''', ("Ezri Dax", "Jadzia Dax"))

# Query Data
cursor.execute('''
SELECT Name, Age 
FROM Roster 
WHERE Species = ?
''', ("Bajoran",))
bajoran_characters = cursor.fetchall()
print("Bajoran Characters:", bajoran_characters)

# Delete Data
cursor.execute('''
DELETE FROM Roster 
WHERE Age > ?
''', (100,))

# Bonus Task: Add a new column and update data
cursor.execute('''
ALTER TABLE Roster 
ADD COLUMN Rank TEXT
''')

cursor.executemany('''
UPDATE Roster 
SET Rank = ? 
WHERE Name = ?
''', [
    ("Captain", "Benjamin Sisko"),
    ("Lieutenant", "Ezri Dax"),
    ("Major", "Kira Nerys")
])

# Advanced Query
cursor.execute('''
SELECT Name, Species, Age, Rank 
FROM Roster 
ORDER BY Age DESC
''')
characters_sorted_by_age = cursor.fetchall()
print("Characters sorted by Age:", characters_sorted_by_age)

# Commit changes and close the connection
conn.commit()
conn.close()
