from flask_jsonpify import jsonify
from flask import render_template
from app import flask_app
from utils.meetup_utils import MeetupUtils


@flask_app.route("/")
def index():
    """
    Index view to verify the app is running
    """
    return "is working :)"


@flask_app.route("/groups")
def groups():
    """
    Page that shows the list of python meetups groups
    """
    try:
        return render_template('groups.html', groups=MeetupUtils().get_all_groups())
    except Exception as e:
        return render_template('500.html'), 500
