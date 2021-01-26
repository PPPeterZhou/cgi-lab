#!/usr/bin/env python3

import cgi, cgitb
import json
import os
import sys
import requests
from templates import login_page

print()

posted_bytes = os.environ.get("CONTENT_LENGTH", 0)
if posted_bytes:
    posted = sys.stdin.read(int(posted_bytes))
    print(f"<p> POSTED: <pre>")
    for line in posted.splitlines():
        print(line)
    print("</pre></p>")
    