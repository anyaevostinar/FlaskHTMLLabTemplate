from flask import Flask
import csv

'''
A basic starter Flask app
This app reads a CSV file and serves the data as a web page.
'''

app = Flask(__name__)
data = []

def load_data():
    #slightly weird syntax for reading from a file, but apparently the proper Pythonic way:
    with open('dataset.csv', newline='') as f:
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

@app.route('/<row>/<column>', strict_slashes=False)
def get_cell(row, column):
    '''
    Renders the cell page
    :param row: The row of the cell
    :param column: The column of the cell
    :return: The cell page
    '''
    try:
        row = int(row)
        column = int(column)
        return data[row][column]
    except IndexError:
        return 'Index out of range'
    except ValueError:
        return 'Invalid index'

if __name__ == '__main__':
    load_data()
    app.run()