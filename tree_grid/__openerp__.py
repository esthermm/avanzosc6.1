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
    "name" : "Editable Tree Grid",
    "version" : "1.2",
    "author" : "Ting!, Avanzosc",
    "category" : "Generic",
    "depends" : ["base","sale","purchase"],
    "init_xml" : [],
    "description": """
        Editable tree view with virtual and real stocks for sales orders.
        
        Editable tree view for:
            Customer invoices 
            Customer refunds
            Supplier invoices
            Supplier refunds
            Purchase order
            Purchase -> Requests for Quotation
            Journal entries
    """,
    'update_xml': ["editable_tree_view.xml"],
    'installable': True,
    'active': False,

}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
