from odoo import fields, models

class RealEstateType(models.Model):
    _name = "estate.property.type"
    _date = "It's the model that defines what property type the real estate is"

    name = fields.Char("Title",required=True,index=True)