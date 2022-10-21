import requests
import pyodata
from flask import Flask

SERVICE_URL = 'http://services.odata.org/V2/Northwind/Northwind.svc/'

# Create instance of OData client
client = pyodata.Client(SERVICE_URL, requests.Session())

order = client.entity_sets.Order_Details.get_entity(
    OrderID=10248, ProductID=42).execute()
print(order.Quantity)

app = Flask(__name__)


@app.route("/")
def order_get():
    return "Order quantity: {}".format(order.Quantity)
