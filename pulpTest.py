"""try it.

https://qiita.com/SaitoTsutomu/items/070ca9cb37c6b2b492f0
"""
import numpy as np
import pandas as pd
from itertools import product
import pulp

m = pulp.LpProblem(sense=pulp.LpMaximize)
x = pulp.LpVariable('x', lowBound=0)
y = pulp.LpVariable('y', lowBound=0)

m += 100 * x + 100 * y

m += x + 2 * y <= 16
m += 3 * x + y <= 18
m.solve()
print(pulp.value(x), pulp.value(y))


# next code
np.random.seed(1)
nw, nf = 3, 4
pr = list(product(range(nw), range(nf)))
print(pr)

supply = np.random.randint(30, 50, nw)
demand = np.random.randint(20, 40, nf)
cost = np.random.randint(10, 20, (nw, nf))

# not use pandas

m1 = pulp.LpProblem()
v1 = {(i, j): pulp.LpVariable('v%d_%d' % (i, j), lowBound=0) for i, j in pr}
m1 += pulp.lpSum(cost[i][j] * v1[i, j] for i, j in pr)
for i in range(nw):
    m1 += pulp.lpSum(v1[i, j] for j in range(nf)) <= supply[i]
for j in range(nf):
    m1 += pulp.lpSum(v1[i, j] for i in range(nw)) >= demand[j]
m1.solve()
print({k: pulp.value(x) for k, x in v1.items() if pulp.value(x) > 0})

# use pandas

a = pd.DataFrame([(i, j) for i, j in pr], columns=['warehouse', "factory"])
a['cost'] = cost.flatten()
print(a)

m2 = pulp.LpProblem()
a['Var'] = [pulp.LpVariable('v%d' % i, lowBound=0) for i in a.index]
m2 += pulp.lpDot(a.cost, a.Var)
for k, v in a.groupby('warehouse'):
    m2 += pulp.lpSum(v.Var) <= supply[k]
for k, v in a.groupby('factory'):
    m2 += pulp.lpSum(v.Var) >= demand[k]
m2.solve()
a['Val'] = a.Var.apply(pulp.value)
a[a.Val > 0]
print(a)
