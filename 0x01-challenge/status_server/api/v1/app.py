#!/usr/bin/python3
"""
Web server
"""
from flask import Flask, jsonify, make_response

app = Flask(__name__)

# Define a route for /api/v1/status
@app.route('/api/v1/status', methods=['GET'])
def api_status():
        return jsonify({"status": "API is running"})

@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
                    
