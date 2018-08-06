import os
import shutil

from benchmark.common import data_folder
from benchmark.common import current_milli_time
from benchmark.common import print_result

data_file = data_folder + '/data.json'


def count_objects():
    print('count_objects')
    s = start = current_milli_time()
    c = 0
    new_object = False
    with open(data_file) as f:
        print_result('open', s)
        s = current_milli_time()
        lines = f.readlines()
        print_result('readlines', s)
        s = current_milli_time()
        for line in lines:
            if '{' in line:
                new_object = True
            elif '}' in line and new_object:
                c += 1
                new_object = False
        print_result('loop', s)
    print_result('total', start, str(c) + ' objects')


def search_object():
    print('search_object')
    s = start = current_milli_time()
    with open(data_file) as f:
        print_result('open', s)
        s = current_milli_time()
        lines = f.readlines()
        print_result('readlines', s)
        s = current_milli_time()
        i = 1
        stop = len(lines)
        for _ in lines:
            if i >= stop:
                break
            i += 1
        print_result('loop', s)
    print_result('total', start, str(i) + ' lines')


def search_object_bis():
    print('search_object_bis')
    s = start = current_milli_time()
    with open(data_file) as f:
        print_result('open', s)
        s = current_milli_time()
        print('Statham' in f)
        print_result('loop', s)
    print_result('total', start, 'searching Statham')


def search_object_dicho(search):
    print('search search_object_dicho')
    s = start = current_milli_time()
    with open(data_file) as f:
        print_result('open', s)
        s = current_milli_time()
        lines = f.readlines()
        print_result('readlines', s)
        s = current_milli_time()
        result = dichotomie(lines, 0, len(lines), search)
        print_result('loop', s, 'result ' + str(result))
    print_result('total', start, 'value ' + search)


def dichotomie(lines, min, max, search):
	if min == max:
		if search == get_value(lines[min]):
			return lines[min]
		else:
			return None
	c = round((min + max) / 2)
	if get_value(lines[c]) is not None:
		compare = comparateur(search, get_value(lines[c])) 
		if search == get_value(lines[c]):
			return lines[c]
		elif compare == get_value(lines[c]):
			return dichotomie(lines, min, c - 1, search)
		else:
			return dichotomie(lines, c + 1, max, search)
	else:
		return dichotomie(lines, min + 1, max, search)


def get_value(line):
    value = line.split('\"value\":\"')
    if len(value) > 1:
        value = value[1].split('\"')
        return value[0]


def move_file(dir, file_name):
    print('move_file')
    s = start = current_milli_time()
    file_list = os.listdir(dir + '/test2')
    print_result('listdir', s)
    trouve = False
    stop = 500
    i = 1
    for file in file_list:
        if file == file_name:
            try:
                os.rename(dir + '/test2/' + file, dir + '/test/' + file)
            except OSError:
                os.mkdir(dir + '/test/')
                os.rename(dir + '/test2/' + file, dir + '/test/' + file)
            if i >= stop:
                break
            i += 1
    print_result('total', start, ' 1 files')

def move_file_lbyl(dir, file_name):
	print('move_file lbyl')
	s = start = current_milli_time()
	file_list = os.listdir(dir + '/test')
	print_result('listdir', s)
	trouve = False
	stop = 500
	i = 1
	for file in file_list:
		if file == file_name:
			if os.path.isdir(dir + '/test2'):
				os.rename(dir + '/test/' + file, dir + '/test2/' + file)
			else:
				os.mkdir(dir + '/test2/')
				os.rename(dir + '/test/' + file, dir + '/test2/' + file)
			if i >= stop:
				break
			i += 1
	print_result('total', start, ' 1 files')	
	
def move_file_shutil(dir, file_name):
	print('move_file_shutil')
	s = start = current_milli_time()
	file_list = os.listdir(dir + '/test2')
	print_result('listdir', s)
	trouve = False
	i = 1
	for file in file_list:
		if file == file_name:
			try:
				shutil.move(dir + '/test2/' + file, dir + '/test/')
			except OSError:
				os.mkdir(dir + '/test/')
				shutil.move(dir + '/test2/' + file, dir + '/test/')
	print_result('total', start, ' 1 files')	
	
