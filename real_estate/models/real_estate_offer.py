from odoo import fields, models

class RealEstateOffer(models.Model):
    _name = "estate.property.offer"
    _date = "It's the model that defines the offer for the real estate"

    name = fields.Char("Title",required=True,index=True)