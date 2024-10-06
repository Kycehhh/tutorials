from odoo import fields, models


class EstateProperty(models.Model):
    _name = "estate_property"
    _description = "Real Estate Property"
    _postcode = fields.Char(string="Postcode")
    _date_availability = fields.Date(string="Available From", copy=False)
    _expected_price = fields.Float(string="Expected Price")
    _sell_price = fields.Float(string="Sell Price", readonly=True, copy=False)
    _bedrooms = fields.Integer(string="Bedrooms")
    _living_area = fields.Integer(string="Living Area")
    _facade = fields.Selection(
        [("brick", "Brick"), ("stone", "Stone"), ("wood", "Wood")],
        string="Facade",
    )
    _garage = fields.Boolean(string="Garage")
    _garden = fields.Boolean(string="Garden")
    _garden_area = fields.Integer(string="Garden Area")
    _garden_orientation = fields.Selection(
        [
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        string="Garden Orientation",
    )

    name = fields.Char(required=True)
    description = fields.Text()
    _expected_price = fields.Float(required=True)

    availability_date = fields.Date(
        string="Availability Date", copy=False
    )  # Prevent copying
    selling_price = fields.Float(
        string="Selling Price", readonly=True, copy=False
    )  # Read-only and no copying
