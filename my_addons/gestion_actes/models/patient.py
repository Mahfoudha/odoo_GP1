from odoo import models, fields

class Patient(models.Model):
    _name = 'gestion_patients.patient'
    _description = 'Patient'

    name = fields.Char(string='Nom', required=True)
    birth_date = fields.Date(string='Date de naissance')
    gender = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string='Sexe')
    # Autres champs pour le patient
