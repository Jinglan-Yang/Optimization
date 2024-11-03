import numpy as np
import matplotlib.pyplot as plt

x1=np.arange(-2.5,1,0.1)
x2=np.arange(0,3.5,0.1)
X1,X2=np.meshgrid(x1,x2)

f = np.exp(1-X1-X2)+np.exp(X1+X2-1)+X1**2+X1*X2+X2**2+X1-3*X2
plt.contour(x1,x2,f,50) 

def func_2d(x):
    """
    目标函数
    :param x: 自变量，二维向量
    :return: 因变量，标量
    """
    return np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+x[0]**2+x[0]*x[1]+x[1]**2+x[0]-3*x[1]


def grad_2d(x):
    """
    目标函数的梯度
    :param x: 自变量，二维向量
    :return: 因变量，二维向量
    """
    deriv0 = -np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+2*x[0]+x[1]+1
    deriv1 = -np.exp(1-x[0]-x[1])+np.exp(x[0]+x[1]-1)+x[0]+2*x[1]-3
    return np.array([deriv0, deriv1])

def armijo(f,df, x, d, gamma=0.5):
    '''
    Armijo非精确线搜索求最小值
    返回搜索步长
    f: 需要求最小值的函数
    x: x_0
    d: 搜索方向
    sigma: armijo准则中的参数
    '''
    alpha, t,beta, k=0.1, 1, 0.5,0
    while f(x+t*d)>f(x)+t*gamma*df(x).dot(d) and k<200:
        t*= beta
        k += 1
    alpha=t
    return alpha

def steepest_descent(f,df, x):
    '''
    最速下降法求最小值
    其中利用黄金分割法求步长
    f: 需要求最小值的函数
    df: 函数的导数
    x: 初始点
    '''
    i=1
    k = 0
    W=np.zeros((2,10**3))
    W[:,0] = x
    result=[]
    while np.linalg.norm(df(x))>1e-5 and k<1000:
        d = -df(x)
        alpha = armijo(f, df, x, d, gamma=0.5)    # armijo非精确搜索求步长
        x = x + alpha*d
        W[:,i] = x
        k += 1
        i+=1
    W=W[:,0:i]
    return [x,f(x),k],W      # 返回最小值点，函数最小值，迭代次数

result2 = steepest_descent(func_2d,grad_2d,np.array([0, 0]))[0]
print(result2)

x0 = np.array([0,0])
W = steepest_descent(func_2d,grad_2d,np.array([0, 0]))[1]
    
plt.plot(W[0,:],W[1,:],'g*',W[0,:],W[1,:]) # 画出迭代点收敛的轨迹
plt.show()