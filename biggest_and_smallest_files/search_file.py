import os
import glob


def search_in_one_dir(dir_name: str, count: int):
    all_sizes = []
    all_py = glob.glob(dir_name + os.sep + '*.py')
    for file_name in all_py:
        file_size = os.path.getsize(file_name)
        all_sizes.append((file_size, file_name))
    all_sizes.sort()
    print(all_sizes[:count])
    print(all_sizes[-count:])


def search_in_one_dir_rec(dir_name: str, count: int, trace: bool = False):
    all_sizes = []
    for (this_dir, subs_here, files_here) in os.walk(dir_name):
        if trace:
            print(this_dir)
        for file_name in files_here:
            if file_name.endswith('.py'):
                if trace:
                    print('...', file_name)
                full_name = os.path.join(this_dir, file_name)
                full_size = os.path.getsize(full_name)
                all_sizes.append((full_size, full_name))
    all_sizes.sort()
    print(all_sizes[:count])
    print(all_sizes[-count:])
