#!/usr/bin/env python3

import cgi, cgitb
import json
import os
import sys
import requests
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


# FROM: https://eclass.srv.ualberta.ca/mod/page/view.php?id=4987525, 2021-01-25, by Hazel Campbell, 2021
# Q4
print(login_page())
print("Correct username and passward: abc, 123")
posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    # print(f"<p> POSTED: <pre>")
    #for line in posted.splitlines():
        # print(line)
    # print("</pre></p>")
# END FROM

# FROM: https://docs.python.org/3/library/http.cookies.html
    # Q5
    posted = posted.split("&")
    posted = [i.split('=', 1)[1] for i in posted]
    if (username == posted[0]) and (password == posted[1]):
        print("Login Correct! Setting Cookies...")
        C = cookies.SimpleCookie()
        C["username"] = posted[0]
        C["password"] = posted[1]
        #print(C)

        # Q6
        #print(C.output(header="Cookie"))
        #C.load("username=abc; password=123")
        #print(C)
        print("Complete!")
        print(secret_page(posted[0], posted[1]))
# END FROM

# Q7

