# 导入数值计算库、绘图库
import numpy as np
import matplotlib.pyplot as plt

# 带温度系数τ的Softmax函数
# logits：原始得分；tau：温度参数，控制分布平滑程度
def softmax_tau(logits, tau):
    # 使用温度缩放原始得分
    z = logits / tau
    # 数值稳定处理，防止exp溢出
    exp_z = np.exp(z - np.max(z))
    return exp_z / np.sum(exp_z)

# 固定实验使用的3分类logits
logits_base = np.array([2.0, 1.0, 0.1])
# 多组温度参数用于对比曲线
tau_list = [0.1, 0.5, 1.0, 2.0, 5.0]
# 每条曲线对应不同颜色
colors = ["red", "orange", "green", "blue", "purple"]

# 创建画布，设置画布尺寸
plt.figure(figsize=(8,5))
# 遍历全部温度，分别计算并绘制概率曲线
for idx, tau in enumerate(tau_list):
    prob = softmax_tau(logits_base, tau)
    # 绘制折线，圆点标记点，图例标注当前温度
    plt.plot([0,1,2], prob, marker="o", label=f"τ={tau}", color=colors[idx])

# 修改x轴刻度文字为类别名称
plt.xticks([0,1,2], ["class0", "class1", "class2"])
plt.xlabel("分类类别")
plt.ylabel("预测概率")
plt.title("不同温度τ下Softmax输出分布")
plt.legend()  # 显示图例区分各曲线
plt.grid(alpha=0.3)  # 浅色网格辅助观察数值
plt.show()  # 弹出绘图窗口展示图像