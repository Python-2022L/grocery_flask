from flask import Flask, request
from db import GroceryDB


app = Flask(__name__)
db = GroceryDB()

# dfkl;sdfk;ld

# view all grocery
@app.route('/grocery')
def all_grocery():
    """Get all grocery"""
    data = db.all()
    # html view
    html = "<h1>View all grocery</h1>"
    html += "<table>"
    html += "<tr><th>Name</th><th>Quantity</th><th>Price</th><th>Type</th></tr>"
    for item in data:
        html += f"<tr><td>{item['name']}</td><td>{item['quantity']}</td><td>{item['price']}</td><td>{item['type']}</td></tr>"
    html += "</table>"
    return html
   
# view add grocery
@app.route('/grocery/add', methods=['POST'])
def add_grocery():
    """Add a grocery"""
    data = request.get_json()
    db.add(data)
    return {"status": "successfully!"}


# view all grocery by type
@app.route('/grocery/type/<type>')
def all_grocery_by_type(type):
    """Get all grocery by type"""
    pass


# view all grocery by name
@app.route('/grocery/name/<name>')
def all_grocery_by_name(name):
    """Get all grocery by name"""
    pass


# view all grocery by price
@app.route('/grocery/price/<float:price>')
def all_grocery_by_price(price):
    """Get all grocery by price"""
    pass



if __name__ == '__main__':
    app.run(debug=True)