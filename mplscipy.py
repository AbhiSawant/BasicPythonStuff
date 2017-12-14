import numpy as np
import matplotlib.pyplot as plt

# fig = plt.figure(figsize=plt.figaspect(2.0))
# fig = plt.figure()
# ax = fig.add_subplot(111)
# # ax2 = fig.add_subplot(212)
# # ax.set(xlim=[0, 1.5], ylim=[0, 1.5], title="My Graph", xlabel="X-Axis", ylabel="Y-Axis")
# # OR

# ax.set_xlim([0, 5])
# ax.set_ylim([0,10])
# ax.set_title("My Graph")
# ax.set_xlabel("X-Axis", color='Blue')
# ax.set_ylabel("Y-Axis", color='Blue')
# ax.plot([1, 2 ,3 ,4], [2, 3, 5 ,8], color="b", linewidth=2)
# ax.scatter([2, 3, 4], [6, 7, 2], color='g', marker='^', alpha=0.5)

# fig, axes = plt.subplots(nrows=2, ncols=2)
# axes[0,0].set(title='Upper left')
# axes[0,1].set(title='Upper right')
# axes[1,0].set(title='Lower left')
# axes[1,1].set(title='Lower right')
# for ax in axes.flat:
#     # Remove all xticks and yticks...
#     ax.set(xticks=[], yticks=[])

# fig, axes = plt.subplots(nrows=3)

# x = np.linspace(0, 10, 100)
# y1, y2, y3 = np.cos(x), np.cos(x + 1), np.cos(x + 2)
# names = ['Signal 1', 'Signal 2', 'Signal 3']
# # axes[0].plot(x,y1)
# for ax, y, name in zip(axes, [y1,y2,y3], names):
# 	ax.plot(x, y, color='g')
# 	ax.set(xticks=[], yticks=[], title=name)


np.random.seed(1)
# x = np.arange(5)
# y = np.random.randn(5)

# fig, axes = plt.subplots(ncols=2)
# ver_bars = axes[0].bar(x, y, color='lightblue')
# hor_bars = axes[1].barh(x, y, color='lightblue')
# axes[0].axhline(0, color='grey', linewidth=2)
# axes[1].axvline(0, color='grey', linewidth=2)

fig, axes = plt.subplots()
# ver_bars = axes.bar(x, y, color='lightblue') 
# for bar in ver_bars:
# 	if bar.xy[1] < 0:
# 		bar.set(edgecolor='darkred', color='salmon')
# axes.axhline(0, color='grey')

# y = np.random.randn(100).cumsum()
# x = np.linspace(0, 10, 100)
# y1 = 2 * x + 1
# y2 = 3 * x + 1.2
# y_mean = 0.5 * x * np.cos(2*x) + 2.5 * x + 1.1

# axes.fill_between(x, y1, y2, color='yellow')
# axes.plot(x, y_mean, color='black')
# axes.set_xlim(0, 10)

# Generate data...
# y_raw = np.random.randn(1000).cumsum() + 15
# x_raw = np.linspace(0, 24, y_raw.size)

# # Get averages of every 100 samples...
# x_pos = x_raw.reshape(-1, 100).min(axis=1)
# y_avg = y_raw.reshape(-1, 100).mean(axis=1)
# y_err = y_raw.reshape(-1, 100).ptp(axis=1)

# bar_width = x_pos[1] - x_pos[0]

# # Make a made up future prediction with a fake confidence
# x_pred = np.linspace(0, 30)
# y_max_pred = y_avg[0] + y_err[0] + 2.3 * x_pred
# y_min_pred = y_avg[0] - y_err[0] + 1.2 * x_pred

# # Just so you don't have to guess at the colors...
# barcolor, linecolor, fillcolor = 'wheat', 'salmon', 'lightblue'

# axes.plot(x_raw, y_raw, color='salmon')
# axes.fill_between(x_pred, y_max_pred, y_min_pred, color='lightblue')
# axes.bar(x_pos, y_avg, yerr=y_err, color='wheat', width=bar_width, edgecolor='grey', ecolor='grey')
# axes.set(xlim=[0,30], ylim=[0, 100])



#working with colors and other stuff for controlling graph
# n = np.arange(0.0, 5.0, 0.2)
# plt.plot(n, n, 'b', n, n**2, 'burlywood', n, n**3, '0.75')

# xs, ys = np.mgrid[:4, 9:0:-1]
# markers = [".", "+", ",", "x", "o", "D", "d", "", "8", "s", "p", "*", "|", "_", "h", "H", 0, 4, "<", "3",
#            1, 5, ">", "4", 2, 6, "^", "2", 3, 7, "v", "1", "None", None, " ", ""]
# descripts = ["point", "plus", "pixel", "cross", "circle", "diamond", "thin diamond", "",
#              "octagon", "square", "pentagon", "star", "vertical bar", "horizontal bar", "hexagon 1", "hexagon 2",
#              "tick left", "caret left", "triangle left", "tri left", "tick right", "caret right", "triangle right", "tri right",
#              "tick up", "caret up", "triangle up", "tri up", "tick down", "caret down", "triangle down", "tri down",
#              "Nothing", "Nothing", "Nothing", "Nothing"]
# fig, ax = plt.subplots(1, 1, figsize=(14, 4))
# for x, y, m, d in zip(xs.T.flat, ys.T.flat, markers, descripts):
#     ax.scatter(x, y, marker=m, s=100)
#     ax.text(x + 0.1, y - 0.1, d, size=14)
# ax.set_axis_off()
# plt.show()

# t = np.arange(0.0, 5.0, 0.2)
# plt.plot(t, t, 'd', t, t**2, 'dr', t, t**3, '>')

# t = np.arange(0.0, 5.0, 0.2)
# plt.plot(t, t, '-', t, t**2, '-.', t, t**3, ':') #with .- it will draw a straight line with dots on it

# t = np.arange(0.0, 5.0, 0.1)
# a = np.exp(-t) * np.cos(2*np.pi*t)
# plt.plot(t, a, color='r', linestyle='-', marker='D', mfc='y', mec='g') # or 'r-D'

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.ylim(-2, 2)
plt.show()

plt.show()
