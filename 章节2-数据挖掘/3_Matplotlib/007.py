#plt.plot(x, y) 当有两个以上参数时，按照x轴和y轴顺序绘制数据点
import matplotlib.pyplot as plt
print(plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2]))
plt.ylabel("Grade")
plt.axis([-1, 10, 0, 6])
plt.show()