import csv


with open('data/iris.csv', newline='') as file:
	context = csv.reader(file, delimiter=' ', quotechar='|')
	
	for row in context:
		line = row[0:1]
		for i in line:
			sep_len = i[4:7]
			sep_wid = i[8:11]
			pet_len = i[12:15]
			pet_wid = i[16:19]
			species = i[20:]

		print(sep_len)
		print(sep_wid)
		print(pet_len)
		print(pet_wid)
		print(species)
		