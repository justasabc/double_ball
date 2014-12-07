import numpy as np
import matplotlib.pyplot as plt

class Plot:
	
	def x_y_list(self,x,y,color,xlabel,ylabel):
		plt.xlabel(xlabel)
		plt.ylabel(ylabel)
		plt.plot(x,y,color)
		#plt.axis([0, 6, 0, 20])
		plt.show()

def case1():
	plot = Plot()
	plot.x_y_list([1,2,3,4],[1,4,9,16],'ro',"x","y")

def case2():
	# evenly sampled time at 200ms intervals
	t = np.arange(0., 5., 0.2)
	# red dashes, blue squares and green triangles
	plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
	plt.show()

def main():
	case2()

if __name__ == "__main__":
	main()
