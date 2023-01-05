import sys
import pprint
pp = pprint.PrettyPrinter(indent=1)


ctx = []  # Stack of directories
_dir = '/'
fs = {
    '/': {}
}

TOTAL_DISK_SPACE    = 70000000
TARGET_UNUSED_SPACE = 30000000


def crashdump(ptr=None, ctx=None):
    print('\n== CRASHDUMP ==')
    print(f'ptr: {ptr}')
    print(f'ctx: {ctx}')
    print(f'dir: {_dir}')
    print(f'fs: {fs}')
    print('===============')
    sys.exit(1)


def calculate_dir_size(fs: dict, parent='/'):
    result = {
        parent: 0
    }

    for dirname, dirtype in fs.items():
        match dirtype:
            case int():
                result[parent] += dirtype
            case dict():
                new_parent = f'/{dirname}' if parent == '/' else f'{parent}/{dirname}'

                subdir = calculate_dir_size(dirtype, parent=new_parent)

                # Hack to avoid doucandidateble counting file sizes
                for dirname, dirsize in subdir.items():
                    if all([name.startswith(dirname) for name in subdir.keys()]):
                        result[parent] += dirsize

                result.update(subdir)
            case _:
                sys.exit(1)

    return result


with open('input', 'r') as input_:
    list_dir = False

    for line in input_.readlines():
        line = line.rstrip('\n')
        parts = line.split(' ')

        match parts[0]:
            case '$':
                match parts[1]:
                    case 'cd':
                        list_dir = False
                        parts = line.split(' ')

                        if parts[2] == '..':
                            ctx.pop()
                        else:
                            ctx.append(parts[2])
                    case 'ls':
                        list_dir = True
            case 'dir':
                ptr = fs[ctx[0]]

                for dir_ in ctx[1:]:
                    ptr = ptr[dir_]

                if not ptr.get(parts[1]):
                    ptr[parts[1]] = {}
            case _:
                ptr = fs[ctx[0]]

                for dir_ in ctx[1:]:
                    ptr = ptr[dir_]

                ptr[parts[1]] = int(parts[0])

    fssize = calculate_dir_size(fs['/'])
    pp.pprint(dict(sorted(fssize.items(), key=lambda item: item[1], reverse=True)))

    print(f'Part 1: {sum([x for x in fssize.values() if x <= 100000])}')

    unused_space = TOTAL_DISK_SPACE - fssize['/']
    space_to_free = TARGET_UNUSED_SPACE - unused_space

    print(f'The total size of the root is {fssize["/"]} with a target size of {TARGET_UNUSED_SPACE}')
    print(f'This means that we need to free up {space_to_free}')

    candidate_directories = sorted([(name, size) for (name, size) in fssize.items() if size >= space_to_free], key=lambda item: item[1])
    print(f'To achieve this we should remove {candidate_directories[0][0]} of size {candidate_directories[0][1]}')
