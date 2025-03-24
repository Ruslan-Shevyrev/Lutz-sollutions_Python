import os

PATH = 'C:\Test'


def lister(curr_dir):
    print('[' + curr_dir + ']')
    for file in os.listdir(curr_dir):
        path = os.path.join(curr_dir, file)
        if not os.path.isdir(path):
            print(path)
        else:
            lister(path)


if __name__ =='__main__':
    lister(PATH)
