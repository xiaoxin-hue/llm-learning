def bayes_calc(p_A, p_B_given_A, p_B_given_notA):
    """
    贝叶斯通用计算函数
    :param p_A: 事件A的先验概率
    :param p_B_given_A: A发生时B发生的似然概率 P(B|A)
    :param p_B_given_notA: A不发生时B发生的似然概率 P(B|Ā)
    :return: 后验概率 P(A|B)
    """
    # 计算A不发生的概率
    p_notA = 1 - p_A
    # 全概率公式计算P(B)：B事件整体发生概率
    p_B = p_B_given_A * p_A + p_B_given_notA * p_notA
    # 贝叶斯公式求解后验概率
    p_A_given_B = (p_B_given_A * p_A) / p_B
    return p_A_given_B

# 程序入口，测试IoT设备故障例题
if __name__ == "__main__":
    # 传入例题已知参数
    res = bayes_calc(p_A=0.01, p_B_given_A=0.95, p_B_given_notA=0.05)
    # 保留四位小数打印结果
    print(f"检测器报警后设备真实故障概率：{res:.4f}")