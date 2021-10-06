from Task_1 import *
import random


class Patient(Person):
	def __init__(self, first_name, last_name, health):
		Person.__init__(self, first_name, last_name)
		self.first_name = first_name
		self.last_name = last_name
		self.health = health

	def get_health(self):
		return int(self.health)

	def set_health(self, new_health):
		self.health = new_health

	def is_contagious(self):
		if self.health > 49:
			return False
		elif self.health < 50:
			return True

	def infect(self, viral_load):
		if self.health <= 29:
			self.health -= 0.1 * viral_load
		elif 29 < self.health < 50:
			self.health -= 1 * viral_load
		elif self.health >= 50:
			self.health -= 2 * viral_load

		if self.health > 100:
			self.set_health(100)
		if self.health < 0:
			self.set_health(0)

	def sleep(self):
		self.health += 5
		if self.health > 100:
			self.set_health(100)
		if self.health < 0:
			self.set_health(0)

	def viral_load(self):
		return 5 + (((self.health - 25) ** 2) / 62)


# for naming Patient objects
pno = {}


def run_simulation(days, meeting_probability, patient_zero_health):
	load_patients()
	pno[1].set_health(patient_zero_health)
	for k in id_p.keys():
		if k == 1:
			continue
		else:
			pno[k].set_health(75)
	contagious = []
	for d in range(days):
		sick = 0
		for k in id_p.keys():
			for f in id_f.get(k, 0):
				p_friend = " ".join(f)
				l = (guy.index(p_friend) + 1)
				# virus can spread is they are visited or visiting
				# visitor infect visited
				# https://stackoverflow.com/questions/5886987/true-or-false-output-based-on-a-probability
				# make a random boolean decision
				if random.random() <= meeting_probability:
					if pno[k].is_contagious():
						vlk = pno[k].viral_load()
						pno[l].infect(vlk)
				# visited infect visitor
					if pno[l].is_contagious():
						vld = pno[l].viral_load()
						pno[k].infect(vld)

		# do a is_contagious test again when the day is over
		for k in id_p.keys():
			if pno[k].is_contagious():
				sick += 1
		contagious.append(sick)
		for k in id_p.keys():
			pno[k].sleep()

	return contagious


def load_patients(initial_health=75):
	load_people()
	for k in id_p.keys():
		first_name = no[k].first_name
		last_name = no[k].last_name
		pno[k] = Patient(first_name, last_name, initial_health)
	return pno


if __name__ == '__main__':
	x = run_simulation(30, 1, 1)
