from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

def get_db_connection():
    conn = mysql.connector.connect(
        host=app.config['localhost'],
        user=app.config['root'],
        password=app.config[''],
        database=app.config['recipe_db']
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM recipes')
    recipes = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=('GET', 'POST'))
def add_recipe():
    if request.method == 'POST':
        title = request.form['title']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO recipes (title, ingredients, instructions) VALUES (%s, %s, %s)',
                       (title, ingredients, instructions))
        conn.commit()
        cursor.close()
        conn.close()
        flash('Recipe added successfully!')
        return redirect(url_for('index'))

    return render_template('add_recipe.html')

if __name__ == '__main__':
    app.run(debug=True)