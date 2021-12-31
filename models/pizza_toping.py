import traceback

from app import db


class PizzaTopping(db.Model):

    __tablename__ = 'pizza_topping'

    id = db.Column(db.Integer, primary_key=True)
    id_pizza = db.Column(db.Integer)
    id_topping = db.Column(db.Integer)


    def __repr__(self):
        return f'Topping {self.id_topping} on pizza {self.id_pizza}'


    def add_toping_to_pizza(self, pizza_id, topping_id):

        pizza_top = PizzaTopping()
        pizza_top.id_pizza = pizza_id
        pizza_top.id_topping = topping_id

        try:
            db.session.add(pizza_top)
            db.session.commit()
        except Exception:
            print(traceback.print_exc())

        return pizza_top
