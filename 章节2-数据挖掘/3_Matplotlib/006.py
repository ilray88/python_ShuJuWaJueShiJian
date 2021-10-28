import matplotlib.pyplot as plt
print(plt.plot([3, 1, 4, 5, 2]))
plt.rcParams['font.sans-serif'] = ['Simsun'] #这两句用来正常显示中文标签
plt.ylabel("成绩")
plt.xlabel("此处")
plt.savefig("test", dpi=600)  # PNG文件
plt.show()