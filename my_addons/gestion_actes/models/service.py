from odoo import fields, models

class Service(models.Model):
    _name = 'gestion_patients.service'
    _description = 'Service du cabinet médical'

    name = fields.Char(string='Service', required=True)
    # Autres champs spécifiques au service
