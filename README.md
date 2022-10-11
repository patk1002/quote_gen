# quote_gen repo

## How to initially create the sqlite database:

When creating a sqlite database such as users.db, to avoid this error message:
```
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.
```
for quote_app.py, use the following within Python:
```
>>> from quote_app import db
>>> from quote_app import app
>>> from flask import current_app
>>> with app.app_context():
...     db.create_all()
... 
>>> 
```

## Start the Flask app
python quote_app.py

## Stop the Flask app
Control-C in the terminal window from which quote_app.py was started.

## Sample curl commands to use quote_app:
```
curl --location --request GET '127.0.0.1:5000/api/quotes'

curl --location --request POST '127.0.0.1:5000/api/quotes' \
--header 'Content-Type: application/json' \
--data-raw '{
    "quote_text": "The first quote",
    "quote_date": "2022-10-10",
    "quote_author": "Pat Kelly",
    "quote_url": "empty"
}'

```

## Sample Python code to use quote_app:
```
# Get all quotes
import requests
url = "127.0.0.1:5000/api/quotes"
payload={}
headers = {}
response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

# Create the first quote
import requests
import json
url = "127.0.0.1:5000/api/quotes"
payload = json.dumps({
  "quote_text": "The first quote",
  "quote_date": "2022-10-10",
  "quote_author": "Pat Kelly",
  "quote_url": "empty"
})
headers = {
  'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)

```