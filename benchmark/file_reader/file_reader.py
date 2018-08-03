import time
import os


def current_milli_time():
    return int(round(time.time() * 1000))


def print_result(subject, start, purpose=None):
    p = ''
    if purpose is not None:
        p = ' for ' + purpose
    print(subject + ': ' + str(current_milli_time() - start) + 'ms' + p)


def count_objects():
    print('count_objects')
    s = start = current_milli_time()
    c = 0
    new_object = False
    with open('./data.json') as f:
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
    with open('./data.json') as f:
        print_result('open', s)
        s = current_milli_time()
        lines = f.readlines()
        print_result('readlines', s)
        s = current_milli_time()
        i = 1
        stop = 10
        for _ in lines:
            if i >= stop:
                break
            i += 1
        print_result('loop', s)
    print_result('total', start, str(i) + ' lines')


def search_object_bis():
    print('search_object_bis')
    s = start = current_milli_time()
    with open('./data.json') as f:
        print_result('open', s)
        s = current_milli_time()
        print('Statham' in f)
        print_result('loop', s)
    print_result('total', start, 'searching Statham')

def search_file(search, dir):
	start = current_milli_time()
	file_list = os.listdir(dir)
	for file in file_list:
		part_name = file.split('-')
		if os.path.isdir(file):
			yield from search_file(search, dir + '\\' + file)
		if len(part_name) > 1 and search > part_name[0] and search < part_name[1]:
			yield file
	print_result('total', start, 'searching file to insert index in dir : ' + dir)
	
def search_file_dir(search, dir):
	start = current_milli_time()
	file_list = os.listdir(dir)
	trouve = False
	for file in file_list:
		if file.endswith('.json'):
			part_name = file.split('-')
			if len(part_name) > 1 and search > part_name[0] and search < part_name[1]:
				yield file
				print('Find in directory : ' + dir)
				trouve = True
	if not trouve:
		dir_list = os.walk(dir)
		for _, dirs, _ in dir_list:
			for directo in dirs:
				yield from search_file_dir(search, dir + '\\' + directo)
	print_result('total', start, 'searching file to insert index in dir : ' + dir)
			
count_objects()
print()
search_object()
print()
search_object_bis()
print()
result = search_file('b', '.\\search_file')
for i in result:
	print(i)
print()
result = search_file_dir('e', '.\\search_file')
for i in result:
	print(i)
print()