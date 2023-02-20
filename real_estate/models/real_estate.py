from odoo import fields, models

class RealEstate(models.Model):
    _name = "real.estate"
    _date = "It's the model that defines what a house is"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availibility = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Type', selection=[('north','North'), ('south','South'), ('east','East'), ('west','West')], help="Choose your garden orientation")
