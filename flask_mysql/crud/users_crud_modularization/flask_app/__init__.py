# __init__.py
from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
app.secret_key = "shhhhhh"