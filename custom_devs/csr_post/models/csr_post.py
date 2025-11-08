from odoo import models, fields

class CSRPost(models.Model):
    _name = 'csr.post'
    _description = 'CSR Post'

    title = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
