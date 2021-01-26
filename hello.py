#!/usr/bin/env python3

import cgi, cgitb
import os
import json
from templates import login_page, secret_page
from secret import username, password
from http import cookies

# FROM: https://www.askpython.com/python/environment-variables-in-python#:~:text=We%20can%20use%20Python%20os,the%20already%20running%20Python%20program.
# Q1
# for k, v in os.environ.items():
#     print(f'{k}={v}')
# END FROM

# print('Content-Type: text/html')
# print('Content-Type: application/octet-stream')
# print('Content-Type: application/Json') # tell the browers what kind of file sent
# print()
# print(json.dumps(dict(os.environ), indent=2))

# Q2: "QUERY_STRING"
# print('Content-Type: text/html')
# print()
# print("""
# <!doctype html>
# <html>
# <body>
# <h1>HELLO I AM HTML</h1>
# """)
# print(f"<p> QUERY_STRING={os.environ['QUERY_STRING']}</p>")

# print("<ul>")
# for parameter in os.environ['QUERY_STRING'].split('&'):
#     (name, value) = parameter.split('=')
#     print(f"<li><em>{name}</em> = {value}</li>")

# print("""
# </ul>
# </body>
# </html>
# """)

# Q3: "HTTP_USER_AGENT"
# print('Content-Type: text/html')
# print()
# print("""
# <!doctype html>
# <html>
# <body>
# <h1>HELLO I AM HTML</h1>
# """)
# print(f"<p> HTTP_USER_AGENT={os.environ['HTTP_USER_AGENT']}</p>")

# print("""
# </body>
# </html>
# """)


# Lines from 66 to 73 are from Zeo Riell, 2021
# Correct username and passward: abc, 123
# Q5
form = cgi.FieldStorage()
user = form.getfirst("username")
pwd = form.getfirst("password")
print('Content-Type: text/html')
if (user == username and pwd == password):
    print("Set-Cookie: UserID={}".format(user))
    print("Set-Cookie: UserPassword={}".format(pwd))
print()

# Lines from 74 to 80 are from Zeo Riell, 2021
# Q7
C = cookies.SimpleCookie(os.environ["HTTP_COOKIE"])
user_c = None
pwd_c = None 
if C.get("UserID"):
    user_c = C.get("UserID").value
if C.get("UserPassword"):
    pwd_c = C.get("UserPassword").value

# if no any correct input received and has no correct cookies -> login page
if not (user == username and pwd == password) and not (user_c == username and pwd_c == password):
    print(login_page())

else:
    if (user_c or pwd_c): 
        print(secret_page(user_c, pwd_c))
    else:
        print(secret_page(user, pwd))
