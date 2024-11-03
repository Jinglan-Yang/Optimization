import numpy as np
import matplotlib.pyplot as plt

x1=np.arange(-2.5,0.5,0.1)
x2=np.arange(0,3,0.1)
X1,X2=np.meshgrid(x1,x2)
f = 60-10*X1-4*X2+X1**2+2*X2**2-X1*X2
f = np.exp(1-X1-X2)+np.exp(X1+X2-1)+X1**2+X1*X2+X2**2+X1-3*X2
plt.contour(x1,x2,f,20) 


def func_2d(x):

    return np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+x[0]**2+x[0]*x[1]+x[1]**2+x[0]-3*x[1]

def jacobian(x):
    return np.array([-np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+2*x[0]+x[1]+1,
    -np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+x[0]+2*x[1]-3])

def hessian(x):
    return np.array([[np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+2,np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+1],
    [np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+1,np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+2]])

def armijo(f,gk,dk,x0,t,gamma,beta):
    while f(x0+t*dk)>f(x0)+gamma*t*np.dot(gk(x0),dk):
        t=beta*t
    alpha=t
    return alpha

def newton(f,g,H,x0):
    # f is f(x) we are optimizing
    # g is the gradient of f
    # H is the Hessian if f
    W=np.zeros((2,10**2))
    i = 1
    W[:,0] = x0
    k=0
    while np.linalg.norm(g(x0))>1e-5:
        dk=-np.dot(np.linalg.inv(H(x0)),g(x0))
        alpha=armijo(f,g,dk,x0,t=1,gamma=0.5,beta=0.5)
        x0=x0+alpha*dk
        W[:,i] = x0
        i+=1
        k+=1
        print('第',k,'次迭代结果:')
        print(x0,f(x0),'\n')

    W=W[:,0:i] 
    return W

x = np.array([0,0])

W=newton(func_2d,jacobian,hessian,x0=x)
plt.plot(W[0,:],W[1,:],'g*',W[0,:],W[1,:]) # 画出迭代点收敛的轨迹
plt.show()

