# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Fleet Management System',
    'version': '2.0',
    'category': 'Vertical Modules/Fleet Management',
    'description': """The module is a vertical for fleet operations management""",
    'author': 'Sharoon Thomas (Daniel -Mod)',
    'website': 'http://www.openerp.com',
    'depends': ['base','account','hr','account_voucher','stock_location'],
    'init_xml': [],
    'update_xml': ["security/avanzosc_vehicle_manager_security.xml",
                   "security/ir.model.access.csv",
                   'fleet_view.xml',
                   'fleet_menu.xml',
                   'fleet_sequence.xml',
                   'fleet_workflow.xml',
                   ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
