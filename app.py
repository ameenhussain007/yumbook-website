from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user, logout_user
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import sqlite3
from recipe_data import recipes
from flask import g


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'supersecretkey123'
bcrypt = Bcrypt(app)

recipes = {
    "vegetarian": [
        {
            "name": "Paneer Tikka",
            "image": "paneer.jpg",
            "slug": "paneer-tikka",
            "ingredients": [
                "250g paneer",
                "1/2 cup yogurt",
                "1 tbsp ginger-garlic paste",
                "1 tsp red chili powder",
                "1 tsp turmeric powder",
                "1 tsp garam masala",
                "Salt to taste",
                "1 tbsp lemon juice"
            ],
            "instructions": [
                "Cut paneer into cubes.",
                "In a bowl, mix yogurt, ginger-garlic paste, chili powder, turmeric, garam masala, salt, and lemon juice.",
                "Marinate the paneer in this mixture for at least 1 hour.",
                "Grill or bake the marinated paneer at 180°C for 20 minutes, turning halfway through."
            ]
        },
        {
            "name": "Veg Biryani",
            "image": "biryani.jpg",
            "slug": "veg-biryani",
            "ingredients": [
                "1 cup basmati rice",
                "1/2 cup mixed vegetables (carrot, peas, beans)",
                "1 onion, sliced",
                "1 tomato, chopped",
                "2 tbsp biryani masala",
                "1 tsp ginger-garlic paste",
                "2 tbsp oil",
                "1/2 cup yogurt",
                "1 tsp garam masala",
                "Salt to taste"
            ],
            "instructions": [
                "Cook basmati rice until 70% done and set aside.",
                "In a pan, heat oil, add onions, and cook until golden.",
                "Add ginger-garlic paste, chopped tomatoes, and cook until soft.",
                "Add mixed vegetables and cook for 5 minutes.",
                "Add yogurt, biryani masala, garam masala, and salt, and cook until the oil separates.",
                "Layer the rice on top, add a little water, cover, and cook on low heat for 10-15 minutes."
            ]
        },
        {
            "name": "Chole Bhature",
            "image": "chole.jpg",
            "slug": "chole-bhature",
            "ingredients": [
                "1 cup chickpeas (soaked overnight)",
                "2 onions, finely chopped",
                "2 tomatoes, chopped",
                "1 tbsp ginger-garlic paste",
                "2 tsp chole masala",
                "1 tsp garam masala",
                "1/2 tsp cumin powder",
                "1/2 tsp coriander powder",
                "Salt to taste"
            ],
            "instructions": [
                "Boil soaked chickpeas until soft.",
                "In a pan, heat oil, add onions and cook until golden.",
                "Add ginger-garlic paste, chopped tomatoes, and cook until soft.",
                "Add spices, chickpeas, and some water. Simmer for 15 minutes.",
                "For bhature, make a dough with flour, water, salt, and yeast, then deep fry until puffed."
            ]
        },
        {
            "name": "Palak Paneer",
            "image": "palak.jpg",
            "slug": "palak-paneer",
            "ingredients": [
                "250g paneer",
                "2 cups spinach",
                "1 onion, chopped",
                "2 tomatoes, chopped",
                "1 tsp ginger-garlic paste",
                "1 tsp cumin seeds",
                "1/2 tsp turmeric powder",
                "1 tsp garam masala",
                "Salt to taste"
            ],
            "instructions": [
                "Blanch spinach and blend it into a smooth puree.",
                "In a pan, heat oil, add cumin seeds, and cook until fragrant.",
                "Add onions, ginger-garlic paste, and tomatoes, and cook until soft.",
                "Add spinach puree, spices, and cook for 10 minutes.",
                "Add paneer cubes and cook for 5 minutes."
            ]
        },
        {
            "name": "Aloo Gobi",
            "image": "aloo_gobi.jpg",
            "slug": "aloo-gobi",
            "ingredients": [
                "2 potatoes, cubed",
                "1/2 cauliflower, broken into florets",
                "1 onion, chopped",
                "2 tomatoes, chopped",
                "1 tsp ginger-garlic paste",
                "1/2 tsp cumin seeds",
                "1/2 tsp turmeric powder",
                "1 tsp garam masala",
                "Salt to taste"
            ],
            "instructions": [
                "Heat oil in a pan, add cumin seeds, and cook until they splutter.",
                "Add onions and ginger-garlic paste, and cook until golden.",
                "Add tomatoes, turmeric, and cook for 5 minutes.",
                "Add potatoes and cauliflower, and cook until tender, stirring occasionally.",
                "Add garam masala and salt, cook for 5 more minutes."
            ]
        }
    ],
    "non_vegetarian": [
        {
            "name": "Butter Chicken",
            "image": "butter_chicken.jpg",
            "slug": "butter-chicken",
            "ingredients": [
                "500g boneless chicken",
                "1 cup yogurt",
                "2 tbsp butter",
                "1 cup tomato puree",
                "1/2 cup cream",
                "1 tsp garam masala",
                "1 tsp chili powder",
                "Salt to taste"
            ],
            "instructions": [
                "Marinate the chicken in yogurt, salt, and chili powder for at least 1 hour.",
                "Grill or pan-fry the marinated chicken until slightly charred.",
                "In a pan, melt butter and add tomato puree. Cook for 5 minutes.",
                "Add grilled chicken, garam masala, and salt. Mix well.",
                "Pour in the cream, simmer for 10 minutes until thick.",
                "Garnish with coriander and serve hot with naan or rice."
            ]
        },
        {
            "name": "Mutton Rogan Josh",
            "image": "mutton.jpg",
            "slug": "mutton-rogan-josh",
            "ingredients": [
                "500g mutton pieces",
                "2 onions, sliced",
                "1 tsp ginger-garlic paste",
                "2 tomatoes, chopped",
                "1 tbsp garam masala",
                "1/2 tsp turmeric powder",
                "1 tsp red chili powder",
                "1/2 cup yogurt",
                "Salt to taste"
            ],
            "instructions": [
                "In a pan, heat oil, add onions, and cook until golden.",
                "Add ginger-garlic paste, tomatoes, and cook for 5 minutes.",
                "Add mutton pieces and cook until browned.",
                "Add spices, yogurt, and cook for 20 minutes.",
                "Simmer until mutton is tender and the gravy thickens."
            ]
        },
        {
            "name": "Chicken Biryani",
            "image": "biryani.jpg",
            "slug": "chicken-biryani",
            "ingredients": [
                "1 cup basmati rice",
                "500g chicken pieces",
                "2 onions, sliced",
                "1 tbsp ginger-garlic paste",
                "1/2 cup yogurt",
                "1 tbsp biryani masala",
                "1 tsp garam masala",
                "1/2 cup mint leaves",
                "1 tsp saffron (optional)"
            ],
            "instructions": [
                "Cook basmati rice until 70% done and set aside.",
                "In a pan, cook chicken with onions, ginger-garlic paste, and spices.",
                "Layer the rice and chicken, add saffron and mint leaves.",
                "Cook on low heat for 20 minutes until fragrant."
            ]
        },
        {
            "name": "Fish Curry",
            "image": "fish.jpg",
            "slug": "fish-curry",
            "ingredients": [
                "500g fish fillets",
                "2 tomatoes, chopped",
                "1 onion, chopped",
                "1 tsp ginger-garlic paste",
                "1/2 tsp turmeric powder",
                "1 tsp red chili powder",
                "Salt to taste",
                "1 tbsp mustard oil"
            ],
            "instructions": [
                "In a pan, heat mustard oil and cook onions until golden.",
                "Add ginger-garlic paste, tomatoes, and spices.",
                "Add fish fillets and cook gently in the gravy until cooked through."
            ]
        },
        {
            "name": "Egg Curry",
            "image": "egg.jpg",
            "slug": "egg-curry",
            "ingredients": [
                "4 boiled eggs",
                "2 onions, chopped",
                "2 tomatoes, chopped",
                "1 tsp ginger-garlic paste",
                "1 tsp garam masala",
                "1 tsp chili powder",
                "Salt to taste"
            ],
            "instructions": [
                "Heat oil, add onions, and cook until golden.",
                "Add ginger-garlic paste, tomatoes, and spices, and cook until soft.",
                "Add water to make a curry, simmer for 5 minutes.",
                "Add boiled eggs and cook for 5 more minutes."
            ]
        }
    ]
}

