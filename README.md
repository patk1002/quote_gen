# quote_gen repo

## How to initially create the sqlite datbases:

When creating a sqlite database such as users.db, to avoid this error message:
```
RuntimeError: Working outside of application context.

This typically means that you attempted to use functionality that needed
the current application. To solve this, set up an application context
with app.app_context(). See the documentation for more information.
```
for app_sample.py to the following within Python:
```
>>> from app_sample import db
>>> from app_sample import app
>>> from flask import current_app
>>> with app.app_context():
...     db.create_all()
... 
>>> 
```
mv ./instance/users.db ./users.db

## Sample curl commands to use the app:
```
patu@DESKTOP-BSP4SEV:~/my_git_repos/quote_gen$ curl http://127.0.0.1:5000/api/users
[]
[]
patu@DESKTOP-BSP4SEV:~/my_git_repos/quote_gen$ curl http://127.0.0.1:5000/api/users/0
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
patu@DESKTOP-BSP4SEV:~/my_git_repos/quote_gen$ curl -H "Content-Type: application/json" -X GET http://127.0.0.1:5000/api/users/1
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
patu@DESKTOP-BSP4SEV:~/my_git_repos/quote_gen$ curl -H "Content-Type: application/json" -X POST -d '"username": "patk", "password": "secretpw", "first_name": Pat", "last_name": "Kelly", "age": 50'  http://127.0.0.1:5000/api/users/1
<!doctype html>
<html lang=en>
<title>404 Not Found</title>
<h1>Not Found</h1>
<p>The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.</p>
patu@DESKTOP-BSP4SEV:~/my_git_repos/quote_gen$ curl -H "Content-Type: application/json" -X POST -d '"username": "patk", "password": "secretpw", "first_name": Pat", "last_name": "Kelly", "age": 50'  http://127.0.0.1:5000/api/users
{
    "message": "Failed to decode JSON object: Extra data: line 1 column 11 (char 10)"
}
```
