pip install flask


from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route for the second page
@app.route('/database')
def database():
    # Retrieve your database data here and pass it to the template
    # Example data
    database_data = [
        {'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 30},
        {'name': 'Tom', 'age': 35}
    ]
    return render_template('database.html', data=database_data)

if __name__ == '__main__':
    app.run(debug=True)
