import json
from flask import session, abort, request, jsonify
from fast import app
from fast import models


@app.route('/orders' , methods=['GET'])
def all_orders ():
    session.clear()
    session['order_items'] = models.orders
    return json.dumps(session['order_items'])

@app.route('/orders/<int:orderID>' , methods=['GET'])
def single_order (orderID):
    session.clear()
    session['order_items'] = models.orders
    for i in session['order_items']:
        order = i.get(str('id'))
        if order == orderID:
            return json.dumps(i)
    abort(404)

@app.route('/orders' , methods=['POST'])
def add_order ():
    order = request.get_json(silent=True)
    session['order_items'] = models.orders
    for i in session['order_items']:
        found = i.get(str('id'))
        if order['id'] == found:
            abort(422,'Order Already exists')
    session['order_items'].append(order)
    return json.dumps(session['order_items'])

@app.route('/orders/<int:orderID>' , methods=['PUT'])
def update_order (orderID):
    session.clear()
    order_status = request.get_json(silent=True)
    session['order_items'] = models.orders
    for i in session['order_items']:
        order = i.get(str('id'))
        if order == orderID:
            i['status'] = order_status['status']
            return jsonify(session['order_items'])
    return 'Failed'