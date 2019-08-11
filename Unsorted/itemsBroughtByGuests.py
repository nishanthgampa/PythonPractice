allGuests = {
	'Nishanth': {'Chicken Biryani': 2, 'Chicken Manchuria': 3},
	'Harshini': {'Palak Paneer': 2, 'Masala Dosa': 4},
	'Anukrati': {'Aloo Sabzi': 3, 'Okra' : 2}
}

def itemsBrought(guests, item):
	numBrought = 0
	for k, v in guests.items():
		numBrought = numBrought + v.get(item, 0)
	return numBrought


print("The Number of Items being brought")
print(str(itemsBrought(allGuests, 'Chicken Biryani')) + ' Chicken Biryanis')
print(str(itemsBrought(allGuests, 'Chicken Manchuria')) + ' Chicken Manchuria')
print(str(itemsBrought(allGuests, 'Masala Dosa')) + ' Masala Dosa')
print(str(itemsBrought(allGuests, 'Aloo Sabzi')) + ' Aloo Sabzi')
print(str(itemsBrought(allGuests, 'Palak Paneer')) + ' Palak Paneer')
print(str(itemsBrought(allGuests, 'Okra')) + ' Okra')