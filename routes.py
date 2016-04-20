from flask import Blueprint, Flask, request, session, g, redirect, url_for, abort, render_template, flash
routes = Blueprint('routes', __name__)

@routes.route("/")
def index():
	return render_template("index.html")