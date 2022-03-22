from flask import Blueprint

home_blueprint = Blueprint(
    'home_bp', __name__)

@home_blueprint .route('/')
def intro():
    return "WiseAlpha refactor task"
