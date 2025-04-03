import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.sans-serif": 'SimHei',   # 防止中文乱码
    "axes.unicode_minus": False    # 修复负号显示
})

def plot_CashFlow_Arrow(cf, distance=None, arrow_color='black', ax=None):
    """绘制现金流箭头图"""
    cf = np.array(cf).flatten()
    if distance is None:
        distance = cf.max() / len(cf)
    
    for i in range(len(cf)):
        if cf[i] == 0:  # 跳过零值现金流
            continue
        ax.arrow(
            i, 0, 0, cf[i],
            fc=arrow_color, ec=arrow_color,
            head_width=0.15,
            head_length=distance,
            length_includes_head=True
        )
        # 添加金额标注
        va = 'bottom' if cf[i] > 0 else 'top'
        ax.text(i + 0.1, cf[i] + (distance if cf[i] > 0 else -distance),
                f"{abs(cf[i])}万元",
                va=va, ha='left')

def set_ax_FlowChart_form(ax, years):
    """设置现金流量图坐标系格式"""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_position(('data', 0))
    
    # 设置x轴刻度
    ax.xaxis.set_major_locator(plt.MultipleLocator(1))
    ax.set_xlim(-0.5, years + 0.5)
    ax.set_ylim(-1.2, 1.2)
    
    # 添加时间标签
    for i in range(years+1):
        ax.text(i, -0.15, f"第{i}年", ha='center')
    
    # 绘制时间轴箭头
    ax.arrow(-0.5, 0, years+1, 0, 
             head_width=0.1, head_length=0.2, 
             fc='black', ec='black')
    return ax

# 生成现金流数据：每年末存入1万元，持续8年
cash_flow = [0]  # 第0年（现在）没有现金流
for _ in range(8):
    cash_flow.append(-1)  # 每年末现金流出1万元

# 创建画布
fig, ax = plt.subplots(figsize=(10, 4))
set_ax_FlowChart_form(ax, years=8)
plot_CashFlow_Arrow(cash_flow, distance=0.2, ax=ax)

# 添加图表标注
plt.title("定期存款现金流量图（每年末存入1万元，持续8年）", pad=20)
plt.ylabel("现金流方向")
plt.tight_layout()
plt.show()