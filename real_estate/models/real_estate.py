from odoo import fields, models

class RealEstate(models.Model):
    _name = "real.estate"
    _date = "It's the model that defines what a house is"

    name = fields.Char(required=True,index=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availibility = fields.Date(copy=False,default=lambda self: fields.Datetime.now())
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True,copy=False)
    bedrooms = fields.Integer(default="2")
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(string='Type', selection=[('north','North'), ('south','South'), ('east','East'), ('west','West')], help="Choose your garden orientation")
    active = fields.Boolean(default=True)
    state = fields.Selection(states='Type', selection=[('new','New'), ('offer received','Offer Received'), ('offer accepted','Offer Accepted'), ('sold','Sold'), ('canceled','Canceled')])