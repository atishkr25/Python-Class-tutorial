import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(0, 3 * np.pi, 0.1)
# print(x)

# y = np.sin(x)
# print(y)

# plt.plot(x, y)
# plt.xlabel('x values (radians)')
# plt.ylabel('sin(x)')
# plt.title('Sine Wave')
# plt.show()



# import random
# num_rand_data_points=7
# plt.figure(figsize=(10,5),facecolor='w',edgecolor='k')
# x_vals=[random.randrange(1,50,1) for i in range(num_rand_data_points)]
# plt.plot(x_vals,label="random data")
# plt.ylabel('the y-axis label')
# plt.xlabel('the x-axis label')
# plt.title("{} random data points".format(num_rand_data_points))
# plt.legend()
# plt.show()


# (x1_vals,y1_vals)=([1,2,3,4],[1,4,9,16])
# (x2_vals,y2_vals)=([0,1,1.5,7],[1,4,12,16])
# (x3_vals,y3_vals)=([0,1,3,5],[3,4.5,7,18])
# plt.figure(figsize=(5,3))
# plt.plot(x1_vals,y1_vals,label="pair1",color="green",marker="o")
# plt.plot(x2_vals,y2_vals,label="pair2",color="red",marker="*")
# plt.plot(x3_vals,y3_vals,label="pair3",color="cyan",marker="^")
# plt.xlabel("x-axis title")
# plt.ylabel("y-axis title")
# plt.title("main title")
# plt.legend()
# plt.show()

x= np.arange(0,3 * np.pi,0.1)
y_sin=np.sin(x)
y_cos=np.cos(x)
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.xlabel('x axis label')
plt.xlabel('y axis label')
plt.title('sine and cosine')
plt.legend(['sine','cosine'])
plt.show()
