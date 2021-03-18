from flask import Flask, jsonify
from flask_cors import CORS
from src.solver import main

app = Flask(__name__)
CORS(app)


@app.route('/hello')
def say_hello_world():
        result = main()
        # print(steps)
        # d = {"steps": [[0, 2], [1, 4], [1, -1], [1, 7], [2, 4], [3, 3], [4, 6], [6, 8], [6, -1], [4, -1], [4, 8], [6, 6], [6, -1], [4, -1], [4, 9], [6, 6], [8, 8], [10, 1], [12, 4], [13, 6], [13, -1], [12, -1], [12, 6], [13, 4], [13, -1], [12, -1], [10, -1], [10, 5], [12, 1], [13, 4], [14, 6], [16, 2], [16, -1], [16, 9], [16, -1], [14, -1], [13, -1], [13, 6], [14, 4], [16, 2], [16, -1], [16, 9], [16, -1], [14, -1], [13, -1], [12, -1], [12, 4], [13, 1], [14, 6], [16, 2], [16, -1], [16, 9], [16, -1], [14, -1], [13, -1], [13, 6], [14, 1], [16, 2], [16, -1], [16, 9], [16, -1], [14, -1], [13, -1], [12, -1], [12, 6], [13, 1], [14, 4], [16, 2], [16, -1], [16, 9], [16, -1], [14, -1], [13, -1], [13, 4], [14, 1], [16, 2], [16, -1], [16, 9], [16, -1], [14, -1], [13, -1], [12, -1], [10, -1], [8, -1], [6, -1], [6, 8], [8, 6], [10, 1], [12, 4], [13, 6], [13, -1], [12, -1], [12, 6], [13, 4], [13, -1], [12, -1], [10, -1], [10, 5], [12, 1], [13, 4]]}
        return jsonify(result)


