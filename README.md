## TRAVIS CI: [![Build Status](https://travis-ci.com/CkCreative/fff.svg?branch=dev)](https://travis-ci.com/CkCreative/fff)
## Features
- Return a list of all orders on **GET** `/orders`
- Return a single order on **GET** `/orders/<orderID>`
- Post an order on **POST** `/orders`
- Update the status of the order on **PUT** `/orders/<orderID>`

## Testing

- Install Git
- Install Python 3
- Install `pytest` in your virtualenv
- Open console and run:
> `git clone https://github.com/CkCreative/fff.git`
>`cd fff && git checkout dev`
>`python run.py`
- On a new console window, cd to the /fff project directory and run:
>`pytest tests.py`
- You can also use Postman to test the endpoints. 

> Sample data to post with POST `/orders`: `{
        "id" : 11,
        "customer_id" : 1254,
        "status" : ""
}`

> Sample data to update order status using PUT `/orders/<orderID>`:
`{
        "status" : "Completed"
 }`

> **Only valid JSON is accepted for POST and PUT**
> To be able to test PUT, first POST and then try PUT to see the changes take effect.
