# part4_challenge.py
# 挑战任务：读取 CSV 文件（10行传感器数据），计算统计值并绘图
# 备注：这个文件会导入上面 "part4_mandatory.py" 中定义的传感器类，实现前后综合

import csv          # 用于读写 CSV 文件
import matplotlib.pyplot as plt  # 用于绘图（ pip install matplotlib）

from part4_mandatory import TemperatureSensor, HumiditySensor


# ==================== 1. 生成示例 CSV 数据 ====================
def generate_sample_csv(filename="sensor_readings.csv"):
    """
    自己编造 10 行传感器数据（时间、温度、湿度），并写入 CSV 文件
    """
    # 模拟数据：时间从 08:00 到 17:00，每小时一条
    sample_data = [
        ["时间", "温度(°C)", "湿度(%)"],
        ["08:00", 22.0, 60],
        ["09:00", 23.5, 65],
        ["10:00", 24.0, 68],
        ["11:00", 25.2, 70],
        ["12:00", 26.1, 72],
        ["13:00", 27.0, 75],
        ["14:00", 26.5, 73],
        ["15:00", 25.8, 70],
        ["16:00", 24.7, 68],
        ["17:00", 23.9, 65]
    ]

    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(sample_data)
    print(f"✅ 已生成示例 CSV 文件: {filename}")


# ==================== 2. 主程序：读取 CSV，统计并绘图 ====================
if __name__ == "__main__":
    print("\n=== 挑战部分：读取 CSV 数据，统计并绘图 ===\n")

    # 2.1 生成 CSV 文件（如果已有可跳过，这里确保有数据）
    generate_sample_csv("sensor_readings.csv")

    # 2.2 读取 CSV 文件中的数据
    times = []      # 存放时间
    temps = []      # 存放温度
    hums = []       # 存放湿度

    with open("sensor_readings.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        header = next(reader)   # 跳过表头行（第一行）
        print(f"CSV 表头: {header}")

        for row in reader:
            times.append(row[0])           # 第一列：时间
            temps.append(float(row[1]))    # 第二列：温度，转为浮点数
            hums.append(float(row[2]))     # 第三列：湿度，转为浮点数

    print(f"共读取 {len(times)} 条数据")

    # 2.3 【亮点】利用必做部分定义的传感器类来处理数据
    # 创建温度传感器和湿度传感器对象，将 CSV 数据添加进去
    temp_sensor = TemperatureSensor("CSV温度计")
    hum_sensor = HumiditySensor("CSV湿度计")

    for t, h in zip(temps, hums):
        temp_sensor.add_reading(t)
        hum_sensor.add_reading(h)

    # 2.4 使用传感器对象的方法计算统计值
    temp_avg = temp_sensor.get_average()
    temp_max = temp_sensor.get_max()
    temp_min = temp_sensor.get_min()

    hum_avg = hum_sensor.get_average()
    hum_max = hum_sensor.get_max()
    hum_min = hum_sensor.get_min()

    print("\n--- 温度统计（使用传感器类计算） ---")
    print(f"  平均值: {temp_avg:.2f}°C")
    print(f"  最大值: {temp_max}°C")
    print(f"  最小值: {temp_min}°C")

    print("\n--- 湿度统计（使用传感器类计算） ---")
    print(f"  平均值: {hum_avg:.2f}%")
    print(f"  最大值: {hum_max}%")
    print(f"  最小值: {hum_min}%")

    # 2.5 使用 Matplotlib 绘制折线图
    plt.figure(figsize=(10, 5))  # 设置画布大小

    # 绘制温度曲线（红色圆点标记）
    plt.plot(times, temps, marker='o', label='温度 (°C)', color='red', linewidth=2)
    # 绘制湿度曲线（蓝色方块标记）
    plt.plot(times, hums, marker='s', label='湿度 (%)', color='blue', linewidth=2)

    # 添加标题和标签
    plt.title("传感器读数变化趋势", fontsize=14)
    plt.xlabel("时间", fontsize=12)
    plt.ylabel("数值", fontsize=12)

    # 让 X 轴标签倾斜 45 度，避免重叠
    plt.xticks(rotation=45)
    # 显示图例
    plt.legend()
    # 显示网格（虚线，半透明）
    plt.grid(True, linestyle='--', alpha=0.6)

    # 自动调整布局，防止标签被裁剪
    plt.tight_layout()

    # 显示图表（运行后会自动弹出窗口）
    plt.show()

    # （可选）将图表保存为图片文件
    # plt.savefig("sensor_plot.png")
    # print("📊 图表已保存为 sensor_plot.png")