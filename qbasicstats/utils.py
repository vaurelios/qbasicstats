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

def isfloat(test):
    try:
        float(test)
        return True
    except ValueError:
        return False

def isint(test):
    return test.isdigit()

def implode(lst, sep=" "):
    text = ""

    for i in range(len(lst)):
        fmt = "{}"

        if not i == len(lst) - 1:
            fmt += sep

        text += fmt.format(lst[i])

    return text