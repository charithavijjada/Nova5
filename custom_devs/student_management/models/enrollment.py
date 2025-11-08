# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class Enrollment(models.Model):
    _name = "enrollment.enrollment"
    _description = "Enrollment"
    _order = "create_date desc"

    name = fields.Char()
   