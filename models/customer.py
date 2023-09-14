from app import db

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(64))
    drink = db.relationship('Drink', backref='customer')
    def __repr__(self):
        return f"<Customer ID {self.id}: {self.customer_name}>"
