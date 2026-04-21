import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock API endpointlari
api_endpoints = {
    '/users': {
        'GET': lambda: json.dumps([{'id': 1, 'name': 'John Doe'}, {'id': 2, 'name': 'Jane Doe'}]),
        'POST': lambda: json.dumps({'id': 3, 'name': 'New User'})
    },
    '/products': {
        'GET': lambda: json.dumps([{'id': 1, 'name': 'Product 1'}, {'id': 2, 'name': 'Product 2'}]),
        'POST': lambda: json.dumps({'id': 3, 'name': 'New Product'})
    }
}

# API endpointlar uchun funksiyalar
def get_users():
    return api_endpoints['/users']['GET']()

def post_users():
    return api_endpoints['/users']['POST']()

def get_products():
    return api_endpoints['/products']['GET']()

def post_products():
    return api_endpoints['/products']['POST']()

# API endpointlar uchun routlar
@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return get_users()
    elif request.method == 'POST':
        return post_users()

@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return get_products()
    elif request.method == 'POST':
        return post_products()

if __name__ == '__main__':
    app.run(debug=True)
```

Bu kodda Flask frameworki qo'llaniladi, API endpointlari uchun funksiyalar yaratiladi va API endpointlar uchun routlar yaratiladi. API endpointlari uchun GET va POST metodlari mavjud.
