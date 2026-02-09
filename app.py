from flask import Flask, render_template
import csv

'''
A basic starter Flask app
This app reads a CSV file and serves the data as a web page.
'''

app = Flask(__name__)
data = []

def load_data():
    with open('Pokemon.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            data.append(row)

@app.route('/')
def index():
    '''
    Renders the index page
    :return: The index page
    '''
    return 'Hello, World!'
    
@app.route('/name/<poke_name>/')
def get_pokemon(poke_name):
    '''
    Renders the Pokemon page
    :param poke_name: The Pokemon to display
    :return: The Pokemon's page
    '''
    for pokemon in data:
        if poke_name==pokemon[1]:
            return pokemon
    return "Pokemon not found, try Bulbasaur instead!"

if __name__ == '__main__':
    load_data()
    app.run(port=5100)