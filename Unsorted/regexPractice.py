import re

isPhoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = isPhoneNumRegex.search("My phone number is 510-378-8864")
print("phone number found: " + mo.group() )


isPhoneNumRegex1 = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo1 = isPhoneNumRegex1.search("Harshini's phone number is 980-248-7185")
print("mo1.group(): " + mo1.group())
print("mo1.group(0): " + mo1.group(0))
print("mo1.group(1): " + mo1.group(1))
print("mo1.group(2): " + mo1.group(2))
print( mo1.groups())
areaCode, mainNumber = mo1.groups()
print("areaCode: " + areaCode)
print("mainNumber: " + mainNumber)

#matching parenthesis in your phone number

isPhoneNumRegex2 = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = isPhoneNumRegex2.search("My phone number is (510) 378-8864")
print("mo2.group(): " + mo2.group())
print("mo2.group(1): " + mo2.group(1))
print("mo2.group(2): " + mo2.group(2))
print(mo2.groups())
areaCode2, mainNumber2 = mo2.groups()
print("areaCode2: " + areaCode2)
print("mainNumber2: " + mainNumber2)


heroRegex = re.compile("Batmann|Tinaa Fey")
mo3 = heroRegex.search("I'm Batman and she is Tina Fey")
print(mo3)
mo3
print("mo3.group(): " + mo3.group())
mo31 = heroRegex.search("I'm Tina Fey and he is Batman")
print("mo31.group(): " + mo31.group())

batRegex = re.compile(r'Bat(man|women|mobile|harshini)')
mo4 = batRegex.search("My girlfriend is Batharshini")
print("mo4.group(): " + mo4.group())
print("mo4.gorup(1): "+ mo4.group(1))
print(mo4.groups())

batRegex1 = re.compile(r'bat(wo)?man')
mo5 = batRegex1.search("Harshini is batwoman")
print("mo5.group(): " + mo5.group())

mo51 = batRegex1.search("Nishu is batman")
print("mo51.group(): " + mo51.group())

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo6 = phoneRegex.search("My phone num is 501-378-8864")
print("mo6.group(): " + mo6.group())
mo61 = phoneRegex.search("Lallu's phone num is 248-7815")
print("mo61.group(): " + mo61.group())

lalluRegex = re.compile(r'(la)*llu')
mo7 = lalluRegex.search("chitti llu is not her name")
print("mo7.group(): " + mo7.group())
mo71 = lalluRegex.search("chitti lallu is her name")
print("mo71.group(): "+mo71.group())
mo72 = lalluRegex.search("chitti lalalalalallu is very cute")
print("mo72.group(): " + mo72.group())

lalluRegex1 = re.compile(r'(la)+llu')
mo8 = lalluRegex1.search("She is chitti lallu")
print("mo8.group(): " + mo8.group())
mo81 = lalluRegex1.search("She is cute chitti lalalalalalallu")
print("mo81.group(): " + mo81.group())
mo82 = lalluRegex1.search("she is not llu")
print(mo82 == None)

haRegex = re.compile(r'(ha){3}')
mo9 = haRegex.search('hahaha')
print("mo9.group(): " + mo9.group())

mo91 = haRegex.search('ha')
print(mo91 == None)

greedyHaRegex = re.compile(r'(ha){3,5}')
mo10 = greedyHaRegex.search("hahahahahaha")
print("mo10.groupo(): " + mo10.group())

nonGreedyRegex = re.compile(r'(ha){3,5}?')
mo11 = nonGreedyRegex.search('hahahahaha')
print("mo11.group(): " + mo11.group())

allPhoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo12 = allPhoneRegex.findall("USA: 510-378-8864 , India: 924-623-4234")
print(mo12)

allPhoneRegex1 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo13 = allPhoneRegex1.findall("USA: 510-378-8864 , India: 924-623-4234")
print(mo13)

ganeshChaturtiRegex = re.compile(r'\d+\s\w+')
mo14 = ganeshChaturtiRegex.findall("11 Coconut, 100 Laddus, 10 Agarbattis, 1 kumkum, 2 deepalu")
print(mo14)

vowelRegex = re.compile(r'[aeiouAEIOU]')
mo15 = vowelRegex.findall('Sambhar and Chicken Fry go together really well')
print(mo15)

consonantRegex = re.compile(r'[^aeiouAEIOU]')
mo16 = consonantRegex.findall('Nishanth need to practice playing football')
print(mo16)

removeSpaceRegex = re.compile(r'^\s*|\s*$')
mo101 = removeSpaceRegex.sub('', '        WTF Bro    ')
mo100 = re.sub(removeSpaceRegex,'', '      WTF Bro      ')
mo100
mo101
print(mo100)
print(mo101)

beginsWithNamesthe = re.compile(r'^Namasthe')
mo17 = beginsWithNamesthe.search("Namasthe uncle ela unnaru?")
print(mo17)

endsWithNum = re.compile(r'\d$')
mo18 = endsWithNum.search("The number od Biryanis Nishanth has ordered for himself is 2")
print(mo18)

onlyNumbers = re.compile(r'^\d+$')
mo19 = onlyNumbers.search(r'1234567890')
print(mo19)

atRegex = re.compile(r'.at')
mo20 = atRegex.findall("The cat sat on the hat that was on a flat mat")
print(mo20)

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo21 = nameRegex.search("First Name: Rangamma Last Name: Mangamma")
print(mo21.group())
print(mo21.group(1))
print(mo21.group(2))

nonGreedyRegex1 = re.compile(r'<.*?>')
mo22 = nonGreedyRegex1.search("<Whats up brother?> NM, I'm doing Okay>")
print(mo22.group())

greedyRegex1 = re.compile(r'<.*>')
mo23 = greedyRegex1.search("<Whats up brother?> NM, I'm doing Okay>")
print(mo23.group())


noNewLineRegex = re.compile(r'.*')
mo24 = noNewLineRegex.search("eat biryani \n pay bill \n repeat it everyday")
print(mo24.group())

newLineRegex = re.compile(r'.*', re.DOTALL)
mo25 = newLineRegex.search("eat biryani \n pay bill \n repeat it everyday")
print(mo25.group())

biryaniRegex = re.compile(r'biryani', re.I)
mo26 = biryaniRegex.search('BIRYANI')
print(mo26.group())
mo27 = biryaniRegex.search("BiRyAnI is lOvE")
print(mo27.group())

onlyChickenBiryani = re.compile(r'\w+ Biryani')
mo28 = onlyChickenBiryani.sub('Chicken Biryani',"Anna, one veg Biryani and paneer Biryani")
print(mo28)
































