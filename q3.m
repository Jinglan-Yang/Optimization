W=input("Input an n*n matrix W(n>2): ");
[n,m]=size(W);
cvx_begin
    variable X(n,n);
    minimize sum(sum(W.*X));
    subject to
        sum(X(1,:))-sum(X(:,1))==1;
        sum(X(:,n))-sum(X(n,:))==1;
        for i=2:n-1
            sum(X(i,:))-sum(X(:,i))==0;
        end
        for i=1:n
            for j=1:n
                X(i,j)<=1;
                X(i,j)>=0;
            end
        end
cvx_end

X
