import numpy as np
from pandas import HDFStore, DataFrame, read_hdf, Series, concat
import time
from collections import namedtuple
import h5py
from multiprocessing import Process, Queue
import argparse

def selct_by_condition_process(file_name, dataset_name, condition, queue):
	hdf = HDFStore(file_name)
	test = hdf.select(dataset_name, where=condition)
	# print(test.get_values().size/2)

	queue.put(test.get_values())
	
	
def selct_by_condition(file_name, dataset_name, condition):
	hdf = HDFStore(file_name)
	test = hdf.select(dataset_name, where=condition)
	# print(test.get_values().size/2)

	hdf.close()
	return test.get_values()
	
	
def selct(file_name, dataset_name):
	hdf = HDFStore(file_name)
	test = hdf.select(dataset_name)
	# print(test.get_values().size/2)

	hdf.close()
	return test.get_values()
	
	
def update_by_condition(file_name, dataset_name, condition, value, index):
	start = time.time()
	hdf = HDFStore(file_name)
	test = hdf.select(dataset_name, where=condition)
	
	for i in test.get_values():
		i[index] = value
	if test.size > 0:
		hdf.put('d1', test, format='table', data_columns=True)
	# queue.put(test.get_values())
	end = time.time()
	print("update by condition terminé en {} secondes".format(end - start))
	
	
def update(file_name, dataset_name, value, index):
	start = time.time()
	hdf = HDFStore(file_name)
	test = hdf.select(dataset_name)
	
	for i in test.get_values():
		i[index] = value
	if test.size > 0:
		hdf.put('d1', test, format='table', data_columns=True)
	# queue.put(test.get_values())
	end = time.time()
	print("update terminé en {} secondes".format(end - start))
	
	
def create_h5(size):
	print('creating h5 file ...')
	hdf = HDFStore('storage.h5')
	df = DataFrame(np.random.rand(size, 1), columns=('A',))
	df2 = DataFrame(np.random.rand(size, 1), columns=('C',))

	hdf.put('d1', df, format='table', data_columns=True)
	hdf.put('d2', df2, format='table', data_columns=True)
	hdf.close()
	print('h5 file created')


def run_processes(hdf, queue_d1, queue_d2):
	thread_render = Process(target=selct_by_condition_process, args=(hdf, 'd1', ['A>0.5'], queue_d1))
	thread_render.start()
	thread_render2 = Process(target=selct_by_condition_process, args=(hdf, 'd2', ['C>0.8'], queue_d2))
	thread_render2.start()


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-type', action='store', dest='type',
                    help='type of test (mono | multi | condition | update)')

	parser.add_argument('-create', action='store', type=int,dest='size_create',
						default=0,
						help='Number of line in the dataset')

	parser.add_argument('-loop', action='store', type=int, default=1,
						dest='size_loop',
						help='Number of loop for testing')

	results = parser.parse_args()
	size_loop = results.size_loop
	size_create = results.size_create
	type = results.type
		
	if size_create > 0:
		create_h5(size_create)
	
	# hdf_test = HDFStore('storage.h5')
	hdf = 'storage.h5'
	
	timer = 0
	if type == 'multi':
		for i in range(size_loop):
		
			start = time.time()
			
			queue_d1 = Queue()
			queue_d2 = Queue()
			run_processes(hdf, queue_d1, queue_d2)
			size_d1 = queue_d1.get().size/2
			size_d2 = queue_d2.get().size/2
			# print(size_d1, size_d2)
			end = time.time()
			timer += end - start
		
		print("temps moyen sur {} loop multiprocess {} secondes".format(size_loop, (timer)/size_loop))
	
	elif type == 'mono':
		hdf = HDFStore('storage.h5')
		for i in range(size_loop):
			start = time.time()
			size_d1 = selct(hdf, 'd1')
			size_d2 = selct(hdf, 'd2')
			# print(np.union1d(size_d1, size_d2))
			np.union1d(size_d1, size_d2)
			
			end = time.time()
			timer += end - start
		hdf.close()
		print("temps moyen sur {} loop mono process {} secondes".format(size_loop, (timer)/size_loop))
	
	elif type == 'condition':	
		for i in range(size_loop):
			start = time.time()
			size_d1 = selct_by_condition(hdf, 'd1', ['A>0.5']).size
			size_d2 = selct_by_condition(hdf, 'd2', ['C>0.8']).size
			# print(size_d1, size_d2)
			
			end = time.time()
			timer += end - start
			
		print("temps moyen sur {} loop read h5 {} secondes".format(size_loop, (timer)/size_loop))
	elif type == 'update':	
		for i in range(size_loop):
			start = time.time()
			update(hdf, 'd1', 0, 0)
			
			end = time.time()
			timer += end - start
			
		print("temps moyen sur {} loop update {} secondes".format(size_loop, (timer)/size_loop))
	else:
		print('Invalid argument')