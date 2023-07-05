from flask import (Flask,current_app,render_template,request,redirect,send_file,url_for,flash,)
from flask_sqlalchemy import SQLAlchemy
import os
from flask_marshmallow import Marshmallow
import datetime

app = Flask(__name__, static_folder="static", template_folder="templates")

marsh = Marshmallow(app)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:gr8ani123@localhost/pharma"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "your_secret_key"

db = SQLAlchemy(app)


class MedEq(db.Model):
    __tablename__ = "medeq"

    id = db.Column(db.String(5), primary_key=True, nullable=False)
    product_name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    rowno = db.Column(db.Integer, nullable=False)  # Changed from 'row' to 'rowno'
    columnno = db.Column(db.Integer, nullable=False)  # Changed from 'column' to 'columnno'
    price = db.Column(db.Integer, nullable=False)


class Supplements(db.Model):
    __tablename__ = "supplements"

    id = db.Column(db.String(5), primary_key=True, nullable=False)
    product_name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    rowno = db.Column(db.Integer, nullable=False)  # Changed from 'row' to 'rowno'
    columnno = db.Column(db.Integer, nullable=False)  # Changed from 'column' to 'columnno'
    price = db.Column(db.Integer, nullable=False)


class OnCounter(db.Model):
    __tablename__ = "oncounter"

    id = db.Column(db.String(5), primary_key=True, nullable=False)
    product_name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    rowno = db.Column(db.Integer, nullable=False)  # Changed from 'row' to 'rowno'
    columnno = db.Column(db.Integer, nullable=False)  # Changed from 'column' to 'columnno'
    price = db.Column(db.Integer, nullable=False)


class PrescriptionMeds(db.Model):
    __tablename__ = "presmed"

    id = db.Column(db.String(5), primary_key=True, nullable=False)
    product_name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    rowno = db.Column(db.Integer, nullable=False)  # Changed from 'row' to 'rowno'
    columnno = db.Column(db.Integer, nullable=False)  # Changed from 'column' to 'columnno'
    price = db.Column(db.Integer, nullable=False)



@app.route("/")
def home():
    return render_template("index1.html")

@app.route("/medeq")
def medeq():
    medeq_records = MedEq.query.all()
    return render_template("medeq.html", medeq_records=medeq_records)

@app.route("/update_medeq", methods=["POST"])
def update_medeq():
    record_id = request.form["id"]
    product_name = request.form["product_name"]
    quantity = request.form["quantity"]
    rowno = request.form["rowno"]
    columnno = request.form["columnno"]
    price = request.form["price"]

    # Fetch the record from the database and update its fields
    record = MedEq.query.get(record_id)
    record.product_name = product_name
    record.quantity = quantity
    record.rowno = rowno
    record.columnno = columnno
    record.price = price

    # Commit the changes to the database
    db.session.commit()

    # Prepare the response data
    response_data = {
        "success": True,
        "record": {
            "id": record.id,
            "product_name": record.product_name,
            "quantity": record.quantity,
            "rowno": record.rowno,
            "columnno": record.columnno,
            "price": record.price,
        }
    }

    return jsonify(response_data)
    

@app.route("/supp")
def supp():
    supp_records = Supplements.query.all()
    return render_template("supp.html",supp_records = supp_records)

@app.route("/update_supp", methods=["POST"])
def update_supp():
    record_id = request.form["id"]
    product_name = request.form["product_name"]
    quantity = int(request.form["quantity"])
    rowno = int(request.form["rowno"])
    columnno = int(request.form["columnno"])
    price = int(request.form["price"])

    # Fetch the record from the database and update its fields
    record = Supplements.query.get(record_id)
    record.product_name = product_name
    record.quantity = quantity
    record.rowno = rowno
    record.columnno = columnno
    record.price = price

    # Commit the changes to the database
    db.session.commit()

    # Prepare the response data
    response_data = {
        "success": True,
        "record": {
            "id": record.id,
            "product_name": record.product_name,
            "quantity": record.quantity,
            "rowno": record.rowno,
            "columnno": record.columnno,
            "price": record.price,
        }
    }

    return jsonify(response_data)


@app.route("/counter")
def counter():
    counter_records = OnCounter.query.all()
    return render_template("counter.html",counter_records = counter_records)

@app.route("/update_counter", methods=["POST"])
def update_counter():
    record_id = request.form["id"]
    product_name = request.form["product_name"]
    quantity = int(request.form["quantity"])
    rowno = int(request.form["rowno"])
    columnno = int(request.form["columnno"])
    price = int(request.form["price"])

    # Fetch the record from the database and update its fields
    record = OnCounter.query.get(record_id)
    record.product_name = product_name
    record.quantity = quantity
    record.rowno = rowno
    record.columnno = columnno
    record.price = price

    # Commit the changes to the database
    db.session.commit()

    # Prepare the response data
    response_data = {
        "success": True,
        "record": {
            "id": record.id,
            "product_name": record.product_name,
            "quantity": record.quantity,
            "rowno": record.rowno,
            "columnno": record.columnno,
            "price": record.price,
        }
    }

    return jsonify(response_data)


@app.route("/pres")
def pres():
    pres_records = PrescriptionMeds.query.all()    
    return render_template("pres.html",pres_records = pres_records)


@app.route("/update_pres", methods=["POST"])
def update_pres():
    record_id = request.form["id"]
    product_name = request.form["product_name"]
    quantity = int(request.form["quantity"])
    rowno = int(request.form["rowno"])
    columnno = int(request.form["columnno"])
    price = int(request.form["price"])

    # Fetch the record from the database and update its fields
    record = PrescriptionMeds.query.get(record_id)
    record.product_name = product_name
    record.quantity = quantity
    record.rowno = rowno
    record.columnno = columnno
    record.price = price

    # Commit the changes to the database
    db.session.commit()

    # Prepare the response data
    response_data = {
        "success": True,
        "record": {
            "id": record.id,
            "product_name": record.product_name,
            "quantity": record.quantity,
            "rowno": record.rowno,
            "columnno": record.columnno,
            "price": record.price,
        }
    }

    return jsonify(response_data)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
