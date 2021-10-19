from flask import Flask, request
from kitchen import *
import json
import requests
cooks = json.load(open('cooks.json', 'r'))

app = Flask(__name__)
menu = json.load(open('foods.json', 'r'))
kitchen = Kitchen(cooks, 2, 1, menu['foods'])

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    prepared_food = kitchen.prepare_food(data)
    requests.post('http://localhost:8081/distribution', json=prepared_food)
    return "finish"

app.run(port=8080)