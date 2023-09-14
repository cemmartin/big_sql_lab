from app import db

class Drink(db.Model):
    __tablename__ = "drinks"

    id = db.Column(db.Integer, primary_key=True)
    drink_name = db.Column(db.Text())
    size = db.Column(db.String(64))
    customer_id = db.Column(db.Integer, db. ForeignKey('customers.id'))
    def __repr__(self):
        return f"<Drink {self.id}, {self.size}>"