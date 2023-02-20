{
    'name': 'Real Estate Custom',
    'version': '1',
    'category': 'Custom',
    'sequence': 15,
    'summary': 'Custom Real estate',
    'depends': [
        'base_setup',
    ],
    'data': [

        'views/real_estate.xml',
        'data/country_states.csv',
        'security/ir.model.access.csv',
    ],

    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}