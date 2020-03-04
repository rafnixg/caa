from datetime import datetime
from app import db


class Client(db.Model):
    """Client model."""
    __tablename__ = 'clients'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Form data
    greeting = db.Column(db.String(10))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    company = db.Column(db.String(100))
    position = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    assistants = db.relationship('Assistant', backref='client')

    def __repr__(self):
        return '<Client: {}>'.format(self.first_name)

    def ticket_price_total(self):
        price_total = 0.0
        for assistant in self.assistants:
            price_total += float(assistant.ticket.price)
        return price_total


class Assistant(db.Model):
    """Assistan model."""
    __tablename__ = 'assistants'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Form Assistant
    greeting = db.Column(db.String(10))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    company = db.Column(db.String(100))
    position = db.Column(db.String(100))
    address = db.Column(db.String(200))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(100))

    is_vegan = db.Column(db.Boolean)
    is_celiac = db.Column(db.Boolean)
    is_luch = db.Column(db.Boolean)

    client_id = db.Column(db.Integer(), db.ForeignKey('clients.id'))
    ticket_id = db.Column(db.Integer(), db.ForeignKey('tickets.id'))

    def __repr__(self):
        return '<Assistant: {}>'.format(self.first_name)


class Ticket(db.Model):
    """Tickets model."""
    __tablename__ = 'tickets'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Form Assistant
    name = db.Column(db.String(100))
    price = db.Column(db.Float())

    assistants = db.relationship('Assistant', backref='ticket')

    def __repr__(self):
        return '<Ticket: {}>'.format(self.name)


class Promocode(db.Model):
    """Promocode model."""
    __tablename__ = 'promocodes'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    name = db.Column(db.String(100))
    percent = db.Column(db.Float())
    uses = db.Column(db.Integer())
    max_uses = db.Column(db.Integer())

    def __repr__(self):
        return '<Promocode: {}>'.format(self.name)

    def use(self):
        if self.uses < self.max_uses:
            self.use_increment()

            pass

    def use_increment(self):
        self.uses += 1

    @staticmethod
    def is_promocode(promocode_str):
        promocode = Promocode.query.filter(Promocode.name == promocode_str).first()
        if promocode:
            return True
        else:
            return False
