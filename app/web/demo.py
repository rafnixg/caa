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
            {'name': 'GE Healthcare', 'src': 'img/sponsors/ge.png'},
            {'name': 'Philips', 'src': 'img/sponsors/philips.png'},
            {'name': 'SynLab', 'src': 'img/sponsors/synlab.png'},
        ],
        # Premium
        [
            {'name': 'AGFA', 'src': 'img/sponsors/agfa.png'}
        ],
        # Gold
        [
            {'name': 'Dedalus', 'src': 'img/sponsors/dedalus.png'},
            {'name': 'Ricoh', 'src': 'img/sponsors/ricoh.png'},
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
                'id': 1,
                'firstName': 'Christine',
                'lastName': 'Porath',
                'position': 'Autora de Mastering Civility',
                'img_bio': 'img/expositors/cp_bio.jpg',
                'img_home': 'img/expositors/cp_home.jpg',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Es profesora titular en la McDonough School of Business de la Universidad de Georgetown y es fundadora de una compañía que ayuda a crear un lugar de trabajo más humano donde los empleados puedan desarrollarse.',  # noqa
                'full_description': 'Es profesora titular en la McDonough School of Business de la Universidad de Georgetown y es fundadora de una compañía que ayuda a crear un lugar de trabajo más humano donde los empleados puedan desarrollarse.'  # noqa
            },
            {
                'id': 2,
                'firstName': 'Pedro',
                'lastName': 'Delgado',
                'position': 'Head of Latin America Region, IHI',
                'img_bio': 'img/expositors/pd_bio.png',
                'img_home': 'img/expositors/pd_home.png',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'MSc, Head of Europe and Latin America, Institute for Healthcare Improvement (IHI), has a unique ability to work across cultures, languages, and systems. Based in the United Kingdom, he has been a driving force in IHI’s global strategy.',  # noqa
                'full_description': 'MSc, Head of Europe and Latin America, Institute for Healthcare Improvement (IHI), has a unique ability to work across cultures, languages, and systems. Based in the United Kingdom, he has been a driving force in IHI’s global strategy. From work on reducing C-sections in Brazil, to improving early years education in Chile, to improving patient safety in Portugal and mental health in London, Mr. Delgado has led the key senior relationships and design and implementation of large-scale health system improvement efforts and networks globally. He coaches senior leaders and teams, and lectures extensively worldwide on large-scale change, patient safety, and quality improvement. During his time at IHI, he also facilitated the Quality and Innovation Centers network, which included Kaiser Permanente’s Performance Improvement Institute, Qualturum in Jönköping County (Sweden), and the James Anderson Center for Clinical Excellence at Cincinnati Children’s Hospital. His background is rich in diversity, including a brief period as a professional football (soccer) player, roles in hospital management and large-scale improvement leadership in the UK, and experience working in mental health in Venezuela and the UK. He holds summa cum laude degrees in Psychology and in Global Business, and an MSc in Healthcare Management and Leadership.'  # noqa
            },
            {
                'id': 3,
                'firstName': 'Donald M. Berwick,',
                'lastName': ' MD, MPP, FRCP',
                'position': 'President Emeritus, IHI',
                'img_bio': 'img/expositors/db_bio.png',
                'img_home': 'img/expositors/db_home.png',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'MD, MPP, President Emeritus and Senior Fellow, Institute for Healthcare Improvement, is also former Administrator of the Centers for Medicare & Medicaid Services.',  # noqa
                'full_description': "MD, MPP, President Emeritus and Senior Fellow, Institute for Healthcare Improvement, is also former Administrator of the Centers for Medicare & Medicaid Services. A pediatrician by background, Dr. Berwick has served on the faculty of the Harvard Medical School and Harvard School of Public Health, and on the staffs of Boston's Children's Hospital Medical Center, Massachusetts General Hospital, and the Brigham and Women's Hospital. He has also served as Vice Chair of the US Preventive Services Task Force, the first \"Independent Member\" of the American Hospital Association Board of Trustees, and Chair of the National Advisory Council of the Agency for Healthcare Research and Quality. He served two terms on the Institute of Medicine's (IOM's) Governing Council, was a member of the IOM's Global Health Board, and served on President Clinton's Advisory Commission on Consumer Protection and Quality in the Healthcare Industry. Recognized as a leading authority on health care quality and improvement, Dr. Berwick has received numerous awards for his contributions. In 2005, he was appointed \"Honorary Knight Commander of the British Empire\" by the Queen of England in recognition of his work with the British National Health Service. Dr. Berwick is the author or co-author of over 160 scientific articles and five books. He also serves as Lecturer in the Department of Health Care Policy at Harvard Medical School."  # noqa
            },
            ],
            [{
                'id': 4,
                'firstName': 'Gonzalo Garrido',
                'lastName': 'Lecca',
                'position': 'President, Clinica Anglo Americana',
                'img_bio': 'img/expositors/gg_bio.png',
                'img_home': 'img/expositors/gg_home.png',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': '',  # noqa
                'full_description': ''  # noqa
            },
            {
                'id': 5,
                'firstName': '',
                'lastName': '',
                'position': '',
                'img_bio': '',
                'img_home': '',
                'facebook': '',
                'twitter': '',
                'instagram': '',
                'description': '',  # noqa
                'full_description': ''  # noqa
            },
            {
                'id': 6,
                'firstName': '',
                'lastName': '',
                'position': '',
                'img_bio': '',
                'img_home': '',
                'facebook': '',
                'twitter': '',
                'instagram': '',
                'description': '',  # noqa
                'full_description': ''  # noqa
            },
            ],
        ]
        },
        {
        'tab': 'speaker',
        'data': [
            [{
                'id': 7,
                'firstName': 'Paulo',
                'lastName': 'Borem',
                'position': 'Director of Latin America Region, IHI',
                'img_bio': 'img/expositors/pb_bio.png',
                'img_home': '',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'MD, is a Senior Director and Improvement Advisor (IA) at the Institute for Healthcare Improvement (IHI), as well as a certified Patient Safety Officer (PSO) and Vascular Surgeon by clinical training.',  # noqa
                'full_description': 'MD, is a Senior Director and Improvement Advisor (IA) at the Institute for Healthcare Improvement (IHI), as well as a certified Patient Safety Officer (PSO) and Vascular Surgeon by clinical training. Dr. Borem leads IHI’s large-scale improvement initiatives in Portugal (the STOP Infecao Hospitalar initiative halved hospital acquired infection rates in 36 months across 19 public hospitals) and in Brazil (the Parto Adequado initiative aims to significantly increase the percentage of vaginal births across 117 maternities; the Saude em Nossas Maos initiative aims to halve hospital acquired infections in 119 public hospital ICU’s; and the Collaborative Sepsis ACSC, initiative aims to reduce sepsis mortality across 12 emergency departments); Collaborative Sepsis PROADI, involving 60 ambulatory unit from public sector health in Brazil and a Collaborative to reduce maternal mortality in 27 public hospitals also in Brazil. Dr. Borem is also responsible for IHI’s improvement capability programming in Portuguese-speaking countries, primarily the Improvement Science in Action and Improvement Specialist programs in Brazil. Prior to joining IHI, Dr. Borem worked as a consultant in health care reform and quality for World Bank and USAID in India, Argentina, México and Mozambique.'  # noqa
            },
            {
                'id': 8,
                'firstName': 'Jafet',
                'lastName': 'Arrieta',
                'position': 'Director of Latin America Region, IHI',
                'img_bio': 'img/expositors/ja_bio.png',
                'img_home': '',
                'facebook': '#',
                'twitter': '#',
                'instagram': '#',
                'description': 'Jafet Arrieta currently serves as Director and Improvement Advisor for the Institute for Healthcare Improvement (IHI)',  # noqa
                'full_description': 'Jafet Arrieta currently serves as Director and Improvement Advisor for the Institute for Healthcare Improvement (IHI). In her role, she supports domestic and international partners in the development and implementation of large-scale quality improvement projects, teaches quality improvement methods and provides strategic guidance and coaching to leaders, managers and team members. \n Jafet has extensive experience in operational, oversight, management and leadership roles within the areas of public health, quality improvement and health systems strengthening across different low-, middle-, and high-resource settings. Jafet is an affiliate member of Ariadne Labs, and has previously served as Improvement Advisor for the Latin American Consortium for Innovation, Quality and Safety in Healthcare (CLICSS) leading the implementation of two multi-country quality improvement collaboratives aimed at reducing the incidence of healthcare-associated infections in Latin America, and as Director of Operations for Partners In Health Mexico, helping establish a public-private partnership and leading the execution of a health system strengthening strategy to improve access to high quality care in one of the most underserved regions of Mexico.'  # noqa
            },
            {
                'id': 9,
                'firstName': '',
                'lastName': '',
                'position': '',
                'img_bio': '',
                'img_home': '',
                'facebook': '',
                'twitter': '',
                'instagram': '',
                'description': '',  # noqa
                'full_description': ''  # noqa
            }]
            # [{
            #     'firstName': 'Brent',
            #     'lastName': 'Ray',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image4.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jeremy',
            #     'lastName': 'Robinson',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image5.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jacob',
            #     'lastName': 'Saunders',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image0.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # ],
            # [{
            #     'firstName': 'Isaiah',
            #     'lastName': 'Anderson',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image1.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jeanette',
            #     'lastName': 'McKinney',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image2.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Ann',
            #     'lastName': 'Herrera',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image3.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # ],
        ]
        },
        {
        'tab': 'panelista',
        'data': [
            # [{
            #     'firstName': 'Isaiah',
            #     'lastName': 'Anderson',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image1.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jeanette',
            #     'lastName': 'McKinney',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image2.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Ann',
            #     'lastName': 'Herrera',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image3.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # ],
            # [{
            #     'firstName': 'Brent',
            #     'lastName': 'Ray',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image4.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jeremy',
            #     'lastName': 'Robinson',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image5.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jacob',
            #     'lastName': 'Saunders',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image0.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # ]
        ]
        },
        {
        'tab': 'moderador',
        'data': [
            # [{
            #     'firstName': 'Brent',
            #     'lastName': 'Ray',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image4.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jeremy',
            #     'lastName': 'Robinson',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image5.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jacob',
            #     'lastName': 'Saunders',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image0.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # ],
            # [{
            #     'firstName': 'Isaiah',
            #     'lastName': 'Anderson',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image1.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Jeanette',
            #     'lastName': 'McKinney',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image2.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # {
            #     'firstName': 'Ann',
            #     'lastName': 'Herrera',
            #     'position': 'Vice Presitende Netflix',
            #     'img_bio': 'img/expositors/image3.jpg',
            #     'facebook': '#',
            #     'twitter': '#',
            #     'instagram': '#',
            #     'description': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sit amet metus ut felis finibus tincidunt. Nulla facilisi. Morbi posuere dui eget vehicula tincidunt. Phasellus semper, nulla sit amet sollicitudin finibus, tellus nunc finibus sem, nec aliquam sapien justo et lorem'  # noqa

            # },
            # ],
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
            # 'Precios de <br> preventa <br> <strong>Hasta el 5 de julio</strong>',
            'Precios regulares <br> <strong>a partir del 6 de <br> abril</strong>'
        ],
        'body': [
            {
                'ticket': 'General',
                'preforo': 'Acceso al minicurso <br> full day',
                'foro': 'Acceso a Sala Plenaria <br> + Salas Paralelas',
                'preforoAndForo': 'Acceso al minicurso <br> + Sala Plenaria <br> + Salas Paralelas',  # noqa
                # 'preSale': '30 USD',
                'price': '513 USD'
            },
            {
                'ticket': 'Enfermera(o)',
                'preforo': 'Acceso al minicurso <br> full day',
                'foro': 'Acceso a Sala Plenaria <br> + Salas Paralelas',
                'preforoAndForo': 'Acceso al minicurso <br> + Sala Plenaria <br> + Salas Paralelas',  # noqa
                # 'preSale': '40 USD',
                'price': '308 USD'
            },
            {
                'ticket': 'Estudiante',
                'preforo': 'Acceso al minicurso <br> full day',
                'foro': 'Acceso a Sala Plenaria <br> + Salas Paralelas',
                'preforoAndForo': 'Acceso al minicurso <br> + Sala Plenaria <br> + Salas Paralelas',  # noqa
                # 'preSale': '50 USD',
                'price': '308 USD'
            },
            {
                'ticket': 'Corporativo',
                'preforo': 'Acceso al minicurso <br> full day',
                'foro': 'Acceso a Sala Plenaria <br> + Salas Paralelas',
                'preforoAndForo': 'Acceso al minicurso <br> + Sala Plenaria <br> + Salas Paralelas',  # noqa
                # 'preSale': '80 USD',
                'price': '369 USD'
            }
        ]
    }
