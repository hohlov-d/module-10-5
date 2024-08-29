import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='UTF-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


filenames = [f'./file {number}.txt' for number in range(1, 5)]
# start = datetime.datetime.now()
# for i in filenames:
#     read_info(i)
#
# end = datetime.datetime.now()
# print(end - start)


if __name__ == '__main__':
    start1 = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end1 = datetime.datetime.now()
    print(end1 - start1)
