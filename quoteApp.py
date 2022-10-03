#! /usr/bin/env python3

"""
quoteApp.py is the Python code to Quote-based Database Driven REST API with Python in 10 Minutes.
Code from https://betterdatascience.com/develop-database-driven-rest-api-with-python-in-10-minutes/
and https://gist.github.com/betterdatascience/1b552750a4ab1c6c94c1d4e451ded9f9 
"""

from flask import Flask, request, jsonify 
from flask_sqlalchemy import SQLAlchemy 
from flask_marshmallow import Marshmallow 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Quote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quotename = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))
    first_name = db.Column(db.String(32))
    last_name = db.Column(db.String(32))
    age = db.Column(db.Integer)

    def __init__(self, quotename, password, first_name, last_name, age):
        self.quotename = quotename
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 


class QuoteSchema(ma.Schema):
    class Meta: 
        fields = ('id', 'quotename', 'password', 'first_name', 'last_name', 'age')

quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)


class QuoteManager(Resource):
    @staticmethod
    def get():
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            quotes = Quote.query.all()
            return jsonify(quotes_schema.dump(quotes))
        quote = Quote.query.get(id)
        return jsonify(quote_schema.dump(quote))

    @staticmethod
    def post():
        quotename = request.json['quotename']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        age = request.json['age']

        quote = Quote(quotename, password, first_name, last_name, age)
        db.session.add(quote)
        db.session.commit()
        return jsonify({
            'Message': f'Quote {first_name} {last_name} inserted.'
        })

    @staticmethod
    def put():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the quote ID' })
        quote = Quote.query.get(id)

        quotename = request.json['quotename']
        password = request.json['password']
        first_name = request.json['first_name']
        last_name = request.json['last_name']
        age = request.json['age']

        quote.quotename = quotename 
        quote.password = password 
        quote.first_name = first_name 
        quote.last_name = last_name
        quote.age = age 

        db.session.commit()
        return jsonify({
            'Message': f'Quote {first_name} {last_name} altered.'
        })

    @staticmethod
    def delete():
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the quote ID' })
        quote = Quote.query.get(id)

        db.session.delete(quote)
        db.session.commit()

        return jsonify({
            'Message': f'Quote {str(id)} deleted.'
        })


api.add_resource(QuoteManager, '/api/quotes')

if __name__ == '__main__':
    app.run(debug=True)