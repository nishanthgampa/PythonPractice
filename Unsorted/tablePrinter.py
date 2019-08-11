tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
			 ['dogs', 'cats', 'moose', 'goose']]

colWidth = 0


for i in tableData:
	for k in i:
		if len(k) > colWidth:
			colWidth = len(k)

