from helpers import AoCHelper

input = AoCHelper.read_input_lines("day7/test1.txt")

cd_lines = [i for i in range(len(input)) if (input[i][:4] == '$ cd' and input[i] != '$ cd ..')]
cd_lines.append(len(input))

contents = {}

for idx, j in enumerate(cd_lines[:-1]):
    _, _, dir_name = input[j].split()

    # if input[j + 1] == '$ ls' and dir_name not in contents.keys():
    contents[dir_name] = [l for l in input[j + 2: cd_lines[idx + 1]] if l != '$ cd ..']



dir_names = list(contents.keys())
dir_names.reverse()


def print_contents(contents, tab, dir):
    for c in contents[dir]:
        f, l = c.split()

        if AoCHelper.is_integer(f):
            print(tab * ' ' + ' - ' + c)
        else:
            print(tab * ' ' + ' - ' + l + '/')
            print_contents(contents, tab + 2, l)


# print('/')
# print_contents(contents, 0, '/')


def build_file_structure(contents, dir):
    dir_cont = {}

    for c in contents[dir]:
        f, l = c.split()

        if AoCHelper.is_integer(f):
            dir_cont[l] = f
        else:
            dir_cont[l] = build_file_structure(contents, l)

    return dir_cont


file_st = {'/': build_file_structure(contents, '/')}
print(file_st)


def find_all_files_in_dir(sub_struct):
    files = []

    for k in sub_struct.keys():
        if AoCHelper.is_integer(sub_struct[k]):
            files.append((k, sub_struct[k]))
        else:
            files += find_all_files_in_dir(sub_struct[k])

    return files


def calculate_dir_sizes(struct, dir, prefix):
    dir_sizes = {}
    direct_size = 0
    indirect_size = 0

    for k in struct.keys():
        if not AoCHelper.is_integer(struct[k]):
            print(f"Adding {int(struct[k])}B for file {k} to size of dir {dir}")
            direct_size += int(struct[k])
        elif len(struct[k].keys()) > 0:
            underlying_struct_sizes = calculate_dir_sizes(struct[k], prefix + '/' + k, prefix + k)
            dir_sizes.update(underlying_struct_sizes)
            direct_size += sum([x - y for (x, y) in underlying_struct_sizes.values()])

    dir_sizes[dir] = (direct_size, indirect_size)

    return dir_sizes


print(find_all_files_in_dir(file_st))

# dir_sizes = calculate_dir_sizes(file_st['/'], '/', '/')
# print(dir_sizes)
# res = sum([x for (x,y) in dir_sizes.values() if x + y <= 100000])
# print(res)