from flask import jsonify

def welcome():
    return "Welcome to the Thrive API."

def health_check():
    return jsonify({"status": "healthy"}), 200