import os
from flask import Flask
from src import generator
import random as r
app = Flask(__name__)

@app.route("/")
def generate_fibo():
    N = r.randint(1,50)
    html = '<html><body><h1> For N='+str(N)+', the Fibonacci Sum is: '
    html += str(generator.fibo(N))
    html += '</h1></body></html>'
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))