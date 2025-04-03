import sys
import numpy as np
import matplotlib.pyplot as plt

print("Python 路径:", sys.executable)
print("numpy 版本:", np.__version__)
print("matplotlib 版本:", plt.__version__)

# 测试绘图
plt.plot([1, 2, 3], [4, 5, 6])
plt.show()