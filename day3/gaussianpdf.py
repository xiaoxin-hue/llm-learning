# 导入数值计算库与绘图库
import numpy as np
import matplotlib.pyplot as plt
import math

def gaussian_pdf(x, mu, sigma):
    """
    计算正态分布概率密度函数PDF
    :param x: 输入自变量数组
    :param mu: 正态分布均值
    :param sigma: 正态分布标准差
    :return: 对应x位置的概率密度值
    """
    # PDF公式第一部分系数 1/(σ√2π)
    term1 = 1 / (sigma * math.sqrt(2 * math.pi))
    # PDF指数部分 exp(-(x-μ)² / 2σ²)
    term2 = np.exp(- (x - mu)**2 / (2 * sigma**2))
    # 两部分相乘得到概率密度
    return term1 * term2

# 生成x轴采样点，范围-10~10，共1000个点，保证曲线平滑
x = np.linspace(-10, 10, 1000)
# 三组不同参数的正态分布用于对比
y1 = gaussian_pdf(x, mu=0, sigma=1)   # 标准正态分布
y2 = gaussian_pdf(x, mu=0, sigma=2)   # 均值相同，标准差更大，曲线更宽
y3 = gaussian_pdf(x, mu=3, sigma=1)   # 标准差相同，均值右移，曲线整体右移

# 创建画布，设置尺寸
plt.figure(figsize=(8,4))
# 绘制三条分布曲线并添加图例标签
plt.plot(x, y1, label="μ=0,σ=1")
plt.plot(x, y2, label="μ=0,σ=2")
plt.plot(x, y3, label="μ=3,σ=1")
# 坐标轴标签
plt.xlabel("x")
plt.ylabel("概率密度 f(x)")
# 图表标题
plt.title("高斯分布PDF曲线")
# 显示图例
plt.legend()
# 显示浅灰色网格，方便读数
plt.grid(alpha=0.3)
# 弹出绘图窗口展示图像
plt.show()