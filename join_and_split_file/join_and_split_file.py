import os

KILOBYTES = 1024
MEGABYTES = KILOBYTES * 1000
CHUNK_SIZE = int(1.4 * MEGABYTES)


def split(from_file: str,
          to_dir: str,
          chunk_size: int = CHUNK_SIZE) -> int:

    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    else:
        for file_name in os.listdir(to_dir):
            os.remove(os.path.join(to_dir, file_name))

    part = 0
    inp = open(from_file, 'rb')

    while True:
        chunk = inp.read(chunk_size)

        if not chunk:
            break
        part += 1
        file_name = os.path.join(to_dir, ('part%04d' % part))
        file_obj = open(file_name, 'wb')
        file_obj.write(chunk)
        file_obj.close()
    inp.close()
    assert part <= 9999
    return part


def join(from_dir: str,
         to_file: str,
         read_size: int = 1024):
    out = open(to_file, 'wb')
    parts = os.listdir(from_dir)
    parts.sort()
    for file_name in parts:
        file_path = os.path.join(from_dir, file_name)
        file_obj = open(file_path, 'rb')
        while True:
            file_bytes = file_obj.read(read_size)
            if not file_bytes:
                break
            out.write(file_bytes)
        file_obj.close()
    out.close()
