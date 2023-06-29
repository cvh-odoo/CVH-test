from odoo import fields, models

class RealEstateTags(models.Model):
    _name = "estate.property.tags"
    _date = "It's the model that defines the property tag of the real estate"

    name = fields.Char("Title",required=True,index=True)