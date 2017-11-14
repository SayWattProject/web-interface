from flask import jsonify, render_template, request
from app import app

@app.route('/energyusage', methods=['GET'])
def energy_usage():
    return render_template('energyusage.html')
