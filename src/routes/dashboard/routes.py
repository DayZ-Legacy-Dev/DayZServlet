from flask import Blueprint, jsonify, request, render_template
from src.utils import Interfaces, log
from datetime import datetime, timedelta
import moment

dashboard = Blueprint("dashboard", __name__)

global_player_count = 0
# Utils
@dashboard.route('/DayZServlet/api/report_player_count', methods=['POST'])
def report_player_count():
    data = request.get_json()
    player_count = data.get('player_count', 0)
    
    # save the player_count somewhere, e.g., a global variable or a database
    global_player_count = player_count  # replace with actual method of storing the player count
    
    log("Dashboard", f"Received player count: {player_count}")
    return jsonify({'status': 'success'}), 200

@dashboard.route('/')
def index():
    log("Dashboard", "Accessing index page")

    player_count = global_player_count
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