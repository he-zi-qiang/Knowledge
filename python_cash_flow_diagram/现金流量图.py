' 导入相应的库 '
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams.update( {
        "font.sans-serif":'SimHei',  # 防止中文乱码
        "axes.unicode_minus":False,  # 中文负号显示
    } )


def plot_CashFlow_Arrow( 
        cf, # CashFlow，一段现金流
        distance = None, # 图表离散尺度
        arrow_color = 'black', # 箭头颜色
        ax = None # 绘图的坐标系
        ):
    cf = np.array(cf).flatten()
    if distance == None : # 如果图表元素离散尺度未给定
        distance = cf.max() / len(cf) # 就取现金流最大值除以总年份为尺度
    for i in range( 0, len(cf) ):
        ax.arrow(
            i, 0, 0, (cf[i]), 
            fc = arrow_color, ec = arrow_color, 
            length_includes_head = True,
            head_width = 0.1, 
            head_length = distance, 
            overhang = 0.5
        )
        if cf[i] > 0:
            ax.text(
                i + len(cf)*0.01, 
                cf[i] + distance, 
                str( round(cf[i], 2) )
            )
        elif cf[i] < 0:
            ax.text(
                i + len(cf)*0.01, 
                cf[i] - distance,
                str( round(cf[i], 2) )
            )            
    return ax


def set_ax_FlowChart_form( 
        ax, 
        length, 
        distance = None, 
        axis_color = "black" 
        ):
    if distance == None : # 如果图表元素离散尺度未给定
        distance = 10 * length # 就取 10 倍年份为 distance
    # 设置四个坐标轴不可见
    ax.spines['top'].set_visible(False) # 设置坐标轴,下同
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # 把 X 轴及其数据标签挪到图表当中
    ax.spines['bottom'].set_position(('data',0))
    plt.setp( ax.xaxis.get_majorticklabels(), ha="left" ) 
    # left 表示 X 坐标数据标签向左对齐
    # 否则箭头会挡住数字
    plt.arrow( # 中央 x 轴箭头
        -0.1, 0, length + 1.2, 0, 
        fc = axis_color, 
        ec = axis_color, 
        shape ="full", 
        head_width = distance*0.5, head_length=0.3, overhang=0.5)

    # 隐藏 y 坐标
    plt.yticks([])

    # 设置 X 轴的刻度为1
    x_major_locator = plt.MultipleLocator(1)    
    # 把x轴的刻度间隔设置为1，并存在变量里
    ax.xaxis.set_major_locator(x_major_locator) 
    # 把x轴的主刻度设置为1的倍数

    # 设置图表 X Y 范围，防止绘图区太大或太小
    # 0.1, 1.4 和 15 都是反复试出来的
    # 因为这样效果好，没什么原因
    ax.set_xlim(-0.1, length + 1.4)
    ax.set_ylim(-15 * distance, 15 * distance)
    return 

distance=2.5
# 用列表保存现金流量的值
A = []
A.append(-30)
for i in range(0, 7):
	A.append(10)
A


fig, ax = plt.subplots()
ax = set_ax_FlowChart_form( ax, len(A), distance = distance )
plot_CashFlow_Arrow( cf = A, distance = distance, ax = ax )
# 画出水平线
x = np.arange(1,8)
y = 0*x + 10
plt.plot(x, y, c='r', ls='--') 
plt.title("等额序列现金流量图")
plt.ylabel("资金（万元）")

Text(0, 0.5, '资金（万元）')


