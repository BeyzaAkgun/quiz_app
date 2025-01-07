from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Result page after quiz submission
@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    answers = {
        'q1': 'a', 'q2': 'b', 'q3': 'c', 'q4': 'd', 'q5': 'a'
    }
    
    # Check answers
    for question, correct_answer in answers.items():
        user_answer = request.form.get(question)
        if user_answer == correct_answer:
            score += 1
    
    # Save the user's score
    conn = get_db_connection()
    conn.execute('INSERT INTO scores (score) VALUES (?)', (score,))
    conn.commit()
    conn.close()

    # Get the highest score from the database
    conn = get_db_connection()
    highest_score = conn.execute('SELECT MAX(score) FROM scores').fetchone()[0]
    conn.close()

    # Calculate percentage
    highest_score_percentage = (highest_score / 5) * 100 if highest_score is not None else 0

    return render_template('results.html', score=score, highest_score=highest_score_percentage)

if __name__ == '__main__':
    app.run(debug=True)
