# 导入数值计算库numpy
import numpy as np

# 手写标准Softmax函数
def softmax_np(logits):
    # 数值稳定优化：减去向量最大值，防止exp大数溢出报错
    max_v = np.max(logits)
    exp_z = np.exp(logits - max_v)
    # 归一化，输出总和=1的概率分布
    return exp_z / np.sum(exp_z)

# 手写单样本交叉熵损失函数
# logits：模型原始得分；one_hot_label：独热编码真实标签
def cross_entropy_np(logits, one_hot_label):
    prob = softmax_np(logits)
    # +1e-10极小值，防止概率为0时log(0)产生负无穷
    return -np.sum(one_hot_label * np.log(prob + 1e-10))

# 题目给定输入：3分类原始logits
logits = np.array([2.0, 1.0, 0.1])
# 调用手写Softmax计算概率
soft_prob = softmax_np(logits)
print("Numpy Softmax结果：", soft_prob)

# 真实标签为第0类，对应one-hot编码
label = np.array([1, 0, 0])
# 计算手写交叉熵损失
loss_np = cross_entropy_np(logits, label)
print("Numpy交叉熵损失：", loss_np)