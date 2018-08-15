import random

from benchmark.common import data_folder
from benchmark.common import create_folder
from benchmark.common import current_milli_time
from benchmark.common import print_result

data_size = 1000000
data_file = 'data.json'


def generate_data_file(size):
    with open(data_folder + '/' + data_file, 'w') as f:
        f.write('[\n')
        for i in range(0, size):
            ids = []
            for j in range(0, random.randint(1, 10)):
                ids.append(random.randint(0, 10000000000))
            f.write('{"value":"prenom' + str(i) + '","ids":' + str(ids) + '}')
            if i < size - 1:
                f.write(',')
            f.write('\n')
        f.write(']')


def main():
    create_folder()
    start = current_milli_time()
    generate_data_file(data_size)
    print_result('generate', start, str(data_size) + ' objects')


main()
