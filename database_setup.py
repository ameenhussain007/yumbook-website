import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("database.db")
cursor = conn.cursor()

# Create recipes table
cursor.execute("""
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    image TEXT NOT NULL,
    ingredients TEXT NOT NULL,
    instructions TEXT NOT NULL
)
""")

# Insert sample recipes
cursor.execute("INSERT INTO recipes (name, category, image, ingredients, instructions) VALUES (?, ?, ?, ?, ?)", 
               ("Spaghetti Bolognese", "Non-Vegetarian", "spaghetti.jpg", 
                "Pasta, ground beef, tomato sauce, onion, garlic", 
                "1. Cook pasta. 2. Sauté onion & garlic. 3. Add beef & sauce."))

cursor.execute("INSERT INTO recipes (name, category, image, ingredients, instructions) VALUES (?, ?, ?, ?, ?)", 
               ("Vegetable Stir Fry", "Vegetarian", "stirfry.jpg", 
                "Broccoli, bell pepper, soy sauce, garlic, tofu", 
                "1. Sauté veggies. 2. Add tofu. 3. Stir in soy sauce."))

# Save changes and close connection
conn.commit()
conn.close()

print("Database setup complete. Recipes table created!")