# Initialize login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'  # Name of your login route

app.secret_key = 'your_secret_key'  # Change this to a strong secret key
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
s = URLSafeTimedSerializer(app.secret_key)

serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])

# Configure Flask-Mail for sending reset emails
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your-email@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'your-email-password'  # Replace with your email password

mail = Mail(app)  # Initialize Flask-Mail

db = SQLAlchemy(app)
DATABASE = "users.db"  # SQLite database file
# Add these fields to User model


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    reset_token = db.Column(db.String(100), nullable=True)
    token_expiry = db.Column(db.DateTime, nullable=True)
    saved_recipes = db.relationship('SavedRecipe', backref='owner', lazy=True)

class SavedRecipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    slug = db.Column(db.String(100), nullable=False)  # ✅ Make sure this exists

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(20), nullable=False)  # 'veg' or 'non-veg'
    ingredients = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Recipe {self.name}>'



class ContactMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

def get_saved_recipes_for_user(user_id):
    saved = SavedRecipe.query.filter_by(user_id=user_id).all()
    result = []

    for entry in saved:
        category = entry.category
        slug = entry.slug

        recipe = next((r for r in recipes[category] if r['slug'] == slug), None)
        if recipe:
            recipe_copy = recipe.copy()
            recipe_copy['category'] = category  # add category for URL building
            result.append(recipe_copy)

    return result


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Function to connect to the database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

