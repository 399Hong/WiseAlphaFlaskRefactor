from flask import Blueprint, jsonify, request,current_app
import sqlite3
import utils
from widgets.widget import service

widget_blueprint = Blueprint(
    'widget_bp', __name__)

@widget_blueprint.route('/widgets/', methods=["GET", "POST"])
def widget_list():
    widgets = []

    if request.method == 'POST':
        return jsonify(service.create_widget())
    
    elif request.method == 'GET':
        name = request.args.get('name')
        print("here")
        widgets = service.getWidgetbyName(name)

    return jsonify(widgets)




@widget_blueprint.route('/widgets/<int:widget_id>/', methods=["GET", "PUT", "DELETE"])
def widget(widget_id):
    response = {}
    
    if request.method == "PUT":
        response = service.updateWidgetbyID(widget_id)
    elif request.method == "DELETE":
        response = service.deleteWidgetbyID(widget_id)
    elif request.method == "GET":
        response = service.getWidgetbyID(widget_id)

    return jsonify(response)


@widget_blueprint.route('/widgets/<int:widget_id>/options/', methods=["GET", "POST"])
def widget_options(widget_id):
    response = {}

    if request.method == 'POST':
        response = service.createWidgetOption(widget_id)

    elif request.method == "GET" :
        response = service.getWidgetOptionByWidgetID(widget_id)
    
    return jsonify(response)


@widget_blueprint.route('/widgets/<int:widget_id>/options/<int:option_id>/', methods=["GET", "PUT", "DELETE"])
def widget_option(widget_id, option_id):

    response = {}
    
    if request.method == "PUT":
        response = service.updateWidgetOptionByID(option_id)

    elif request.method == "DELETE":
        response = service.deleteWidgetOptionByID(option_id)
    elif request.method == "GET":
        response = service.getWidgetOptionByID(option_id)
    return jsonify(response)