import requests
import json
import fast

client = fast.app.test_client()

def test_get_all_orders():
    r = client.get('http://127.0.0.1:5000/orders')
    assert r.status_code == 200.


def test_get_one_order(requests_mock):
    data = {
        "id" : 11,
        "customer_id" : 1254,
        "status" : ""
    }
    client.post('http://127.0.0.1:5000/orders', json=data)
    r = client.get('http://127.0.0.1:5000/orders/11')
    assert r.status_code == 200

    r_two = client.get('http://127.0.0.1:5000/orders/13')
    assert r_two.status_code == 404


def test_post_order(requests_mock):
    data = {
        "id" : 12,
        "customer_id" : 1254,
        "status" : ""
    }
    before = client.get('http://127.0.0.1:5000/orders/12')
    client.post('http://127.0.0.1:5000/orders', json=data)
    after = client.get('http://127.0.0.1:5000/orders/12')
    assert before.status_code == 404
    assert after.status_code == 200


def test_update_order(requests_mock):
    data = {
        "id" : 14,
        "customer_id" : 1254,
        "status" : ""
    }
    update = {
        "status" : "Completed"
    }
    updated = {
        "id" : 14,
        "customer_id" : 1254,
        "status" : "Completed"
    }
    client.post('http://127.0.0.1:5000/orders', json=data)
    client.put('http://127.0.0.1:5000/orders/14', json=update) 
    res = client.get('http://127.0.0.1:5000/orders/14')
    assert json.loads(res.get_data()) == updated
