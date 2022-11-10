import os
from flask import Flask
from src import generator

app = Flask(__name__)

@app.route("/")
def generate_buzz():
    page = '<html><body><h1> For N=9, the Fibonacci Sum is'
    page += str(generator.fibo(9))
    page += '</h1></body></html>'
    return page

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))