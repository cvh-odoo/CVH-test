from odoo import fields, models

class RealEstateOffer(models.Model):
    _name = "estate.property.offer"
    _date = "It's the model that defines the offer for the real estate"

    name = fields.Char("Title",required=True,index=True)
    price = fields.Float("Price")
    status = fields.Selection(string='Status', selection=[('accepted','Accepted'), ('refused','Refused')],copy=False)
    partner_id = fields.Many2one("res.partner",string="Client",required=True)
    property_id = fields.Many2one("real.estate",string="Offer for",required=True)
    