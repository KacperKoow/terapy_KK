#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2013-2014  Vincent Paeder
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""

    Read scan event class (read 1st measured value)

"""

from terapy_2.scan.read import ReadBase

class Read1(ReadBase):
    """
    
        Read scan event class (read 1st measured value)
        
        Read value from selected input device. Stored in provided measurement data structure.
    
    """
    __extname__ = "Read X"
    def __init__(self, parent = None):
        ReadBase.__init__(self, parent)
        self.is_visible = True
        
    def run(self, data):
        if self.can_run:
            inp = self.inlist[self.input]
            data.SetCurrentValue(self.m_id, inp.read()[0])
