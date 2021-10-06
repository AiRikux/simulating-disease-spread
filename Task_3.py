from Task_2 import *
from matplotlib import pyplot


def visual_curve(days, meeting_probability, patient_zero_health):
	y = run_simulation(days, meeting_probability, patient_zero_health)
	print(y)
	pyplot.plot(range(1, days + 1), y)
	# automatically generate graph
	pyplot.show()


if __name__ == '__main__':
	visual_curve(90, 0.18, 40)

# my result match the prediction although with meeting_probability = 1 and patient_zero_health = 1
# isn't as accurate as the sample result, the graph is somewhat a representative of the scenarios
