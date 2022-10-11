#! /usr/bin/env python3

"""
quote_app.py is the Python code for a Quote-based Database-driven REST API.
Some code is from https://betterdatascience.com/develop-database-driven-rest-api-with-python-in-10-minutes/
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
    quote_id = db.Column(db.Integer, primary_key=True)
    quote_text = db.Column(db.String(1024), unique=True)
    quote_date = db.Column(db.String(8))
    quote_author = db.Column(db.String(32))
    quote_url = db.Column(db.String(64))

    def __init__(self, quote_text, quote_date, quote_author, quote_url):
        self.quote_text = quote_text
        self.quote_date = quote_date
        self.quote_author = quote_author
        self.quote_url = quote_url 


class QuoteSchema(ma.Schema):
    class Meta: 
        fields = ('quote_id', 'quote_text', 'quote_date', 'quote_author', 'quote_url')

quote_schema = QuoteSchema()
quotes_schema = QuoteSchema(many=True)


class QuoteManager(Resource):
    @staticmethod
    def get():
        try: quote_id = request.args['quote_id']
        except Exception as _: quote_id = None

        if not quote_id:
            quotes = Quote.query.all()
            return jsonify(quotes_schema.dump(quotes))
        quote = Quote.query.get(quote_id)
        return jsonify(quote_schema.dump(quote))

    @staticmethod
    def post():
        quote_text = request.json['quote_text']
        quote_date = request.json['quote_date']
        quote_author = request.json['quote_author']
        quote_url = request.json['quote_url']

        quote = Quote(quote_text, quote_date, quote_author, quote_url)
        db.session.add(quote)
        db.session.commit()
        return jsonify({
            'Message': f'Quote {quote_id} inserted.'
        })

    @staticmethod
    def put():
        try: quote_id = request.args['quote_id']
        except Exception as _: quote_id = None
        if not quote_id:
            return jsonify({ 'Message': 'Must provide the quote quote_id' })
        quote = Quote.query.get(quote_id)

        quote_text = request.json['quote_text']
        quote_date = request.json['quote_date']
        quote_author = request.json['quote_author']
        quote_url = request.json['quote_url']

        quote.quote_text = quote_text 
        quote.quote_date = quote_date 
        quote.quote_author = quote_author
        quote.quote_url = quote_url 

        db.session.commit()
        return jsonify({
            'Message': f'Quote {quote_id} altered.'
        })

    @staticmethod
    def delete():
        try: quote_id = request.args['quote_id']
        except Exception as _: quote_id = None
        if not quote_id:
            return jsonify({ 'Message': 'Must provide the quote ID' })
        quote = Quote.query.get(quote_id)

        db.session.delete(quote)
        db.session.commit()

        return jsonify({
            'Message': f'Quote {str(quote_id)} deleted.'
        })


api.add_resource(QuoteManager, '/api/quotes')

if __name__ == '__main__':
    app.run(debug=True)