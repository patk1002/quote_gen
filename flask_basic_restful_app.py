#! /usr/bin/env python

# Some code from https://www.youtube.com/watch?v=s_ht4AKnWZg

from flask import Flask, jsonify, request
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return jsonify({"about": "Hello World in json dictionary!"})

    def post(self):
        some_json = request.get_json()
        return jsonify({'You sent': some_json}), 201

class Multiby10(Resource):
    def get(self, num):
        return {'result': num*10}

api.add_resource(HelloWorld, '/')
app.add_resource(Multiby10, '/multi/<int:num>')

if __name__ == "__main__":
    app.run(debug=True)

# Use 'curl -v http://127.0.0.1:5000/' to see output without browser OR
#   use 'curl -v http://127.0.0.1:5000/multi/16 OR
#   use 'curl -H "Content-Type: application/json" -X POST -d '{"name":"Pat", "city":"Sugar Land", "state":"TX"}' http://127.0.0.1:5000/ 
