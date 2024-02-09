{
    'name': "gestion_actes",
    'summary': "Module pour la gestion des patients",
    'description': """
        Module personnalisé pour la gestion des patients dans un cabinet médical.
    """,
    'author': "GP1",
    'website': "www.GP1.com",
    'category': 'Healthcare',
    'version': '0.1',
    'depends': ['base' ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/patient_views.xml',
        'views/doctor_views.xml',
        'views/service_views.xml',
        'views/medical_act_views.xml',
        'views/exam_document_views.xml',
        'views/invoice_views.xml',
         'views/contacts.xml',

    ],
}
