# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class Course(models.Model):
    _name = "course.course"
    _description = "Course"
    _order = "name asc"

    name = fields.Char(required=True)
    