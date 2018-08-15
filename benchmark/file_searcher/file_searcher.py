import os

from benchmark.common import data_folder
from benchmark.common import current_milli_time
from benchmark.common import print_result


def search_file_dir(search, dir, subcall=False):
	start = current_milli_time()
	file_list = os.listdir(dir)
	trouve = False
	for file in file_list:
		if file.endswith('.json'):
			part_name = file.split('-')
			if len(part_name) > 1 and part_name[0] < search < part_name[1]:
				yield file
				print('Find in directory : ' + dir)
				trouve = True
	if not trouve:
		dir_list = os.walk(dir)
		for _, dirs, _ in dir_list:
			for directo in dirs:
				part_name = directo.split('-')
				if len(part_name) > 1 and part_name[0] < search < part_name[1]:
					yield from search_file_dir(search, dir + '\\' + directo, True)
	if subcall is False:
		print_result('total', start, 'searching file to insert index in dir : ' + dir)
		
result = search_file_dir('e', data_folder)
for i in result:
    print(i)
print()
