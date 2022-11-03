# 作者：天行健
# 链接：https://www.zhihu.com/question/59170648/answer/2467684802
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import matplotlib.pyplot as plt
from matplotlib.patheffects import withStroke
from matplotlib.collections import LineCollection
import numpy as np
# 设置坐标系为0到180度，半径为10，去掉刻度标签和网格线，量角器的形状就出来了
ax.set_thetamin(0)
ax.set_thetamax(180)
ax.set_rlim(0, 10)
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.grid(False)
# 接下来是画出刻度线，每1度的刻度线最短，每5度的长一点，10度的再长一度，90度的最长。一共是0到180度181根刻度线。极坐标系中坐标是由极角和极径组成，确定一条直线需要两个点，也就是 ，(θ0,ρ0)，(θ1,ρ1)(\theta_0,\rho_0)，(\theta_1,\rho_1)(\theta_0,\rho_0)，(\theta_1,\rho_1) 。比如要画一条45度的从6开始到8的直线。就是要确定两个点(45,6),(45,8)。如下图所示：<img src="https://pica.zhimg.com/50/v2-3cb5f6fbcbdf07e272026a6fca3e13d6_720w.jpg?source=1940ef5c" data-caption="" data-size="normal" data-rawwidth="647" data-rawheight="628" class="origin_image zh-lightbox-thumb" width="647" data-original="https://pic1.zhimg.com/v2-3cb5f6fbcbdf07e272026a6fca3e13d6_r.jpg?source=1940ef5c"/>因为要画的线比较多，用for循环plot来画会比较慢，这里使用LineCollection来画。先用数组创建出线的坐标。再用ax.add_collection方法一次性画出来
scale = np.zeros((181, 2, 2))
scale[:, 0, 0] = np.linspace(0, np.pi, 181)  # 刻度线的角度值
scale[:, 0, 1] = 9.6  # 每度的刻度线起始点r值
scale[::5, 0, 1] = 9.3  # 每5度的刻度线起始点r值
scale[::10, 0, 1] = 2  # 每10度的刻度线起始点r值
scale[::90, 0, 1] = 0  # 90度的刻度线起始点r值
scale[:, 1, 0] = np.linspace(0, np.pi, 181)
scale[:, 1, 1] = 10

line_segments = LineCollection(scale, linewidths=[1, 0.5, 0.5, 0.5, 0.5],
                               color='k', linestyle='solid')
ax.add_collection(line_segments)
# 接下来再画两个半圆和45度刻度线。再加上数字。大功告成。
c = np.linspace(0, np.pi, 500)
ax.plot(c, [7]*c.size, color='k', linewidth=0.5)
ax.plot(c, [2]*c.size, color='k', linewidth=0.5)

ax.plot([0, np.deg2rad(45)], [0, 10],
        color='k', linestyle='--', linewidth=0.5)
ax.plot([0, np.deg2rad(135)], [0, 10],
        color='k', linestyle='--', linewidth=0.5)

text_kw = dict(rotation_mode='anchor',
               va='top', ha='center', color='black', clip_on=False,
               path_effects=[withStroke(linewidth=5, foreground='white')])

for i in range(10, 180, 10):
    theta = np.deg2rad(i)
    if theta == np.pi/2:
        ax.text(theta, 8.7, i, fontsize=18, **text_kw)
        continue
    ax.text(theta, 8.9, i, rotation=i-90, fontsize=12, **text_kw)
    ax.text(theta, 7.9, 180-i, rotation=i-90, fontsize=12, **text_kw)


plt.show()
