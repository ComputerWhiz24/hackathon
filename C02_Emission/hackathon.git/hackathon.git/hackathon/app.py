from flask import Flask, render_template, request

views = Flask(__name__ , "views")

# Route to display the home page
@views.route("/")
def home():
    return render_template('home.html')

@views.route("profile/<>")
