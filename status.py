import csv

dictionary ={}
a = []

#DICTIONARY VERSION
# def hier(row, dictionary, hcc, *drop):
# 	if hcc in row:
# 		b = []
# 		for i in [i for i,z in enumerate(row) if z==hcc]:
# 			pos = i
# 		for x in drop:
# 			if x in row:
# 				if row[0] not in dictionary:
# 					dictionary[row[0]] = list()
# 				dictionary[row[0]].append(hcc)
# 				dictionary[row[0]].append(row[pos+1])
# 				for i in [i for i,z in enumerate(row) if z==x]:
# 					pos2 = i
# 				dictionary[row[0]].append(x)
# 				dictionary[row[0]].append(row[pos2+1])

#LIST VERSION
def hier(row, dictionary, hcc, *drop):
    if hcc in row:
        b = []
        for i in [i for i,z in enumerate(row) if z==hcc]:
            pos = i
        b.append(row[0])
        for x in drop:
            if x in row:
                b.append(hcc)
                b.append(row[pos+1])
                for i in [i for i,z in enumerate(row) if z==x]:
                    pos2 = i
                b.append(x)
                b.append(row[pos2+1])
        a.append(b)

def hier_1(row, dictionary):
    hier(row, dictionary, '3', '4')

def hier_2(row, dictionary):
    if '8' in row:
        hier(row, dictionary, '8', '9', '10', '11', '12', '13')
    elif '9' in row:
        hier(row, dictionary, '9', '10', '11', '12', '13')
    elif '10' in row:
        hier(row, dictionary, '10', '11', '12', '13')
    elif '11' in row:
        hier(row, dictionary, '11', '12', '13')
    elif '12' in row:
        hier(row, dictionary, '12', '13')

def hier_3(row, dictionary):
    if '18' in row:
        hier(row, dictionary, '18', '19', '20', '21', '46', '47')
    elif '19' in row or '46' in row:
        if '19' in row and '46' in row:
            hier(row, dictionary, '19', '20', '21')
            hier(row, dictionary, '46', '47')
        if '19' in row:
            hier(row, dictionary, '19', '20', '21')
        if '46' in row:
            hier(row, dictionary, '46', '47')
    elif '20' in row:
        hier(row, dictionary, '20', '21')

def hier_4(row, dictionary):
    if '34' in row:
        hier(row, dictionary, '34', '35', '36', '37', '38')
    elif '35' in row:
        hier(row, dictionary, '35', '36', '37', '38')
    elif '36' in row:
        hier(row, dictionary, '36', '37')

def hier_5(row, dictionary):
    hier(row, dictionary, '41', '45', '48')
    hier(row, dictionary, '42', '45')
    hier(row, dictionary, '54', '55')
    hier(row, dictionary, '56', '57')
    hier(row, dictionary, '66', '75')
    hier(row, dictionary, '67', '75')
    hier(row, dictionary, '68', '69', '74', '75')
    hier(row, dictionary, '70', '71')
    hier(row, dictionary, '73', '74')
    hier(row, dictionary, '81', '82')
    hier(row, dictionary, '96', '97')

def hier_6(row, dictionary):
    if '87' in row:
        hier(row, dictionary, '87', '88', '89', '90', '102', '103')
    elif '88' in row:
        hier(row, dictionary, '88', '89', '90', '102', '103')
    elif '89' in row:
        hier(row, dictionary, '89', '90', '102', '103')
    elif '102' in row:
        hier(row, dictionary, '102', '90', '103')
    elif '103' in row:
        hier(row, dictionary, '103', '90')

def hier_7(row, dictionary):
    if '106' in row:
        hier(row, dictionary, '106', '107', '108', '109', '110', '150', '151')
    elif '107' in row:
        hier(row, dictionary, '107', '109', '110', '150', '151')
    elif '108' in row:
        hier(row, dictionary, '108', '109', '110', '151')
    elif '109' in row:
        hier(row, dictionary, '109', '110', '151')

def hier_8(row, dictionary):
    hier(row, dictionary, '112', '113')

def hier_9(row, dictionary):
    if '125' in row:
        hier(row, dictionary, '125', '126', '127')
    elif '126' in row:
        hier(row, dictionary, '126', '127')

def hier_10(row, dictionary):
    if '128' in row:
        hier(row, dictionary, '128', '129', '130')
    elif '129' in row:
        hier(row, dictionary, '129', '130')

def hier_11(row, dictionary):
    hier(row, dictionary, '131', '132')

def hier_12(row, dictionary):
    if '137' in row:
        hier(row, dictionary, '137', '138', '139')
    elif '138' in row:
        hier(row, dictionary, '138', '139')

def hier_13(row, dictionary):
    hier(row, dictionary, '145', '146', '149')
    hier(row, dictionary, '150', '151')
    hier(row, dictionary, '153', '217', '254')

def hier_14(row, dictionary):
    if '158' in row:
        hier(row, dictionary, '158', '159', '160', '161', '162')
    elif '159' in row or '162' in row:
        #think this is redundant
        # if '159' in row and '162' in row:
        #     hier(row, dictionary, '159', '160', '161')
        #     hier(row, dictionary, '162', '161')
        if '159' in row:
            hier(row, dictionary, '159', '160', '161')
        elif '162' in row:
            hier(row, dictionary, '162', '161')
    elif '160' in row:
        hier(row, dictionary, '160', '161')

