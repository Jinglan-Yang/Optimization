cvx_begin
    variable y1
    variable y2
    variable y3
    variable y4
    maximize 30*y1+40*y2+400*y3
    subject to 
        4*y1+7*y2+130*y3<=3;
        6*y1+10*y2+120*y3<=4;
        20*y1+150*y3<=8;
        y1+30*y2+70*y3<=2;
        y1>=0;
        y2>=0;
        y3>=0;
        y4>=0;

cvx_end
y1
y2
y3
y4

