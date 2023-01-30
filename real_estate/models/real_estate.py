from odoo import fields, models

class RealEstate(models.Model):
    _name = "real.estate"
    _date = "It's the model that defines what a house is"

    name = fields.Char()