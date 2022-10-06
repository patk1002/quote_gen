#! /usr/bin/env python

# Some code from https://www.youtube.com/watch?v=s_ht4AKnWZg

from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({'You sent': some_json}), 201
    else:
        return jsonify({"about": "Hello World in json dictionary!"})

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
        return jsonify({"result": num*10})

if __name__ == "__main__":
    app.run(debug=True)

# Use 'curl -v http://127.0.0.1:5000/' to see output without browser OR
#   use 'curl -v http://127.0.0.1:5000/multi/16 OR
#   use 'curl -H "Content-Type: application/json" -X POST -d '{"name":"Pat", "city":"Sugar Land", "state":"TX"}' http://127.0.0.1:5000/ 
