class Person:

	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name
		self.friend_list = []
		persons.append(self)

	def add_friend(self, friend_person):
		a = (guy.index(friend_person) + 1)
		self.friend_list.append(no[a])

	def get_name(self):
		name = "{f} {l}".format(f=self.first_name, l=self.last_name)
		return name

	def get_friends(self):
		return print(self.friend_list)


# for object naming purposes
no = {}
# separate main person to his friends list
friend = []
guy = []
# separate to first_name and last_name
person = []
friends = []
# for storage purposes
id_p = {}
id_f = {}

persons = []

def load_people():
	global id_p, id_f
	imported_names = open("a2_sample_set.txt").read().splitlines()
	# import names and set it up to separate first and last names
	# set up to person, friends list
	for x in imported_names:
		a = x.split(": ")
		guy.append(a[0])
		friend.append(a[1].split(", "))
	# split to first name and last name for person name
	for y in guy:
		person.append(y.split())
	# split to first and last name for person's friends' name
	for z in friend:
		f = []
		for zz in z:
			f.append(zz.split())
		friends.append(f)
	# assign id for object naming
	# id start at 1
	id_p.update(dict(zip(range(1, (1 + len(person))), person)))
	id_f.update(dict(zip(range(1, (1 + len(person))), friends)))
	for k in id_p.keys():
		n = id_p.get(k, 0)
		no[k] = Person(n[0], n[1])
	# end of creating objects for each name

	# start adding friends object to object
	for k in id_p.keys():
		if len(id_f.get(k, 0)) > 0:
			for f in id_f.get(k, 0):
				# https://stackoverflow.com/questions/11959513/python-automatic-object-generation-plus-naming
				# automatic naming objects
				friend_name = " ".join(f)
				no[k].add_friend(friend_name)
		else:
			continue
	return persons


if __name__ == '__main__':
	load_people()
	no[1].add_friend("Alton Justis")
	no[1].get_friends()
	print(persons)