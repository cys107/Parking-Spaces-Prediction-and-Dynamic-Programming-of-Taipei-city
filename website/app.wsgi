#!/usr/bin/python3.6
import os,sys


sys.path.insert(0, "${SRVROOT}/htdocs")

from server import app as application
application.secret_key = "123"
