import traceback

from app import db


class Vote(db.Model):

    __tablename__ = 'vote'

    id = db.Column(db.Integer, primary_key=True)
    id_pizza = db.Column(db.Integer)

    def __repr__(self):
        return f'Vote {self.id}'

    def create_vote(self, id_pizza):

        vote = Vote()
        vote.id_pizza = id_pizza

        try:
            db.session.add(vote)
            db.session.commit()
        except Exception:
            print(traceback.print_exc())

        return vote.id

