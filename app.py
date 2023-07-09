from flask import Flask, render_template

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    background_color = '0000ff'  # Default background color
    return render_template('home.html', background_color=background_color)


# Route for the second page
@app.route('/database')
def database():
    # Retrieve your database data here and pass it to the template
    # Example data
    database_data = [
        {'datetime': 'datadb'},
        {'temperature': 'tempdb'},
        {'soilhumidity': 'shdb'},
        {'ambienthumidity': 'ahdb'}
    ]
    return render_template('database.html', data=database_data)

if __name__ == '__main__':
    app.run(debug=True)
