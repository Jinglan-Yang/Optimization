from pulp import *

prob=LpProblem("Problem",LpMaximize)

x11=LpVariable("var1",0,1,LpInteger)
x12=LpVariable("var2",0,1,LpInteger)
x21=LpVariable("var3",0,1,LpInteger)
x22=LpVariable("var4",0,1,LpInteger)
x31=LpVariable("var5",0,1,LpInteger)
x32=LpVariable("var6",0,1,LpInteger)
x41=LpVariable("var7",0,1,LpInteger)
x42=LpVariable("var8",0,1,LpInteger)
x51=LpVariable("var9",0,1,LpInteger)
x52=LpVariable("var10",0,1,LpInteger)
x61=LpVariable("var11",0,1,LpInteger)
x62=LpVariable("var12",0,1,LpInteger)
x71=LpVariable("var13",0,1,LpInteger)
x72=LpVariable("var14",0,1,LpInteger)

prob+=2*(x11+x12)+(x21+x22)+3*(x31+x32)+2*(x41+x42)+(x51+x52)+4*(x61+x62)+2*(x71+x72)


prob+=2*x11+0.5*x21+0.5*x31+0.1*x41+0.5*x51+x61+1.5*x71<=3
prob+=2*x12+0.5*x22+0.5*x32+0.1*x42+0.5*x52+x62+1.5*x72<=2
prob+=x11+x12<=1
prob+=x21+x22<=1
prob+=x31+x32<=1
prob+=x41+x42<=1
prob+=x51+x52<=1
prob+=x61+x62<=1
prob+=x71+x72<=1
prob.writeLP("hw9P3.lp")

prob.solve()

print("Status: ", LpStatus[prob.status])
for v in prob.variables():
    print(v.name,'=',v.varValue)