from odoo import fields, models

class ExamDocument(models.Model):
    _name = 'gestion_patients.exam_document'
    _description = 'Document d\'examen'

    name = fields.Char(string='Nom', required=True)
    patient_id = fields.Many2one('gestion_patients.patient', string='Patient')
    # Autres champs pour le document d'examen
