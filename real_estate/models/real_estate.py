from odoo import fields, models
from dateutil.relativedelta import relativedelta

class RealEstate(models.Model):
    _name = "real.estate"
    _date = "It's the model that defines what a house is"

    name = fields.Char("Title",required=True,index=True)
    description = fields.Text("Description")
    postcode = fields.Char("Postcode")
    date_availibility = fields.Date("Available from",copy=False,default=lambda self: fields.Date.context_today(self)+relativedelta(months=3))
    expected_price = fields.Float("Expected price",required=True)
    selling_price = fields.Float("Price",readonly=True,copy=False)
    bedrooms = fields.Integer("Bedrooms",default="2")
    living_area = fields.Integer("Living Area (sqm)")
    facades = fields.Integer("Facades")
    garage = fields.Boolean("Garage")
    garden = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area (sqm)")
    garden_orientation = fields.Selection(string='Type', selection=[('north','North'), ('south','South'), ('east','East'), ('west','West')], help="Choose your garden orientation")
    active = fields.Boolean("Active", default=True)
    state = fields.Selection(string='Status', selection=[('new','New'), ('offer received','Offer Received'), ('offer accepted','Offer Accepted'), ('sold','Sold'), ('canceled','Canceled')], default='new', required=True, copy=False)
    partner_id = fields.Many2one("res.partner",string="Buyer")
    res.users_id = fields.Many2one("res.users",string="Salesperson")