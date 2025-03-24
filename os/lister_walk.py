import os

PATH = 'C:\Test'


def lister(root):
    for (this_dir, subs_here, files_here) in os.walk(root):
        print('['+this_dir+']')
        for f_name in files_here:
            path = os.path.join(this_dir, f_name)
            print(path)


if __name__ =='__main__':
    lister(PATH)
