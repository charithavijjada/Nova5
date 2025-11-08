# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from datetime import date

class Student(models.Model):
    _name = "student.student"
    _description = "Student"
    _order = "create_date desc"
    _rec_name = "name"

    name = fields.Char()
