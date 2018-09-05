import json
from flask import session
from fast import app
from fast import models


@app.route('/orders' , methods=['GET'])
def all_orders ():
    session.clear()
    session['order_items'] = models.orders
    return json.dumps(session['order_items'])
