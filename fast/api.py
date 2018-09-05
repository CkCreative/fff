import json
from flask import session
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