from pulp import *

prob=LpProblem("Problem",LpMaximize)

x=LpVariable("var1",None,None,LpInteger)
y=LpVariable("var2",None,None,LpInteger)

prob+=2*x+y

prob+=-3*x+2*y<=5
prob+=-x-2*y<=-2
prob+=5*x+2*y<=17

prob.writeLP("hw9P1.lp")

prob.solve()

print("Status: ", LpStatus[prob.status])
for v in prob.variables():
    print(v.name,'=',v.varValue)