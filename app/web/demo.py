# -*- encoding: utf-8 -*-
"""Data demo."""


def sponsor_types_demo():
    """Sponsor types demo data."""
    return [
        'Elite',
        'Lead',
        'Premium',
        'Gold',
        'Silver',
        'Media Partner Oficial',
        'Media Partners'
    ]


def sponsors_demo():
    """Sponsor demo data."""
    return [
        # Elite
        [],
        # Lead
        [
            {'name': 'GE Healthcare', 'src': 'img/sponsors/GE.png'},
            {'name': 'Philips', 'src': 'img/sponsors/PHILIPS.png'},
            {'name': 'SynLab', 'src': 'img/sponsors/SYNLAB.png'},
        ],
        # Premium
        [],
        # Gold
        [
            {'name': 'Dedalus', 'src': 'img/sponsors/DEDALUS.png'},
            {'name': 'Sura', 'src': 'img/sponsors/SURA.png'},
            {'name': 'Ricoh', 'src': 'img/sponsors/RICOH.png'},
        ],
        # Silver
        [],
        # Media partner oficial
        [],
        # Media Partner
        []
    ]


def schedules_demo():
    """Schedule demo data."""
    return [
        {
            'name': 'Preforo',
            'tab': 'tab1',
            'data': [
                {
                    'description': 'Preforo',
                    'date': '28/09',
                    'class': 'green',
                    'sessions': [
                        {
                            'name': 'Cecilia Roberts',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        },
                        {
                            'name': 'Jeff Tate',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        },
                        {
                            'name': 'Sean Daniels',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        }
                    ]
                }
            ]
        },
        {
            'name': 'Foro Día1 / Día 2',
            'tab': 'tab2',
            'data': [
                {
                    'description': 'Foro día 1',
                    'date': '29/09',
                    'class': 'turquoise',
                    'sessions': [
                        {
                            'name': 'William Hernandez',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        },
                        {
                            'name': 'Jerome Martinez',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        },
                        {
                            'name': 'Nina Terry',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        }
                    ]
                },
                {
                    'description': 'Foro día 2',
                    'date': '30/09',
                    'class': 'fuchsia',
                    'sessions': [
                        {
                            'name': 'Marguerite Carlson',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        },
                        {
                            'name': 'Eva Norton',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        },
                        {
                            'name': 'Ivan Jefferson',
                            'hour': '10.00am - 11.00am',
                            'room': 'Sala 1',
                            'description': 'Plenary Session: Laying the foundations for future success with the new consumer'  # noqa
                        }
                    ]
                }
            ]
        }
    ]


def expositors_demo():
    """Expositor demo data."""
    return [{
        'tab': 'keynote',
        'data': [
            [{
                'firstName': 'Christine',
                'lastName': 'Porath',
                'position': 'Autora de Mastering Civility',
                'img_bio': 'img/expositors/cp_bio.jpg',
                'img_home': 'img/expositors/cp_home.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Es profesora titular en la McDonough School of Business de la Universidad de Georgetown y es fundadora de una compañía que ayuda a crear un lugar de trabajo más humano donde los empleados puedan desarrollarse.'  # noqa
            },
            {
                'firstName': 'Jeanette',
                'lastName': 'McKinney',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image2.jpg',
                'img_home': 'img/backgrounds/expositors-home.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa
            },
            {
                'firstName': 'Ann',
                'lastName': 'Herrera',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image3.jpg',
                'img_home': 'img/backgrounds/expositors-home.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa
            },
            ],
            [{
                'firstName': 'Brent',
                'lastName': 'Ray',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image4.jpg',
                'img_home': 'img/backgrounds/expositors-home.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jeremy',
                'lastName': 'Robinson',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image5.jpg',
                'img_home': 'img/backgrounds/expositors-home.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jacob',
                'lastName': 'Saunders',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image0.jpg',
                'img_home': 'img/backgrounds/expositors-home.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            ]
        ]
        },
        {
        'tab': 'speaker',
        'data': [
            [{
                'firstName': 'Brent',
                'lastName': 'Ray',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image4.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jeremy',
                'lastName': 'Robinson',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image5.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jacob',
                'lastName': 'Saunders',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image0.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            ],
            [{
                'firstName': 'Isaiah',
                'lastName': 'Anderson',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image1.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jeanette',
                'lastName': 'McKinney',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image2.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Ann',
                'lastName': 'Herrera',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image3.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            ],
        ]
        },
        {
        'tab': 'panelista',
        'data': [
            [{
                'firstName': 'Isaiah',
                'lastName': 'Anderson',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image1.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jeanette',
                'lastName': 'McKinney',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image2.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Ann',
                'lastName': 'Herrera',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image3.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            ],
            [{
                'firstName': 'Brent',
                'lastName': 'Ray',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image4.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jeremy',
                'lastName': 'Robinson',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image5.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jacob',
                'lastName': 'Saunders',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image0.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            ]
        ]
        },
        {
        'tab': 'moderador',
        'data': [
            [{
                'firstName': 'Brent',
                'lastName': 'Ray',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image4.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jeremy',
                'lastName': 'Robinson',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image5.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jacob',
                'lastName': 'Saunders',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image0.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            ],
            [{
                'firstName': 'Isaiah',
                'lastName': 'Anderson',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image1.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Jeanette',
                'lastName': 'McKinney',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image2.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            {
                'firstName': 'Ann',
                'lastName': 'Herrera',
                'position': 'Vice Presitende Netflix',
                'img_bio': 'img/expositors/image3.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            },
            ],
        ]
    }]


def inversion_demo():
    """Inversion demo data."""
    return {
        'head': [
            'Entradas',
            'Preforo <br> <strong>28/09</strong>',
            'Foro Día 1/Día 2 <br> <strong>29/09 - 30/09</strong>',
            'Preforo <br> + Foro Día 1/Día 2 <br> <strong>28/09 - 30/09</strong>',
            'Precios de <br> preventa <br> <strong>Hasta el 5 de julio</strong>',
            'Precios regulares <br> <strong>a partir del 6 de <br> abril</strong>'
        ],
        'body': [
            {
                'ticket': 'General',
                'preforo': 'Acceso al minicurso <br> full day',
                'foro': 'Acceso a Sala Plenaria <br> + Salas Paralelas',
                'preforoAndForo': 'Acceso al minicurso <br> + Sala Plenaria <br> + Salas Paralelas',  # noqa
                'preSale': '30 USD',
                'price': '40 USD'
            },
            {
                'ticket': 'Enfermera(o)',
                'preforo': 'Acceso al minicurso <br> full day',
                'foro': 'Acceso a Sala Plenaria <br> + Salas Paralelas',
                'preforoAndForo': 'Acceso al minicurso <br> + Sala Plenaria <br> + Salas Paralelas',  # noqa
                'preSale': '40 USD',
                'price': '50 USD'
            },
            {
                'ticket': 'Estudiante',
                'preforo': 'Acceso al minicurso <br> full day',
                'foro': 'Acceso a Sala Plenaria <br> + Salas Paralelas',
                'preforoAndForo': 'Acceso al minicurso <br> + Sala Plenaria <br> + Salas Paralelas',  # noqa
                'preSale': '50 USD',
                'price': '60 USD'
            },
            {
                'ticket': 'Corporativo',
                'preforo': 'Acceso al minicurso <br> full day',
                'foro': 'Acceso a Sala Plenaria <br> + Salas Paralelas',
                'preforoAndForo': 'Acceso al minicurso <br> + Sala Plenaria <br> + Salas Paralelas',  # noqa
                'preSale': '80 USD',
                'price': '100 USD'
            }
        ]
    }
