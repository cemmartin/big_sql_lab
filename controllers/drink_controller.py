from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.customer import Customer
from models.drink import Drink
from app import db

drink_blueprint = Blueprint("drinks", __name__)

@drink_blueprint.route("/drinks")
def get_drinks():
    # customer1 = Customer(customer_name="Bella")
    # customer2 = Customer(customer_name="Sean")
    # customer3 = Customer(customer_name="Sean")
    # customer4 = Customer(customer_name="Evan")
    # customer5 = Customer(customer_name="Teresa")

    # db.session.add(customer1)
    # db.session.add(customer2)
    # db.session.add(customer3)
    # db.session.add(customer4)
    # db.session.add(customer5)

    # drink1 = Drink(drink_name="Iced Mocha", size="Medium", customer=customer1)
    # drink2 = Drink(drink_name="American", size="Small", customer=customer2)
    # drink3 = Drink(drink_name="Oat Hot Chocolate", size="Large", customer=customer3)
    # drink4 = Drink(drink_name="White Caramel Chocolate Mocha", size="Large", customer=customer4)
    # drink5 = Drink(drink_name="Chai", size="Large", customer=customer5)
    # drink6 = Drink(drink_name="Americano", size="Medium", customer=customer4)

    # db.session.add(drink1)
    # db.session.add(drink2)
    # db.session.add(drink3)
    # db.session.add(drink4)
    # db.session.add(drink5)
    # db.session.add(drink6)
    # db.session.commit()

    customers_from_db = Customer.query.all()
    drinks_from_db = Drink.query.all()
    return render_template("index.jinja",
    drinks=drinks_from_db, customers=customers_from_db)

@drink_blueprint.route("/drinks", methods=["POST"])
def save_drink():
    drink_name = request.form["drink"]
    size = request.form["size"]
    customer_id = request.form["customer name"] #what should this be??? customers? customer id? customer name?
    drink_to_be_saved = Drink(drink_name=drink_name,
    size=size, customer_id=customer_id)

    db.session.add(drink_to_be_saved)
    db.session.commit()
    return redirect("/drinks")

@drink_blueprint.route("/drinks/<index>")
def drink_show():
    drink_to_show= Drink.query.get(id)
    return render_template("show.jinja", 
    drink=drink_to_show)


    # drink = drinks[int(index)] #need to check over this bit
    # return render_template("drinks/show.jinja", drink=drink, index=index)



# @bat_blueprint.route("/bats/delete/<id>", methods=["POST"])
# def delete_bat(id):
    # bat_to_delete = Bat.query.get(id)
    # if bat_to_delete:
    #     db.session.delete(bat>to>delete)
    #     de.session.commit()
    #     return