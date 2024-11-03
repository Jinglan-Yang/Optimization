cvx_begin
variable x(7,2)
maximize 2*sum(x(1,:))+sum(x(2,:))+3*sum(x(3,:))+2*sum(x(4,:))+sum(x(5,:))+4*sum(x(6,:))+2*sum(x(7,:))
subject to
    2*x(1,1)+0.5*x(2,1)+0.5*x(3,1)+0.1*x(4,1)+0.5*x(5,1)+x(6,1)+1.5*x(7,1)<=3;
    2*x(1,2)+0.5*x(2,2)+0.5*x(3,2)+0.1*x(4,2)+0.5*x(5,2)+x(6,2)+1.5*x(7,2)<=2;
    for i=1:7
        x(i,1)+x(i,2)<=1;
    end
    x>=0;
    x<=1;
cvx_end
x