def hier_15(row, dictionary):
    if '183' in row:
        hier(row, dictionary, '183', '184', '187', '188')
    elif '184' in row:
        hier(row, dictionary, '184', '187', '188')
    elif '187' in row:
        hier(row, dictionary, '187', '188')

def hier_16(row, dictionary):
    if '207' in row:
        hier(row, dictionary, '207', '203', '204', '205', '208', '209')
    elif '203' in row or '208' in row:
        if '203' in row and '208' in row:
            hier(row, dictionary, '203', '204', '205')
            hier(row, dictionary, '208', '209')
        elif '203' in row:
            hier(row, dictionary, '203', '204', '205')
        elif '208' in row:
            hier(row, dictionary, '208', '209')
    elif '204' in row:
        hier(row, dictionary, '204', '205')

def hier_17(row, dictionary):
    hier(row, dictionary, '226', '227')

def hier_18(row, dictionary):
    if '242' in row:
        hier(row, dictionary, '242', '243', '244', '245', '246', '247', '248', '249')
    elif '243' in row:
        hier(row, dictionary, '243', '244', '245', '246', '247', '248', '249')
    elif '244' in row:
        hier(row, dictionary, '244', '245', '246', '247', '248', '249')
    elif '245' in row:
        hier(row, dictionary, '245', '246', '247', '248', '249')
    elif '246' in row:
        hier(row, dictionary, '246', '247', '248', '249')
    elif '247' in row:
        hier(row, dictionary, '247', '248', '249')
    elif '248' in row:
        hier(row, dictionary, '248', '249')

def hierarchize(row, dictionary):
    hier_1(row, dictionary)
    hier_2(row, dictionary)
    hier_3(row, dictionary)
    hier_4(row, dictionary)
    hier_5(row, dictionary)
    hier_6(row, dictionary)
    hier_7(row, dictionary)
    hier_8(row, dictionary)
    hier_9(row, dictionary)
    hier_10(row, dictionary)
    hier_11(row, dictionary)
    hier_12(row, dictionary)
    hier_13(row, dictionary)
    hier_14(row, dictionary)
    hier_15(row, dictionary)
    hier_16(row, dictionary)
    hier_17(row, dictionary)
    hier_18(row, dictionary)


with open('one_plus_hcc_valuation.csv', 'rb') as f:
	reader = csv.reader(f)
	for row in reader:
            hierarchize(row, dictionary)

with open('temp_dictionary.csv', 'wb') as g:
	writer =csv.writer(g)
	for row in a:
		writer.writerow(row)

#each row will have the same hcc in the odd column (row[1], row[3])
#if hcc in even column is from 'NEW' then it is automatically no value
# if odd column = NEW and even column = OLD, find all those pairs. These are partials. The value is incremental over next highest.
# if odd column = NEW and even column = NEW, then drop even NEW. if no NEW - OLD combos found, then odd column gets full Value
# if odd column = OLD and even column = OLD ignore
# if odd column = OLD and even column = NEW, mark the even column as a NO_VALUE
c = []

for row in a:
    if len(row) == 5:
        b=[]
        d=[]
        temp = [row[2], row[4]]
        if temp[0] == 'NEW' and temp[1] ==  'NEW':
            b.append(row[0])
            b.append(row[1])
            b.append("FULL VALUE")
            d.append(row[0])
            d.append(row[3])
            d.append("NO VALUE")
            c.append(b)
            c.append(d)
        elif temp[0] == 'NEW' and temp[1] == 'OLD':
            b.append(row[0])
            b.append(row[1])
            b.append("PARTIAL VALUE OVER")
            b.append(row[3])
            c.append(b)
        elif temp[0] == 'OLD' and temp[1] == 'NEW':
            b.append(row[0])
            b.append(row[3])
            b.append("NO VALUE")
            c.append(b)
    elif len(row) > 5:
        inf_set = []
        memid = row[0]
        if row[2] == 'OLD':
            for x in range(4, len(row), 4):
                if row[x] == 'NEW':
                    tempset2 = []
                    tempset2.append(memid)
                    tempset2.append(row[x-1])
                    tempset2.append("NO VALUE")
                    c.append(tempset2)
        elif row[2] == "NEW":
            newnew = ''
            newold = ''
            partialover = []
            for x in range(4, len(row), 4):
                if row[x] == 'NEW':
                    tempset2 = []
                    tempset2.append(memid)
                    tempset2.append(row[x-1])
                    tempset2.append("NO VALUE")
                    c.append(tempset2)
                    newnew = 1
                elif row[x] == 'OLD':
                    newold = 1
                    partialover.append(row[x-1])

            if newold == 1:
                tempset2 = []
                tempset2.append(memid)
                tempset2.append(row[1])
                tempset2.append("PARTIAL VALUE OVER")
                tempset2.append(partialover)
                c.append(tempset2)
            elif newnew == 1:
                tempset2 = []
                tempset2.append(memid)
                tempset2.append(row[1])
                tempset2.append("FULL VALUE")
                c.append(tempset2)




with open('one_plus_results.csv', 'wb') as g:
	writer =csv.writer(g)
	for row in c:
		writer.writerow(row)
