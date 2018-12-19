import numpy as np
import time
import h5py
import argparse

def create_h5_file(size):

	mon_tableau = np.random.rand(size, 1)
	mon_tableau2 = np.random.rand(size, 1)
	mon_tableau3 = np.random.rand(size, 2)

	# création du fichier hdf5
	mon_fichier = h5py.File('./mon_fichier.h5', 'a')
	del mon_fichier['d1']
	del mon_fichier['d2']
	del mon_fichier['d3']
	mon_dataset = mon_fichier.create_dataset("d1", data=mon_tableau)
	mon_dataset2 = mon_fichier.create_dataset("d2", data=mon_tableau2)
	mon_dataset3 = mon_fichier.create_dataset("d3", data=mon_tableau3)
	mon_fichier.flush()
	mon_fichier.close()


def upadate_test():
	# update
	start = time.time()
	mon_fichier = h5py.File('./mon_fichier.h5', 'a')
	mon_dataset = mon_fichier['d1']
	mon_dataset3 = mon_fichier['d3']
	mon_dataset[0, 0] = 0
	mon_dataset3[3, 0] = 0
	end = time.time()
	print("update all en {} secondes".format(end - start))
	mon_fichier.close()


def union_test():
	# Union = OR query condition
	start = time.time()
	mon_fichier = h5py.File('./mon_fichier.h5', 'a')
	mon_dataset = mon_fichier['d1']
	mon_dataset2 = mon_fichier['d2']
	# print(np.union1d(mon_dataset, mon_dataset2))
	np.union1d(mon_dataset, mon_dataset2)
	end = time.time()
	print("Union en {} secondes".format(end - start))
	mon_fichier.close()


def intersect_test():
	# Intersect = AND query condition
	start = time.time()
	mon_fichier = h5py.File('./mon_fichier.h5', 'a')
	mon_dataset = mon_fichier['d1']
	mon_dataset2 = mon_fichier['d2']
	# print(np.intersect1d(mon_dataset, mon_dataset2))
	np.intersect1d(mon_dataset, mon_dataset2)
	end = time.time()
	print("Intersect en {} secondes".format(end - start))
	mon_fichier.close()

def filter_by_mask_test():
	start = time.time()
	mon_fichier = h5py.File('./mon_fichier.h5', 'a')
	mon_dataset = mon_fichier['d1']
	mon_dataset3 = mon_fichier['d3']

	# generate mask used to filter dataset
	mask = np.in1d(mon_dataset3[:, 0], mon_dataset)
	print(mask)

	# apply mask
	print(mon_dataset3[:][mask])
	end = time.time()
	print("filter en {} secondes".format(end - start))
	mon_fichier.close()
	

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	
	parser.add_argument('--create', action='store', type=int,dest='size_create',
						default=0,
						help='Number of line in the dataset')

	parser.add_argument('--update',
						dest='update',
						action='store_true', 
						help='run the update test')
	parser.add_argument('--union',
						dest='union',
						action='store_true',
						help='run the union test')
	parser.add_argument('--intersect',
						dest='intersect',
						action='store_true',
						help='run the intersect test')
	parser.add_argument('--filter',
						dest='filter',
						action='store_true',
						help='run the filter by mask test')

	
	results = parser.parse_args()
	size_create = results.size_create
	update = results.update
	union = results.union
	intersect = results.intersect
	filter = results.filter
	
	if size_create > 0:
		create_h5_file(size_create)
	if update:
		upadate_test()
	if union:
		union_test()
	if intersect:
		intersect_test()
	if filter:
		filter_by_mask_test()