# Initialize the database and create the users table if not exists
def init_db():
    with app.app_context():
        db = get_db()
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE NOT NULL,
                            password TEXT NOT NULL)''')
        db.commit()

# Close the database connection after request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

        
@app.route("/")
@login_required
def home():
    return render_template("index.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")

@app.route('/save_recipe/<category>/<slug>', methods=['POST'])
@login_required
def save_recipe(category, slug):
    # Check if already saved
    existing = SavedRecipe.query.filter_by(user_id=current_user.id, slug=slug).first()
    if existing:
        flash('Recipe already saved!', 'info')
    else:
        new_saved = SavedRecipe(user_id=current_user.id, slug=slug, category=category)
        db.session.add(new_saved)
        db.session.commit()
        flash('Recipe saved successfully!', 'success')
    return redirect(request.referrer or url_for('home'))
    
@app.route('/saved')
@login_required
def saved():
    saved_recipes = get_saved_recipes_for_user(current_user.id)  # Your function here
    return render_template('saved.html', saved_recipes=saved_recipes)

    
@app.route('/recipes_list')
def recipe_list():
    category = request.args.get('category')
    
    # Use the recipes dictionary you have
    if category == 'vegetarian':
        recipe_list = recipes.get("vegetarian", [])
    elif category == 'non_vegetarian':
        recipe_list = recipes.get("non_vegetarian", [])
    else:
        recipe_list = []

    return render_template('recipes.html', category=category.title(), recipes=recipe_list)


@app.route("/recipes/<category>")
def show_recipes(category):
    if category not in recipes:
        return "Category not found", 404
    return render_template("recipes.html", category=category.capitalize(), recipes=recipes[category])

@app.route("/recipes/<category>/<slug>")
def recipe_detail(category, slug):
    recipe_list = recipes.get(category, [])
    recipe = next((r for r in recipe_list if r["slug"] == slug), None)
    if recipe:
        return render_template("recipe_detail.html", recipe=recipe)
    else:
        return "Recipe not found", 404
    
@app.route('/recipes/vegetarian/<slug>')
def vegetarian_recipe(slug):
    recipe_list = recipes.get('vegetarian', [])
    recipe = next((r for r in recipe_list if r['slug'] == slug), None)
    if recipe:
        return render_template('recipe_detail.html', recipe=recipe)
    return "Recipe not found", 404

@app.route('/recipes/nonvegetarian/<slug>')
def nonvegetarian_recipe(slug):
    recipe_list = recipes.get('non_vegetarian', [])
    recipe = next((r for r in recipe_list if r['slug'] == slug), None)
    if recipe:
        return render_template('recipe_detail.html', recipe=recipe)
    return "Recipe not found", 404

@app.route('/vegetarian')
def vegetarian():
    return render_template(
        'category_recipes.html',
        title='Vegetarian Recipes',
        category_color='#ffcc00',
        recipes=vegetarian_recipes,
        detail_route='vegetarian_recipe'
    )

@app.route('/nonvegetarian')
def nonvegetarian():
    return render_template(
        'category_recipes.html',
        title='Non-Vegetarian Recipes',
        category_color='#ff3300',
        recipes=nonvegetarian_recipes,
        detail_route='nonvegetarian_recipe'
    )



#@app.route('/another-login', methods=['GET', 'POST'])
#def another_login():
  #  if 'user_id' in session:
   #     return redirect(url_for('home'))
   # # continue as usual...
   # return render_template("login.html")


@app.route('/recipes_alt')
def recipes_alt():
    category = request.args.get('category', 'all')  # Default to 'all' if no category is passed

    if category == 'all':
        recipes_list = Recipe.query.all()
    else:
        recipes_list = Recipe.query.filter_by(category=category).all()

    # Pass the recipes to the template to display
    return render_template('recipes.html', recipes=recipes_list, category=category)



@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(username=username, email=email, password=hashed_pw)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully!", "success")
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("home"))
        
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()

        try:
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash(f"Welcome, {user.username}!", "success")
                return redirect(url_for("home"))
            else:
                flash("Invalid email or password", "danger")
        except ValueError:
            flash("Corrupted password data. Please reset your password.", "danger")
            return redirect(url_for("forgot_password"))

    return render_template("login.html")

@app.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password_token(token):
    if current_user.is_authenticated:
        return redirect(url_for("home"))

    user = User.verify_reset_token(token)
    if user is None:
        flash("That is an invalid or expired token", "warning")
        return redirect(url_for("forgot_password"))

    if request.method == "POST":
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            flash("Passwords do not match", "danger")
            return render_template("reset_password.html", token=token)

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user.password = hashed_password
        db.session.commit()
        flash("Your password has been updated! You can now log in.", "success")
        return redirect(url_for("login"))

    return render_template("reset_password.html", token=token)

@app.route('/set-new-password/<token>', methods=['GET', 'POST'])
def set_new_password(token):
    try:
        username = s.loads(token, salt='password-reset-salt', max_age=1800)  # 30 mins
        user = User.query.filter_by(username=username, reset_token=token).first()
    except Exception:
        return "Invalid or expired token."

    if request.method == 'POST':
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        if new_password != confirm_password:
            return "Passwords do not match."

        user.password = generate_password_hash(new_password)
        user.reset_token = None
        user.token_expiry = None
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('set_new_password.html')

@app.route('/reset-confirmation')
def reset_confirmation():
    return render_template('reset_confirmation.html')


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_token(token):
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)  # Token valid for 1 hour
    except SignatureExpired:
        return 'The reset link has expired.'
    except BadSignature:
        return 'Invalid or tampered reset link.'

    if request.method == 'POST':
        new_password = request.form['password']
        hashed_password = generate_password_hash(new_password, method='pbkdf2:sha256')

        user = User.query.filter_by(username=email).first()  # Assuming username is the email
        if user:
            user.password = hashed_password
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return 'User not found.'

    return render_template('reset_password.html', token=token)

@app.route("/forgot_password", methods=["GET", "POST"])
def forgot_password():
    if request.method == "POST":
        email = request.form.get("email")
        print(f"🔍 Email received: {email}")
        # rest of your logic here
        user = User.query.filter_by(email=email).first()
        if user:
            token = serializer.dumps(email, salt='password-reset-salt')
            user.reset_token = token
            user.token_expiry = datetime.utcnow() + timedelta(hours=1)
            db.session.commit()

            reset_url = url_for('reset_password_token', token=token, _external=True)
            print(f"✅ Password reset link: {reset_url}")
            flash('Password reset link has been sent. Check console.', 'info')
        else:
            flash('No account found with that email.', 'danger')

    return render_template('forgot_password.html')

# Route for Dashboard (After Successful Login)
@app.route('/dashboard')
def dashboard():
    if 'user' in session:
        return f"Welcome, {session['user']}! You are now logged in."
    return redirect(url_for('login'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.", "info")
    return redirect(url_for("login"))

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        new_msg = ContactMessage(name=name, email=email, message=message)
        db.session.add(new_msg)
        db.session.commit()

        flash('Your message has been sent! Thank you.', 'success')
        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/messages')
@login_required  # Optional: Only show to admin
def messages():
    all_messages = ContactMessage.query.order_by(ContactMessage.timestamp.desc()).all()
    return render_template('messages.html', messages=all_messages)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print("✅ Database created.")
