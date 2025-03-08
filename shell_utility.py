import shutil
import os
from glob import iglob

source_files = ['shell_utility.py', 'os_path.py', 'iter_function.py']
splice_source_file = 'splice_source_file.txt'

with open(splice_source_file, 'wt') as outfile:
    for source_file in source_files:
        with open(source_file, 'rt') as infile:
            shutil.copyfileobj(infile, outfile)

splice_source_file_copyfile = 'splice_source_file_copyfile.txt'

shutil.copyfile(splice_source_file, splice_source_file_copyfile)

splice_source_file_copy = 'splice_source_file_copy.txt'

shutil.copy(splice_source_file, splice_source_file_copy)

splice_source_file_copy_dir = 'splice_source_file_copy_dir'

if os.path.exists(splice_source_file_copy_dir):
    print(f"{splice_source_file_copy_dir} exists")
else:
    os.mkdir(splice_source_file_copy_dir)

shutil.copy(splice_source_file, splice_source_file_copy_dir)

splice_source_file_copy2 = 'splice_source_file_copy2.txt'

# copy2 will retain the file meta attributes (permission bits, access time, creation time, etc.)
shutil.copy2(splice_source_file, splice_source_file_copy2)

for copy_file in iglob('splice_source_file_copy*.txt'):
    shutil.copy2(copy_file, splice_source_file_copy_dir)

splice_source_file_copy_dir_copy = 'splice_source_file_copy_dir_copy'

shutil.copytree(splice_source_file_copy_dir, splice_source_file_copy_dir_copy, dirs_exist_ok=True)

splice_source_file_copy_dir_copy_ignore = 'splice_source_file_copy_dir_copy_ignore'

shutil.copytree(splice_source_file_copy_dir, splice_source_file_copy_dir_copy_ignore, ignore=shutil.ignore_patterns('*copy*'),
                dirs_exist_ok=True)



