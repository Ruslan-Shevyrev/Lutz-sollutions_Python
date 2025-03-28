import join_and_split_file as jas

FILE = ''
FOLDER = ''

jas.split(from_file=FILE,
          to_dir=FOLDER,
          chunk_size=10000)

jas.join(from_dir=FOLDER,
         to_file=FILE)
