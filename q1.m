cvx_begin
variables x y
maximize 2*x+y
subject to
    -3*x+2*y<=5;
    -x-2*y<=-2;
    5*x+2*y<=17;
cvx_end
x,y

cvx_begin
variables x1 y1
maximize 2*x1+y1
subject to
    -3*x1+2*y1<=5;
    -x1-2*y1<=-2;
    5*x1+2*y1<=17;
    x1<=1;
cvx_end
x1,y1

cvx_begin
variables x2 y2
maximize 2*x2+y2
subject to
    -3*x2+2*y2<=5;
    -x2-2*y2<=-2;
    5*x2+2*y2<=17;
    x2>=2;
cvx_end
x2,y2

cvx_begin
variables x3 y3
maximize 2*x3+y3
subject to
    -3*x3+2*y3<=5;
    -x3-2*y3<=-2;
    5*x3+2*y3<=17;
    x3>=2;
    y3<=3;
cvx_end
x3,y3

cvx_begin
variables x4 y4
maximize 2*x4+y4
subject to
    -3*x4+2*y4<=5;
    -x4-2*y4<=-2;
    5*x4+2*y4<=17;
    x4>=2;
    y4>=4;
cvx_end
x4,y4

cvx_begin
variables x5 y5
maximize 2*x5+y5
subject to
    -3*x5+2*y5<=5;
    -x5-2*y5<=-2;
    5*x5+2*y5<=17;
    x5<=2;
    y5<=3;
cvx_end
x5,y5


cvx_begin
variables x6 y6
maximize 2*x6+y6
subject to
    -3*x6+2*y6<=5;
    -x6-2*y6<=-2;
    5*x6+2*y6<=17;
    x6>=3;
    y6<=3;
cvx_end
x6,y6


