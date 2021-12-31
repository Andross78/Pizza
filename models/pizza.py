import traceback

from app import db

from models.pizza_toping import PizzaTopping
from models.topping import Topping
from models.vote import Vote


class Pizza(db.Model):

    __tablename__ = 'pizza'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return f'Pizza {self.name}'


    def create_pizza(self, pizza_name):

        pizza = Pizza()
        pizza.name = pizza_name

        try:
            db.session.add(pizza)
            db.session.commit()
        except Exception:
            print(traceback.print_exc())

        return pizza

    def serialize(self):


        pizza_toppings = PizzaTopping.query.filter_by(id_pizza=self.id).all()
        pizza_toppings_ids = [p_t.id_topping for p_t in pizza_toppings]

        topings = []
        for i in pizza_toppings_ids:
            topings.append(Topping.query.filter_by(id=i).first().name)

        votes = Vote.query.filter_by(id_pizza=self.id).all()

        output = {
            "id": self.id,
            "name": self.name,
            "toppings_count": len(topings),
            "toppings": topings,
            "votes": len(votes),
        }
        return output