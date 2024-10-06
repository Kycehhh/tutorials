from odoo import fields, models
from datetime import datetime
from dateutil import relativedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
    description = fields.Text()

    postcode = fields.Char(string="Postcode")
    expected_price = fields.Float(string="Expected Price")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    facade = fields.Integer(string="Facade")
    garden = fields.Boolean(string="Garden")
    garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        string="Garden Orientation",
    )

    date_availability = fields.Date(
        string="Available From",
        copy=False,
        default=datetime.today() + relativedelta.relativedelta(months=3),
    )

    sell_price = fields.Float(string="Sell Price", readonly=True, copy=False)

    living_area = fields.Integer(string="Living Area")

    garage = fields.Boolean(string="Garage")
    garden_area = fields.Integer(string="Garden Area")
