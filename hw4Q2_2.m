cvx_begin
    variable x1
    variable x2
    variable x3
    variable x4
    minimize 3*x1+4*x2+8*x3+2*x4
    subject to
        4*x1+6*x2+20*x3+x4>=30;
        7*x1+10*x2+30*x4>=40;
        130*x1+120*x2+150*x3+70*x4>=400;
        x1>=0;
        x2>=0;
        x3>=0;
        x4>=0;
cvx_end

x1
x2
x3
x4