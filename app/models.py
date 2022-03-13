from flask_sqlalchemy import SQLAlchemy
from app.app import db

class Cars(db.Model):
    id_car = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(80), nullable=False)
    vin = db.Column(db.String(80), nullable=False)
    year = db.Column(db.String(80), nullable=False)
    colour = db.Column(db.String(80), nullable=False)
    complectation = db.Column(db.String(80), nullable=False)
    photo = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    transmission = db.Column(db.Integer, db.ForeignKey('transmissions.id'))
    transmission_connection = db.relationship('Transmissions', backref=db.backref('Cars', lazy=False))
    engine = db.Column(db.Integer, db.ForeignKey('engines.id'))
    engine_connection = db.relationship('Engines', backref=db.backref('Cars', lazy=False))
    body = db.Column(db.Integer, db.ForeignKey('bodies.id'))
    body_connection = db.relationship('Bodies', backref=db.backref('Cars', lazy=False))
    brand = db.Column(db.Integer, db.ForeignKey('brands.id'))
    brand_connection = db.relationship('Brands', backref=db.backref('Cars', lazy=False))

    def __repr__(self):
        return f'({self.id_car}, {self.model})'


class Transmissions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __repr__(self):
        return f'({self.id}, {self.name})'


class Bodies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __repr__(self):
        return f'({self.id}, {self.name})'


class Engines(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __repr__(self):
        return f'({self.id}, {self.name})'


class Brands(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, unique=True)

    def __repr__(self):
        return f'({self.id}, {self.name})'


class Orders(db.Model):
    id_order = db.Column(db.Integer, primary_key=True)
    id_car = db.Column(db.Integer, db.ForeignKey('cars.id_car'), nullable=False)
    car_connection = db.relationship('Cars', backref=db.backref('Orders', lazy=False))
    name_of_customer = db.Column(db.String(80), nullable=False)
    phone = db.Column(db.String(30), nullable=False)
    call_time = db.Column(db.String(80), default='Now')
    status = db.Column(db.String(80), default='Interested')
    best_price = db.Column(db.Integer, default=1000000000)
    def __repr__(self):
        return f'({self.id_order}, {self.id_car}, {self.name_of_customer}, {self.phone})'
