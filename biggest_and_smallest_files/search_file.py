import os
import glob
import sys


def search_in_one_dir(dir_name: str, count: int, ext_name: str = '.py'):
    all_sizes = []
    all_py = glob.glob(dir_name + os.sep + '*' + ext_name)
    for file_name in all_py:
        file_size = os.path.getsize(file_name)
        all_sizes.append((file_size, file_name))
    all_sizes.sort()
    print(all_sizes[:count])
    print(all_sizes[-count:])


def search_in_one_dir_rec(dir_name: str, count: int, ext_name: str = '.py', trace: bool = False):
    all_sizes = []
    for (this_dir, subs_here, files_here) in os.walk(dir_name):
        if trace:
            print(this_dir)
        for file_name in files_here:
            if file_name.endswith(ext_name):
                if trace:
                    print('...', file_name)
                full_name = os.path.join(this_dir, file_name)
                full_size = os.path.getsize(full_name)
                all_sizes.append((full_size, full_name))
    all_sizes.sort()
    print(all_sizes[:count])
    print(all_sizes[-count:])


def search_in_modules(count: int,
                      ext_name: str = '.py',
                      trace: int = 0):
    visited = {}
    all_sizes = []
    for src_dir in sys.path:
        for (this_dir, subs_here, files_here) in os.walk(src_dir):
            if trace > 0:
                print(this_dir)
            this_dir = os.path.normpath(this_dir)
            fix_case = os.path.normcase(this_dir)
            if fix_case in visited:
                continue
            else:
                visited[fix_case] = True

            for file_name in files_here:
                if file_name.endswith(ext_name):
                    if trace > 1:
                        print('...', file_name)
                    full_name = os.path.join(this_dir, file_name)
                    try:
                        full_size = os.path.getsize(full_name)
                    except os.error:
                        print('skipping', full_name, sys.exc_info()[0])
                    else:
                        full_lines = len(open(full_name, 'rb').readlines())
                        all_sizes.append((full_size, full_lines, full_name))
    print('By size...')
    all_sizes.sort()
    print(all_sizes[:count])
    print(all_sizes[-count:])

    print('By lines...')
    all_sizes.sort(key=lambda x: x[1])
    print(all_sizes[:count])
    print(all_sizes[-count:])


def full_scan(dir_name: str,
              count: int,
              ext_name: str = '.py',
              trace: int = 0):
    visited = set()
    all_sizes = []
    for (this_dir, subs_here, files_here) in os.walk(dir_name):
        if trace > 0:
            print(this_dir)
        this_dir = os.path.normpath(this_dir)
        fix_case = os.path.normcase(this_dir)
        if fix_case in visited:
            if trace > 0:
                print('Skipping: ' + this_dir)
        else:
            visited.add(fix_case)
            for file_name in files_here:
                if file_name.endswith(ext_name):
                    if trace > 1:
                        print('...', file_name)
                    full_name = os.path.join(this_dir, file_name)
                    try:
                        full_size = os.path.getsize(full_name)
                        full_lines = len(open(full_name, 'rb').readlines())
                    except Exception:
                        print('error', sys.exc_info()[0])
                    else:
                        all_sizes.append((full_size, full_lines, full_name))
    print('By size...')
    all_sizes.sort()
    print(all_sizes[:count])
    print(all_sizes[-count:])

    print('By lines...')
    all_sizes.sort(key=lambda x: x[1])
    print(all_sizes[:count])
    print(all_sizes[-count:])
