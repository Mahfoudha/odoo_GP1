from odoo import fields, models

class Doctor(models.Model):
    _name = 'gestion_patients.doctor'
    _description = 'Docteur'

    name = fields.Char(string='Nom', required=True)
    speciality = fields.Char(string='Spécialité')
    # Autres champs pour le docteur
