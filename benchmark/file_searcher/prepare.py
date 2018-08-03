from benchmark.common import create_folder
from benchmark.common import current_milli_time
from benchmark.common import print_result

data_size = 5
data_depth = 3


def generate_data_files(depth, size, folder=None):
    if depth > 0:
        for i in range(0, size):
            folder_name = str(i) + '-' + str(i + 1)
            path = ''
            if folder is not None:
                path = folder
            path += '/' + folder_name
            create_folder(path)
            generate_data_files(depth - 1, size, path)


def main():
    start = current_milli_time()
    generate_data_files(data_depth, data_size)
    print_result('generate', start, str(data_depth * data_size) + ' nested folders')


main()
