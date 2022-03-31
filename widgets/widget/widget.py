from flask import Blueprint, jsonify, request,current_app

from widgets.widget import service

widget_blueprint = Blueprint(
    'widget_bp', __name__)

@widget_blueprint.route('/widgets/', methods=["GET", "POST"])
def widget_list():

    response = []

    if request.method == 'POST':
        response = service.create_widget()

    elif request.method == 'GET':
        name = request.args.get('name')
        response = service.getWidgetbyName(name = name)

    return jsonify(response)




@widget_blueprint.route('/widgets/<int:widget_id>/', methods=["GET", "PUT", "DELETE"])
def widget(widget_id):

    response = {}
    
    if request.method == "PUT":
        response = service.updateWidgetbyID(id = widget_id)

    elif request.method == "DELETE":
        response = service.deleteWidgetbyID(id = widget_id)

    elif request.method == "GET":
        response = service.getWidgetbyID(id = widget_id)

    return jsonify(response)


@widget_blueprint.route('/widgets/<int:widget_id>/options/', methods=["GET", "POST"])
def widget_options(widget_id):

    response = {}

    if request.method == 'POST':
        response = service.createWidgetOption(id = widget_id)

    elif request.method == "GET" :
        response = service.getWidgetOptionByWidgetID(id = widget_id)
    
    return jsonify(response)


@widget_blueprint.route('/widgets/<int:widget_id>/options/<int:option_id>/', methods=["GET", "PUT", "DELETE"])
def widget_option(widget_id, option_id):

    response = {}
    
    if request.method == "PUT":
        response = service.updateWidgetOptionByID(id = option_id)

    elif request.method == "DELETE":
        response = service.deleteWidgetOptionByID(id = option_id)

    elif request.method == "GET":
        response = service.getWidgetOptionByID(id = option_id)
        
    return jsonify(response)