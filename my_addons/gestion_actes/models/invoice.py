from odoo import fields, models

class Invoice(models.Model):
    _name = 'gestion_patients.invoice'
    _description = 'Facture'

    name = fields.Char(string='Numéro de facture', required=True)
    patient_id = fields.Many2one('gestion_patients.patient', string='Patient')
    medical_act_ids = fields.Many2many('gestion_patients.medical_act', string='Actes Médicaux')
    total_amount = fields.Float(string='Montant total')
    # Autres champs pour la facture
