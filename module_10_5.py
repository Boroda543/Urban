import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    filenames = [f'file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_duration = time.time() - start_time
    print(f'Линейный вызов завершён за: {linear_duration:.6f} секунд')

    start_time = time.time()
    with Pool(processes=len(filenames)) as pool:
        pool.map(read_info, filenames)
    multiprocess_duration = time.time() - start_time
    print(f'Многопроцессный вызов завершён за: {multiprocess_duration:.6f} секунд')