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

from collections import Counter
import math

from .utils import *

def get_prev_class(classes, index):
    if index == 0:
        return [(0, 0), 0, 0, 0]

    return classes[index-1]

def do_rol(raw):
    rol = []

    for item in raw:
        if isint(item):
            rol.append(int(item))
        else:
            if isfloat(item):
                rol.append(float(item))

    rol.sort()
    return rol

def do_table(rol):
    n = len(rol)
    H = rol[-1] - rol[0]
    k = int(math.sqrt(n))
    h = int(H / k) + 1

    print("k = sqrt(n) = {}".format(k))
    print("H = L - l = {}".format(H))
    print("h = H / k = {}\n".format(h))

    print("{:-^80}".format(" Distribuição de Frequência "))
    print("{:^13}|{:^7}|{:^9}|{:^8}|".format("Classes", "fi", "Fri", "Fi"))

    classes = []
    prev = []
    for i in range(k):
        l = 0
        if len(prev) == 0:
            l = rol[0]
        else:
            l = prev[1]

        prev = [l, l + h]

        fi = 0
        for item in rol:
            if item >= prev[0] and item < prev[1]:
                fi += 1

        classes.append([(prev[0], prev[1]), fi, (fi * 100) / len(rol), get_prev_class(classes, i)[3] + fi])

    sum_fi = 0
    sum_Fri = 0
    sum_Fi = 0
    for cls in classes:
        rng = "{:>3} ⊢ {:<3}".format(cls[0][0], cls[0][1])
        rel = "{:.1f}%".format(cls[2])

        sum_fi += cls[1]
        sum_Fri += cls[2]
        sum_Fi += cls[3]

        print("{:^13}|{:^7}|{:^9}|{:^8}|".format(rng, cls[1], rel, cls[3]))

    print("-" * 41)
    print("{:>13}|{:^7}|{:^9}|{:^8}|".format("Total", sum_fi, "{:.0f}%".format(sum_Fri), sum_Fi))
    print("\n")

    return classes

def do_central_from_rol(rol):
    n = len(rol)

    # Index da mediana no ROL
    Mei = ((n + 1) / 2.0) - 1

    x = 0
    Me = 0
    Mo = None

    x = sum(rol) / n

    Meii = int(Mei)

    # Mei é um número decial ?
    if Mei - Meii > 0:
        Me = (rol[Meii] + rol[Meii + 1]) / 2.0
    else:
        Me = rol[Meii]

    # mc é os números que mais se repetem no formato [(número, quantidade)]
    mc = Counter(rol).most_common()
    if mc[0][1] > 1:
        Mo = "{}".format(mc[0][0])

        for item in mc[1:]:
            if item[1] == mc[0][1]:
                Mo += ", {}".format(item[0])

    print("{:-^80}".format(" Medidas de Tendencia Central (Apartir do ROL) "))
    print("x  = {:.2f}".format(x))
    print("Me = {:.2f}".format(Me))
    print("Mo = {}".format(Mo))

    # Quartis
    Q1 = 0
    Q2 = Me
    Q3 = 0

    # Index de cada quartil
    Q1i = ((n + 1) / 4) - 1
    Q3i = (3 * ((n + 1) / 4)) - 1

    Q1ii = int(Q1i)
    Q3ii = int(Q3i)
    
    if (Q1i - Q1ii) > 0:
        Q1 = (rol[Q1ii] + rol[Q1ii + 1]) / 2
        Q3 = (rol[Q3ii] + rol[Q3ii + 1]) / 2
    else:
        Q1 = rol[Q1ii]
        Q3 = rol[Q3ii]

    print("Q1: {:.2f}".format(Q1))
    print("Q2: {:.2f}".format(Q2))
    print("Q3: {:.2f}".format(Q3))

    ## Variancia / Desvio Padrão
    sum_var = 0
    for i in rol:
        sum_var += math.pow(i - x, 2)

    variancia = sum_var / n
    dp = math.sqrt(variancia)

    print("Variância: {:.2f}".format(variancia))
    print("Desvio Padrão: {:.2f}".format(dp))