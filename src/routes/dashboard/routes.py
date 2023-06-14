from flask import Blueprint, jsonify, request, render_template
from src.utils import Interfaces, log
from datetime import datetime, timedelta
import moment

dashboard = Blueprint("dashboard", __name__)

@dashboard.route('/')
def index():
    log("Dashboard", "Accessing index page")
    # Get the data you need from the database
    player_count = 0  # replace with your actual method for getting player count

    # Render a template with this data
    return render_template('index.html', player_count=player_count)

@dashboard.route('/users')
def users():
    log("Dashboard", "Accessing users page")
    return render_template('users.html')

@dashboard.route('/cpanel')
def cpanel():
    log("Dashboard", "Accessing cpanel page")
    return render_template('cpanel.html')

@dashboard.route('/logs')
def logs():
    return render_template('logs.html')

@dashboard.route('/patches')
def patches():
    return render_template('patches.html')

@dashboard.route('/executor')
def executor():
    return render_template('executor.html')

@dashboard.route('/stats')
def stats():
    return render_template('stats.html')