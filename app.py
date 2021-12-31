import traceback

from flask import (
    Flask,
    jsonify,
)

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:your_db_pass@localhost/PizzaDataBase'

app.config['SECRET_KEY'] = 'your_session_key'

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

db = SQLAlchemy(app)
db.init_app(app)

from models.pizza import Pizza
from models.vote import Vote

@app.route('/pizza', methods=['GET'])
def pizza():

    try:
        pizzas = Pizza.query.all()
        output = [Pizza.serialize(pizza) for pizza in pizzas]
        return jsonify(output)

    except Exception:
        print(traceback.print_exc())
        return 'No pizzas'


@app.route('/pizza/<int:pizza_id>', methods=['GET'])
def pizza_details(pizza_id):

    try:
        pizza = Pizza.query.filter_by(id=pizza_id).first()
        output = Pizza.serialize(pizza)
        return jsonify(output)

    except AttributeError:
        return f'No pizza with id {pizza_id}'


@app.route('/pizza/<int:pizza_id>/vote', methods=['GET'])
def pizza_vote(pizza_id):

    try:
        Vote.create_vote(Vote(), pizza_id)
        pizza = Pizza.query.filter_by(id=pizza_id).first()
        output = Pizza.serialize(pizza)
        return jsonify(output)

    except AttributeError:
        return f'Impossilbe to upvote pizza with id {pizza_id}, or pizza does not exists'


@app.errorhandler(404)
def return_to_login(e):
    return "Page does not exists"

if __name__ == '__main__':
    app.run()
