# -*- encoding: utf-8 -*-
"""Data demo."""


def tickets_data():
    """Tickets types demo data."""
    return [
        {
            'dates': ['29'],
            'title': '6th Latin American Forum on Quality and Safety in Healthcare',
            'service': 'Almuerzo | cóctel | Workshop 1',
            'name': 'Antonio Olson'
        },
        {
            'dates': ['27', '28', '29'],
            'title': '6th Latin American Forum on Quality and Safety in Healthcare',
            'service': 'Almuerzo | cóctel | Workshop 1',
            'name': 'Antonio Olson'
        }
    ]

def tickets_type():
    return [{
        'name': 'Preforo - [28/09]',
        'id': 1,
        'price': 40
        },{
        'name': 'Foro - [29/09 - 29/09]',
        'id': 2,
        'price': 50
        },{
        'name': 'Preforo + Foro - [28/09 - 29/09 - 30/09]',
        'id': 3,
        'price': 60
    }]