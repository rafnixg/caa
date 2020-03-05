# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""
import base64
import os
import requests
import json
from app import db
from app.register import blueprint
from flask import render_template, redirect, url_for, request, session

# Import data demo
from app.register.models import Client, Assistant, Ticket, SaleOrder, Promocode

from app.register.forms import ClientForm


@blueprint.route('/', methods=['GET', 'POST'])
def index():
    """General ticket type."""
    form = ClientForm(request.form)
    data = {
        'title': 'Registro General',
        'form': form
    }
    if request.method == 'POST':
        if form.validate_on_submit():
            client_id = session.get('client_id')

            greeting = request.form.get('greeting')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            company = request.form.get('company')
            position = request.form.get('position')
            phone = request.form.get('phone')
            email = request.form.get('email')
            address = request.form.get('address')
            if client_id:
                client = Client.query.get(client_id)
                client.greeting = greeting
                client.first_name = first_name
                client.last_name = last_name
                client.company = company
                client.phone = phone
                client.position = position
                client.email = email
                client.address = address
            else:
                client = Client(
                    greeting=greeting,
                    first_name=first_name,
                    last_name=last_name,
                    company=company,
                    phone=phone,
                    position=position,
                    email=email,
                    address=address
                )

                db.session.add(client)
            db.session.commit()
            session['client_id'] = client.id
            return redirect(url_for('register_blueprint.assistants'))
    return render_template('register/index.html', **data)


@blueprint.route('/student')
def student():
    """Index page."""
    data = {
        'title': '6to Foro latinoamericano',
    }

    return render_template('register/index-student.html', **data)


@blueprint.route('/nurse')
def nurse():
    """Index page."""
    data = {
        'title': '6to Foro latinoamericano',
    }
    return render_template('register/index-nurse.html', **data)


@blueprint.route('/assistants', methods=['GET', 'POST'])
def assistants():
    """Assistant page."""
    client_id = session.get('client_id')
    if not client_id:
        return redirect(url_for('register_blueprint.index'))

    if request.method == 'POST':
        assistants = _get_list(
            ('greeting[]',
             'first_name[]',
             'last_name[]',
             'company[]',
             'position[]',
             'phone[]',
             'email[]',
             'address[]'))

        for assistant in assistants:
            if assistant['email']:
                assis = Assistant(
                    greeting=assistant['greeting'],
                    first_name=assistant['first_name'],
                    last_name=assistant['last_name'],
                    company=assistant['company'],
                    phone=assistant['phone'],
                    position=assistant['position'],
                    email=assistant['email'],
                    address=assistant['address'],
                    client_id=client_id
                )
                db.session.add(assis)
                db.session.commit()
        return redirect(url_for('register_blueprint.tickets'))
    data = {
        'title': '6to Foro latinoamericano',
        'client_id': client_id
    }

    return render_template('register/assistants.html', **data)


@blueprint.route('/tickets', methods=['GET', 'POST'])
def tickets():
    """Ticket page."""
    client_id = session.get('client_id')
    if not client_id:
        return redirect(url_for('register_blueprint.index'))
    tickets = Ticket.query.all()

    if request.method == 'GET':
        assistants = Assistant.query.filter(Assistant.client_id == client_id)
        data = {
            'title': '6to Foro latinoamericano',
            'assistants': assistants,
            'tickets': tickets
        }
        return render_template('register/ticket.html', **data)
    elif request.method == 'POST':
        assistants_data = _get_list(('assistant_id[]', 'ticket_type[]'))

        for assistants in assistants_data:
            assistant = Assistant.query.get(int(assistants['assistant_id']))
            assistant.ticket_id = int(assistants['ticket_type'])
            db.session.commit()
        return redirect(url_for('register_blueprint.payment'))


@blueprint.route('/info', methods=['GET', 'POST'])
def info():
    """Info page."""
    client_id = session.get('client_id')
    if not client_id:
        return redirect(url_for('register_blueprint.index'))
    if request.method == 'GET':
        assistants = Assistant.query.filter(Assistant.client_id == client_id)
        data = {
            'title': '6to Foro latinoamericano',
            'assistants': assistants
        }

        return render_template('register/info.html', **data)

    elif request.method == 'POST':
        assistants_data = _get_list(('assistant_id[]', 'lunch[]', 'vegetarian[]', 'celiac[]'))  # noqa

        for assistants in assistants_data:
            assistant = Assistant.query.get(int(assistants['assistant_id']))
            assistant.is_vegan = False
            assistant.is_celiac = False
            assistant.is_luch = False


@blueprint.route('/payment', methods=['GET', 'POST'])
def payment():
    """Payment page."""
    client_id = session.get('client_id')
    if request.method == 'GET':
        if not client_id:
            return redirect(url_for('register_blueprint.index'))

        client = Client.query.get(int(client_id))
        promocode = request.args.get('promocode')
        # Payzen init
        username = os.getenv('PAYZEN_USERNAME')
        password = os.getenv('PAYZEN_PASSWORD')
        base_url = os.getenv('PAYZEN_URL')
        public_key = os.getenv('PAYZEN_PUBLIC_KEY')
        url = "{}{}".format(base_url, 'Charge/CreatePayment')
        authorization = base64.encodebytes(('%s:%s' % (username, password)).encode('utf8')).decode('utf8').replace('\n', '')  # noqa
        headers = {
            'content-type': 'application/json',
            'Authorization': 'Basic {}'.format(authorization)
        }
        tickets_price_total = client.ticket_price_total()
        if promocode == 'CongresoCirugia':
            percent = 0.8
            tickets_price_total = tickets_price_total * percent
        # Data
        payload = {
            "amount": int(tickets_price_total * 100),
            "currency": "PEN",
            "orderId": "OV-{0:04}".format(client_id),  # noqa reverse int(orderId.split('OV-')[1])
            "customer": {
                "email": client.email,
                "reference": client_id,
            }
        }
        # Request payzen form
        r = requests.post(url, data=json.dumps(payload), headers=headers).json()  # noqa
        print(r)
        form_token = r['answer']['formToken']
        tickets_data = client.tickets()

        data = {
            'title': '6to Foro latinoamericano',
            'tickets': tickets_data,
            'ticket_price_total': tickets_price_total,
            'payzen_public_key': public_key,
            'form_token': form_token,
            'promocode': bool(promocode)
        }

        return render_template('register/payment.html', **data)

    elif request.method == 'POST':
        res = json.loads(request.form.get('kr-answer'))
        if res['orderStatus'] == 'PAID':
            sale_order = SaleOrder(
                name=res['orderDetails']['orderId'],
                promocode='',
                status=res['orderStatus'],
                amount_total=res['orderDetails']['orderTotalAmount'],
                tickets_total=0,
                ruc='',
                social_reason='',
                address='',
                # payzen_code=res['transactions']['uuid']
            )

            db.session.add(sale_order)
            db.session.commit()
        return redirect(url_for('register_blueprint.done'))
        # else:
        #     return redirect(url_for('web_blueprint.index'))


@blueprint.route('/done', methods=['GET'])
def done():
    """Susscess pages."""
    data = {
        'title': '6to Foro latinoamericano',
    }
    session.pop('client_id')
    return render_template('register/done.html', **data)


def _get_list(headers):
    values = [request.form.getlist(h) for h in headers]
    items = [{} for i in range(len(values[0]))]
    for x, i in enumerate(values):
        for _x, _i in enumerate(i):
            items[_x][headers[x][:-2]] = _i
    return items
