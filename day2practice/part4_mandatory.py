# part4_mandatory.py
# 必做任务：传感器类继承设计 + JSON 保存读数

import json  # 用于 JSON 文件的读写


# ==================== 1. 定义基类：传感器 ====================
class Sensor:
    """传感器基类，提供通用的属性和方法"""

    def __init__(self, name, unit=""):
        """
        初始化传感器
        :param name: 传感器名称（如 "温度计1号"）
        :param unit: 测量单位（如 "°C"）
        """
        self.name = name          # 传感器名称
        self.unit = unit          # 单位
        self.readings = []        # 用于存储所有读数的列表

    def add_reading(self, value):
        """添加一个读数到列表中"""
        self.readings.append(value)
        print(f"  -> {self.name} 添加读数: {value}{self.unit}")

    def get_average(self):
        """计算所有读数的平均值，若无读数则返回 0"""
        if not self.readings:
            return 0
        return sum(self.readings) / len(self.readings)

    def get_max(self):
        """获取最大值，若无读数则返回 None"""
        return max(self.readings) if self.readings else None

    def get_min(self):
        """获取最小值，若无读数则返回 None"""
        return min(self.readings) if self.readings else None

    def to_dict(self):
        """
        将当前对象的重要数据转换为字典，方便后续转为 JSON
        """
        return {
            "name": self.name,
            "unit": self.unit,
            "readings": self.readings
        }

    def save_to_json(self, filename):
        """
        将当前传感器的读数保存为 JSON 文件
        :param filename: 要保存的文件名（如 "sensor_data.json"）
        """
        with open(filename, 'w', encoding='utf-8') as f:
            # indent=4 让 JSON 格式更美观，ensure_ascii=False 支持中文
            json.dump(self.to_dict(), f, indent=4, ensure_ascii=False)
        print(f"✅ 数据已成功保存到 {filename}")

    @classmethod
    def load_from_json(cls, filename):
        """
        从 JSON 文件中加载数据，并返回一个 Sensor 对象（类方法）
        :param filename: 要读取的 JSON 文件名
        :return: 构造好的 Sensor 对象
        """
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # 根据字典数据创建对象并恢复读数
        sensor = cls(data["name"], data["unit"])
        sensor.readings = data["readings"]
        return sensor

    def __str__(self):
        """友好的字符串显示（供用户查看）"""
        return f"{self.name} (单位: {self.unit})，当前共有 {len(self.readings)} 条读数"

    def __repr__(self):
        """开发调试时的显示"""
        return f"<Sensor {self.name} readings={self.readings}>"


# ==================== 2. 定义子类：温度传感器 ====================
class TemperatureSensor(Sensor):
    """温度传感器，继承自 Sensor"""

    def __init__(self, name, unit="°C"):
        # 调用父类的初始化方法
        super().__init__(name, unit)

    def add_reading(self, value):
        """
        重写添加读数的方法，加入温度范围提醒（-50°C ~ 100°C）
        """
        if value < -50 or value > 100:
            print(f"  ⚠️ 警告：温度值 {value}{self.unit} 超出常规范围，仍会添加")
        # 调用父类的方法完成实际添加
        super().add_reading(value)


# ==================== 3. 定义子类：湿度传感器 ====================
class HumiditySensor(Sensor):
    """湿度传感器，继承自 Sensor"""

    def __init__(self, name, unit="%"):
        super().__init__(name, unit)

    def add_reading(self, value):
        """
        重写添加读数的方法，加入湿度范围校验（0 ~ 100）
        如果超出范围，则拒绝添加
        """
        if value < 0 or value > 100:
            print(f"  ❌ 错误：湿度值 {value}{self.unit} 超出 0~100 范围，拒绝添加")
            return  # 直接返回，不执行父类的添加逻辑
        # 合法值才调用父类添加
        super().add_reading(value)


# ==================== 4. 主程序：演示必做功能 ====================
if __name__ == "__main__":
    print("\n=== 必做部分：传感器类继承与 JSON 存储演示 ===\n")

    # 4.1 创建温度传感器并添加读数
    temp_sensor = TemperatureSensor("实验室温度计")
    temp_sensor.add_reading(23.5)
    temp_sensor.add_reading(24.0)
    temp_sensor.add_reading(22.8)
    temp_sensor.add_reading(25.1)
    temp_sensor.add_reading(150)   # 超出范围，会有警告但依然添加

    # 4.2 创建湿度传感器并添加读数
    hum_sensor = HumiditySensor("温室湿度计")
    hum_sensor.add_reading(65)
    hum_sensor.add_reading(70)
    hum_sensor.add_reading(68)
    hum_sensor.add_reading(-10)    # 非法值，会被拒绝添加
    hum_sensor.add_reading(45)

    # 4.3 打印统计信息
    print("\n--- 温度传感器统计 ---")
    print(temp_sensor)
    print(f"  平均温度: {temp_sensor.get_average():.2f}°C")
    print(f"  最高温度: {temp_sensor.get_max()}°C")
    print(f"  最低温度: {temp_sensor.get_min()}°C")

    print("\n--- 湿度传感器统计 ---")
    print(hum_sensor)
    print(f"  平均湿度: {hum_sensor.get_average():.2f}%")
    print(f"  最高湿度: {hum_sensor.get_max()}%")
    print(f"  最低湿度: {hum_sensor.get_min()}%")

    # 4.4 将温度传感器数据保存为 JSON 文件
    temp_sensor.save_to_json("temperature_data.json")

    # 4.5 从 JSON 文件加载数据，验证是否保存成功
    loaded_sensor = Sensor.load_from_json("temperature_data.json")
    print("\n--- 从 JSON 文件加载的数据 ---")
    print(loaded_sensor)
    print(f"加载后的读数列表: {loaded_sensor.readings}")