def split_file():
	start = current_milli_time()
	input = open('./data/data2.json', 'r').read().split('\n')
	lenght = round(len(input)/2)
	for lines in range(0, len(input), lenght):
		l = lines + lenght
		if len(input) < l:
			l = len(input) - 1
		outputData = input[lines:l]
		i = 0
		if get_value(input[l - 1]) != None:
			endName = get_value(input[l - 1])
		else:
			while get_value(input[l - 1]) == None:
				endName = get_value(input[l - 1 - i])
				i += 1
		output = open('./data/' + get_value(input[lines]) + '-' + endName +'.json', 'w')
		output.write('\n'.join(outputData))
		output.close()
	print_result('total', start, str(lenght) + ' data in files')
	
def test_seek(f, min, max, search):
	print('search search_object_dicho')
	start = current_milli_time()
	result = search_dich(f, min, max, search)
	print_result('total', start, 'find value ' + str(result))
	
def search_dich(f, min, max, search):
	if min == max:
		f.seek(min)
		for line in f:
			if 'value' in line:
				if search == get_value(line):
					return line
				else:
					return None
				break
	c = round((min + max) / 2)
	f.seek(c)
	value = None
	for line in f:
		if 'value' in line:
			value = get_value(line)
			if value is not None:
				compare = comparateur(search, value) 
				if search == value:
					return line
				elif compare == value:
					return search_dich(f, min, c - 1, search)
				else:
					return search_dich(f, c + 1, max, search)
			else:
				return search_dich(f, min + 1, max, search)
			break	

def comparateur(str1, str2):
	num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	size = min(len(str1), len(str2))
	cpt1 = ''
	cpt2 = ''
	for i in range(0, size):
		if str1[i] in num and str2[i] in num:
			cpt1 += str1[i]
			cpt2 += str2[i]
		else:
			if cpt1 != '' and cpt2 != '':
				if cpt1 > cpt2:
					return str1
				elif cpt1 < cpt2:
					return str2
			cpt1 = ''
			cpt2 = ''
			if str1[i] > str2[i]:
				return str1
			elif str1[i] < str2[i]:
				return str2
				
	#Si ça se termine pas des chiffre on verifie s'il ne reste pas un chiffre pour un des deux sinon on compare ces chiffres			
	if cpt1 != '' and cpt2 != '':
		if len(str1) != len(str2):
			try:
				if str1[size] in num:
					return str1
			except:
				if str2[size] in num:
					return str2
				else:
					if str1[i] > str2[i]:
						return str1
					elif str1[i] < str2[i]:
						return str2
		else:
			if cpt1 > cpt2:
				return str1
			else:
				return str2
	
def delete_file(file_name):
	os.remove(file_name)
	print("File Removed!")
	
def copy_file(src, dst):
	print('copy file')
	start = current_milli_time()
	try:
		O_BINARY = os.O_BINARY
	except:
		O_BINARY = 0
	READ_FLAGS = os.O_RDONLY | O_BINARY
	WRITE_FLAGS = os.O_WRONLY | os.O_CREAT | os.O_TRUNC | O_BINARY
	BUFFER_SIZE = 128*1024
	print('INIT')
	try:
		fin = os.open(src, READ_FLAGS)
		stat = os.fstat(fin)
		fout = os.open(dst, WRITE_FLAGS, stat.st_mode)
		print('OPEN ok')
		for x in iter(lambda: os.read(fin, BUFFER_SIZE), b''):
			os.write(fout, x)
	finally:
		try:
			os.close(fin)
			delete_file(src)
		except: pass
		try: os.close(fout)
		except: pass
	print_result('total', start, 'copy and delete ' + src)
	
# count_objects()
# print()

# search_object()
# print()

# search_object_bis()
# print()
	
# print(comparateur('prenom9', 'prenom50'))
# print(comparateur('prenom50', 'prenom9'))
# print(comparateur('prenom50', 'prenome9'))
# print(comparateur('prenom5', 'prenom9a'))
# print(comparateur('prenom50b', 'prenom90a'))
# print(comparateur('prenom90b', 'prenom90a'))
# print(comparateur('prenom987', 'prenom997'))
# print()

# search_object_dicho('prenom987')
# print()

move_file(data_folder, 'dataMove.json')
print()

move_file_lbyl(data_folder, 'dataMove.json')
print()

move_file_shutil(data_folder, 'dataMove.json')
print()

copy_file(data_folder + '/test/' + 'dataMove.json', data_folder + '/test2/' + 'dataMove.json')
print()

# split_file()
# print()

# max = os.path.getsize(data_file)
# with open(data_file) as f:
	# test_seek(f, 0, max, 'prenom987')
# print()