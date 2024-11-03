cvx_begin
    variable x12
    variable x13
    variable x23
    variable x24
    variable x34
    variable y
    maximize y
    subject to
        x12-x23-x24==0;
        x13+x23-x34==0;
        y-x12-x13==0;
        x34+x24-y==0;
        x12<=8;
        x13<=7;
        x23<=2;
        x24<=4;
        x34<=12;
        x12>=0;
        x13>=0;
        x23>=0;
        x24>=0;
        x34>=0;

cvx_end
x12
x13
x23
x24
x34