cvx_begin
    variable z12
    variable z13
    variable z23
    variable z24
    variable z34
    variable y1
    variable y2
    variable y3
    variable y4
    minimize 8*z12+7*z13+2*z23+4*z24+12*z34
    subject to
        z12>=y1-y2;
        z13>=y1-y3;
        z23>=y2-y3;
        z24>=y2-y4;
        z34>=y3-y4;
        y1-y4==1;
        z12>=0;
        z13>=0;
        z23>=0;
        z24>=0;
        z34>=0;
        y1==1;
        y2>=0;
        y3>=0;
        y4==0;

cvx_end
y1
y2
y3
y4