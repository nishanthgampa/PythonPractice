line = 'My name is nishanth gampa and I work as a Data Analyst at All Star Directories and I love my company'
dict = {}


for i in line:
	dict.setdefault(i,0)
	dict[i] = dict[i]+1


print(dict)
