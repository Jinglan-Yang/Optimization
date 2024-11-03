cvx_begin
    variables x(5)
    minimize -x(1)-x(2)+x(5)
    subject to
        (x(1)-x(2))^(2)+(x(3)+2*x(4))^(4)<=5;
        x(1)+2*x(2)+x(3)+2*x(4)<=6;
        x(5)>=x(3);
        x(5)>=x(4);
        x>=0;
cvx_end
x