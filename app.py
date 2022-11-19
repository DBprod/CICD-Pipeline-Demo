import os
from flask import Flask
import random as r
from src import generator
app = Flask(__name__)

@app.route("/")
def generate():
    N = r.randint(1,50)
    sum, title = generator.generate_random_series(N) 
    html = '<html><body><h1> For N='+str(N)+', '+title
    html += str(sum)
    html += '</h1></body></html>'
    return html

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5001)))