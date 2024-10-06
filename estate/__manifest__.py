# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# -*- coding: utf-8 -*-
{
    "name": "Real Estate Advertisement Module",
    "summary": "Real Estate Advertisement Module",
    "depends": ["base"],
    "application": True,
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",  # Make sure this is included
        "views/estate_menus.xml",  # Add this line to load the menus
    ],
}
