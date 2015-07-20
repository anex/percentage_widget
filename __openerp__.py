# -*- encoding: utf-8 -*-
###############################################################################
#
#   Percentage Widget for Odoo
#   Copyright (C) 2015 Epyme
#   @author: Carlos Paredes <cparedes@exds.co>
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program. If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

{
    'name': 'Percentage Widget',
    'version': '0.1',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'web',
    ],
    'author': 'Carlos Paredes',
    'description': """
Percentage Widget
=============
This module add a widget to show percentage symbol.
""",
    'images': [
    ],
    'website': 'https://github.com/anex',
    'category': 'Tools',
    'complexity': 'expert',
    'demo': [],
    'data': [
        'views/percentage_widget_view.xml',
    ],
    'qweb' : [
        'static/src/xml/*.xml',
    ],
    'active': False,
    'installable': True,
    'application': False,
}
