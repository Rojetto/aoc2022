import re

root_dir = {}
current_dir = root_dir

for line in open('07.txt', "r"):
    if re.match(r"\$ cd /", line):
        current_dir = root_dir
    elif m := re.match(r"\$ cd ([a-zA-Z\.]+)", line):
        current_dir = current_dir[m[1]]
    elif m := re.match(r"dir ([a-zA-Z]+)", line):
        dir_name = m[1]
        if dir_name not in current_dir:
            current_dir[dir_name] = {'..': current_dir}
    elif m := re.match(r"(\d+) ([a-zA-Z]+(?:\.[a-zA-Z]+)?)", line):
        current_dir[m[2]] = int(m[1]) # file size

def get_dir_size(dir):
    size = 0
    for k, v in dir.items():
        if k == '..':
            continue
        if isinstance(v, int):
            size += v
        else:
            size += get_dir_size(v)
    return size

total_space = 70000000
used_space = get_dir_size(root_dir)
needed_space = 30000000
space_to_free = needed_space - (total_space - used_space)

def get_big_dirs(dir):
    big_dirs = []
    for k, v in dir.items():
        if k == '..':
            continue
        if isinstance(v, int):
            continue
        if get_dir_size(v) >= space_to_free:
            big_dirs.append(v)
        big_dirs += get_big_dirs(v)
    return big_dirs

print(min(get_dir_size(d) for d in get_big_dirs(root_dir)))
