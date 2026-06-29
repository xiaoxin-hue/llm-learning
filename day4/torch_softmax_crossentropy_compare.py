# 导入numpy用于数值对比，torch调用官方深度学习接口
import numpy as np
import torch

# 1. Numpy手动实现标准Softmax
def softmax_np(logits):
    # 数值稳定优化，避免指数运算溢出
    max_v = np.max(logits)
    exp_z = np.exp(logits - max_v)
    return exp_z / np.sum(exp_z)

# 2. Numpy手动实现单样本交叉熵损失
def cross_entropy_np(logits, one_hot_label):
    prob = softmax_np(logits)
    # 极小偏移防止log(0)报错
    return -np.sum(one_hot_label * np.log(prob + 1e-10))

# 给定3分类logits，运行手写实现
logits = np.array([2.0, 1.0, 0.1])
soft_prob = softmax_np(logits)
print("Numpy Softmax结果：", soft_prob)

# 真实标签one-hot编码
label = np.array([1, 0, 0])
loss_np = cross_entropy_np(logits, label)
print("Numpy交叉熵损失：", loss_np)

# ---------------------- PyTorch官方接口对比模块 ----------------------
# 将numpy数组转换为torch张量
logits_torch = torch.tensor([2.0, 1.0, 0.1])
# Torch交叉熵不需要独热编码，直接传入类别索引 0=第一类
label_torch = torch.tensor([0])

# torch内置Softmax计算概率，dim=0按第一维归一化
soft_torch = torch.softmax(logits_torch, dim=0)
# detach脱离计算图，转为numpy数组打印
print("\nPyTorch Softmax结果：", soft_torch.detach().numpy())

# torch内置交叉熵：内部自带Softmax，直接输入原始logits
# unsqueeze(0)扩充batch维度，匹配函数输入格式
loss_torch = torch.nn.functional.cross_entropy(logits_torch.unsqueeze(0), label_torch)
print("PyTorch交叉熵损失：", loss_torch.item())

# 计算两组Softmax结果最大差值，验证精度误差小于1e-6
diff = np.max(np.abs(soft_prob - soft_torch.detach().numpy()))
print(f"\nNumpy与Torch Softmax最大误差：{diff:.10f}")