import sys
import pprint
pp = pprint.PrettyPrinter(indent=1)


ctx = []  # Stack of directories
_dir = '/'
fs = {
    '/': {}
}


def crashdump(ptr=None, ctx=None):
    print('\n== CRASHDUMP ==')
    print(f'ptr: {ptr}')
    print(f'ctx: {ctx}')
    print(f'dir: {_dir}')
    print(f'fs: {fs}')
    print('===============')
    sys.exit(1)


def calculate_dir_size(fs: dict, parent='/', result={}):
    for dirname, dirtype in fs.items():
        current_size = result.get(parent, 0)

        match dirtype:
            case int():
                result[parent] = current_size + dirtype
            case dict():
                result[parent] = current_size + sum(calculate_dir_size(dirtype, parent=f'{parent}/{dirname}').values())
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

    fssize = calculate_dir_size(fs)
    pp.pprint(fs)
    print(f'part 1: {sum([x for x in fssize.values() if x <= 100000])}')
