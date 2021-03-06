#### Travis CI: [![Build Status](https://travis-ci.com/CkCreative/fff.svg?branch=dev)](https://travis-ci.com/CkCreative/fff) Better Code: [![BCH compliance](https://bettercodehub.com/edge/badge/CkCreative/fff?branch=release)](https://bettercodehub.com/) Coveralls: [![Coverage Status](https://coveralls.io/repos/github/CkCreative/fff/badge.svg?branch=dev)](https://coveralls.io/github/CkCreative/fff?branch=dev)
## Features
- Return a list of all orders on **GET** `https://fast-food-fast-api.herokuapp.com/api/v1/orders`
- Return a single order on **GET** `https://fast-food-fast-api.herokuapp.com/api/v1/orders/<orderID>`
- Post an order on **POST** `https://fast-food-fast-api.herokuapp.com/api/v1/orders`
- Update the status of the order on **PUT** `https://fast-food-fast-api.herokuapp.com/api/v1/orders/<orderID>`

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

> Sample data to post with **POST** `/api/v1/orders`: `{
        "id" : 11,
        "customer_id" : 1254,
        "status" : ""
}`

> Sample data to update order status using **PUT** `/api/v1/orders/<orderID>`:
`{
        "status" : "Completed"
 }`

> **Only valid JSON is accepted for POST and PUT**
> To be able to test **PUT**, first **POST** and then try **PUT** to see the changes take effect.
