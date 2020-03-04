# -*- encoding: utf-8 -*-
"""
License: MIT.

Copyright (c) 2019 - present AppSeed.us
"""
import base64
import os
import requests
import json
from pprint import pprint
from app import db
from app.register import blueprint
from flask import render_template, redirect, url_for, request, session

# Import data demo
from app.register.demo import tickets_data
from app.register.models import Client, Assistant, Ticket

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
            greeting = request.form.get('greeting')
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            company = request.form.get('company')
            position = request.form.get('position')
            phone = request.form.get('phone')
            email = request.form.get('email')
            address = request.form.get('address')

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
    tickets = Ticket.query.all()

    if request.method == 'GET':
        client_id = session.get('client_id')
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
    if request.method == 'GET':
        client_id = session.get('client_id')
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
        if client_id:
            # Payzen init
            username = os.getenv('PAYZEN_USERNAME')
            password = os.getenv('PAYZEN_PASSWORD')
            base_url = os.getenv('PAYZEN_URL')
            public_key = os.getenv('PAYZEN_PUBLIC_KEY')
            base64string = base64.encodebytes(('%s:%s' % (username, password)).encode('utf8')).decode('utf8').replace('\n', '')  # noqa
            headers = {
                'content-type': 'application/json',
                'Authorization': 'Basic {}'.format(base64string)
            }
            url = "{}{}".format(base_url, 'Charge/CreatePayment')

            client = Client.query.get(int(client_id))

            tickets_price_total = client.ticket_price_total()

            payload = {
                "amount": 9000,
                "currency": "PEN",
                "orderId": "myOrderId-321979",
                "customer": {
                    "email": "rafnixg@gmail.com"
                }
            }
            r = requests.post(url, data=json.dumps(payload), headers=headers)
            formToken = r.json()['answer']['formToken']
            data = {
                'title': '6to Foro latinoamericano',
                'tickets': tickets_data(),
                'ticket_price_total': tickets_price_total,
                'payzen_public_key': public_key,
                'form_token': formToken,
            }

            return render_template('register/payment.html', **data)
        else:
            return redirect(url_for('web_blueprint.index'))
    elif request.method == 'POST':
        pprint(request.headers)
        pprint(request.form)
        return redirect(url_for('web_blueprint.index'))


def _get_list(headers):
    values = [request.form.getlist(h) for h in headers]
    items = [{} for i in range(len(values[0]))]
    for x, i in enumerate(values):
        for _x, _i in enumerate(i):
            items[_x][headers[x][:-2]] = _i
    return items
