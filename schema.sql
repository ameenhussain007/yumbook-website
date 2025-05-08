-- Users table
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT NOT NULL UNIQUE,
  email TEXT NOT NULL,
  password TEXT NOT NULL
);

-- Recipes table
CREATE TABLE IF NOT EXISTS recipes (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  short_description TEXT,
  ingredients TEXT,
  instructions TEXT
);

-- Reviews table
CREATE TABLE IF NOT EXISTS reviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  recipe_id INTEGER,
  user_id INTEGER,
  comment TEXT,
  FOREIGN KEY (recipe_id) REFERENCES recipes(id),
  FOREIGN KEY (user_id) REFERENCES users(id)
);
INSERT INTO recipes (name, short_description, ingredients, instructions)
VALUES ('Spaghetti Carbonara', 'Classic Italian pasta dish', 'Spaghetti, Eggs, Cheese, Bacon', 'Cook pasta. Mix eggs and cheese. Combine with bacon and pasta.');
