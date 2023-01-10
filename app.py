# Ioana A Mititean
# Exercise 19.2 - Flask Madlibs

"""
Code for application - setup of Flask and definition of routes and view functions.
"""

from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension

from stories import story, story2

app = Flask(__name__)
app.config['SECRET_KEY'] = "ceva_secreta"

debug = DebugToolbarExtension(app)


@app.route("/")
def homepage():
    """
    Display form for inputting missing words into a Madlibs story.
    """

    return render_template("story_input.jinja2",
                           prompt_list=story2.prompts)


@app.route("/story")
def create_story():
    """
    Display final story, with the missing words filled in by the user.
    """

    final_story = story2.generate(request.args)

    return render_template("final_story.jinja2",
                           final_story=final_story)
