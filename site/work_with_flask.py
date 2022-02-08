from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  # объект приложения Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testdb.db'  # привязываем базу данных
db = SQLAlchemy(app)  # создаем объект SQLAlchemy


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

'''
# db.create_all()
reno = Cars.query.all()[0]
bmw = Cars.query.all()[1]
maserati = Cars.query.all()[2]
car = Cars(model='GranTurismo', vin='5555555555', year='2020', colour='black', complectation='speed+', photo='link3',
           price=1050010500, description='Обалдеть, еще быстрее BMW, но не такая комфортная', transmission_connection=obj1, engine_connection=obj2,
           body_connection=body, brand_connection=brand)

# order1 = Orders(car_connection=reno, name_of_customer='Иван', phone='+77777777777')
order2 = Orders(car_connection=bmw, name_of_customer='Никита', phone='+79999999999', best_price=12456456564)
order3 = Orders(car_connection=maserati, name_of_customer='Наталья', phone='+78888888888', status='Сделал заказ', best_price=123456)
# db.session.add(car)
# db.session.add(body)
# db.session.add(engine)
db.session.add_all([order2,order3])
db.session.commit()
# print(reno)'''
bmw = Cars.query.all()[1]
third_order = Orders.query.all()[2]
third_order.car_connection = bmw
db.session.add(third_order)
db.session.commit()
