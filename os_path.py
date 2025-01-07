import os

current_work_directory = os.getcwd()
print(current_work_directory)

directories_list = os.listdir(current_work_directory)
print(directories_list)

for path, dirs, files in os.walk(current_work_directory):
    print(path)
    print(dirs)
    print(files)
    print('\n')

if os.path.exists(directories_list[0]):
    print(f"{directories_list[0]} exists")
else:
    print(f"{directories_list[0]} doesn't exists")

new_dir = current_work_directory + '/foo'
if os.path.exists(new_dir):
    print(f"{new_dir} exists")
else:
    os.mkdir(new_dir)

new_dirs = current_work_directory + '/foo/bar'
if os.path.exists(new_dirs):
    print(f"{new_dirs} exists")
else:
    os.makedirs(new_dirs)

os.rmdir(new_dirs)
os.rmdir(new_dir)

new_file = os.path.join(current_work_directory, 'new_file.txt')
print(new_file)

print(os.path.split(new_file))

print(os.path.dirname(new_file))
print(os.path.basename(new_file))

for directory in os.listdir():
    if os.path.isdir(directory):
        print(f"{directory} is a directory")
    elif os.path.isfile(directory):
        print(f"{directory} is a file")

print(os.sep)

print(os.path.getsize(current_work_directory))

print(os.path.abspath(directories_list[0]))