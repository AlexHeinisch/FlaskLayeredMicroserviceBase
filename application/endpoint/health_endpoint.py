from flask import Blueprint


health = Blueprint('health', __name__)

@health.route('')
def health_check():
    return 'OK', 200
