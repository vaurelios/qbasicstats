#!/bin/env python3
# encoding: utf-8

# This file is part of QBasicStats.
#
# QBasicStats is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# QBasicStats is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with QBasicStats.  If not, see <http://www.gnu.org/licenses/>.

from qbasicstats.utils import implode
from qbasicstats.basicstats import do_rol, do_table, do_central_from_rol

if __name__ == '__main__':
    raw = input("Entre com os dados brutos: ").split(" ")

    rol = do_rol(raw)

    print("ROL: {}\n".format(implode(rol)))

    do_table(rol)
    do_central_from_rol(rol)