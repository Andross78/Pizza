import traceback

from app import db


class Topping(db.Model):

    __tablename__ = 'topping'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))


    def __repr__(self):
        return f'Topping {self.name}'


    def create_topping(self, topping_name):

        topping = Topping()
        topping.name = topping_name

        try:
            db.session.add(topping)
            db.session.commit()
        except Exception:
            print(traceback.print_exc())

        return topping