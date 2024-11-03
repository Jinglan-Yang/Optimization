cvx_begin
variable x(5)
maximize 2*x(1)+x(2)+3*x(3)+2*x(4)+2*x(5)
subject to
    x(1)+x(3)<=1;
    x(1)+x(4)+x(5)<=2;
    x(2)+x(3)+x(4)<=3;
    x>=0;
    x<=1;
cvx_end
x