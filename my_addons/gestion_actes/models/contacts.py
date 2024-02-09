from odoo import fields, models

class Doctor(models.Model):
    _inherit = 'res.partner'

    is_doctor = fields.Boolean(string='Is Doctor')
    is_patient = fields.Boolean(string='Is Patient')
    # _name = 'gestion_patients.doctor'
    # _description = 'Docteur'
    #
    # name = fields.Char(string='Nom', required=True)
    speciality = fields.Char(string='Spécialité')
    # Autres champs pour le docteur

    birth_date = fields.Date(string='Date de naissance')
    gender = fields.Selection([('male', 'Homme'), ('female', 'Femme')], string='Sexe')
    # Autres champs pour le patient
