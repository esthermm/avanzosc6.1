
# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution    
#    Copyright (C) 2008-2012 Daniel (AvanzOSC). All Rights Reserved
#    
#    
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################



{
    "name" : "Avanzosc Claim mod",
    "version" : "1.0",
    "description": """ 
                This module adds:
                 - Filter for team group
                    """,
    "author" : "AvanzOSC",
    "website" : "www.avanzosc.com",
    "depends" : ["base","crm_claim"],
    "category" : "Generic Modules",
    "init_xml" : [],
    "demo_xml" : [],
    "update_xml" : ["claim_mod_view.xml",
                    ],
    "active" : False,
    "installable" : True
    
}

