import numpy as np
import matplotlib.pyplot as plt

x1=np.arange(-2.5,0.5,0.01)
x2=np.arange(0,3,0.01)
X1,X2=np.meshgrid(x1,x2)

f = np.exp(1-X1-X2)+np.exp(X1+X2-1)+X1**2+X1*X2+X2**2+X1-3*X2
plt.contour(x1,x2,f,30) 

def func_2d(x):
    """
    目标函数
    :param x: 自变量，二维向量
    :return: 因变量，标量
    """
    #return - math.exp(-(x[0] ** 2 + x[1] ** 2))
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


def gradient_descent_2d(grad, cur_x=np.array([0, 0]), learning_rate=0.1, precision=0.00001, max_iters=10000):
    """
    二维问题的梯度下降法
    :param grad: 目标函数的梯度
    :param cur_x: 当前 x 值，通过参数可以提供初始值
    :param learning_rate: 学习率，也相当于设置的步长
    :param precision: 设置收敛精度
    :param max_iters: 最大迭代次数
    :return: 局部最小值 x*
    """
    print(f"{cur_x} 作为初始值开始迭代...")
    W=np.zeros((2,10**3))
    W[:,0] = cur_x
    for i in range(max_iters):
        grad_cur = grad(cur_x)
        if np.linalg.norm(grad_cur, ord=2) < precision:
            break  # 当梯度趋近为 0 时，视为收敛
        cur_x = cur_x - grad_cur * learning_rate
        W[:,i+1] = cur_x
        #print(np.linalg.norm(grad_cur, ord=2))
        if func_2d(cur_x)>1e+5: # in case alpha = 1, f diverges.
            print("第", i+1, "次迭代: x 值为 ", cur_x, "目标函数值：",func_2d(cur_x))
            return cur_x, W
        print("第", i+1, "次迭代: x 值为 ", cur_x, "目标函数值：",func_2d(cur_x))

    print("局部最小值 x =", cur_x)
    W=W[:,0:i]
    return cur_x, W

#第 120 次迭代: x 值为  [-1.57128395  2.42870314] 目标函数值： -2.285679688702567
#局部最小值 x = [-1.57128395  2.42870314]

#初始点
x0 = np.array([0,0])
W = gradient_descent_2d(grad_2d, cur_x=np.array([0,0]), learning_rate=1, precision=0.00001, max_iters=10000)[1]
    
plt.plot(W[0,:],W[1,:],'g*',W[0,:],W[1,:]) # 画出迭代点收敛的轨迹
plt.show()
