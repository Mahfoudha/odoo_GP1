from odoo import fields, models

class MedicalAct(models.Model):
    _name = 'gestion_patients.medical_act'
    _description = 'Acte Médical'

    name = fields.Char(string='Nom', required=True)
    act_type = fields.Selection([('consultation', 'Consultation'), ('operation', 'Opération'), ('exam', 'Examen'), ('hospitalization', 'Hospitalisation')], string='Type d\'acte')
    amount = fields.Float(string='Montant')
    # Autres champs pour l'acte médical
