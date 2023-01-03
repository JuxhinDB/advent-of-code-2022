import pprint
pp = pprint.PrettyPrinter(indent=1)


ctx = []  # Stack of directories
_dir = '/'
fs = {
    '/': {}
}


def crashdump(ptr=None):
    print('\n== CRASHDUMP ==')
    print(f'ptr: {ptr}')
    print(f'ctx: {ctx}')
    print(f'dir: {_dir}')
    print(f'fs: {fs}')
    print('===============')


def calculate_dir_size(fs: dict, result={}):
    for dirname, dirlist in fs.items():
        for dir_ in dirlist:
            if isinstance(fs[dirname][dir_], int):
                if result.get(dirname):
                    result[dirname] += fs[dirname][dir_]
                else:
                    result[dirname] = fs[dirname][dir_]

            print(f'dirname: {dirname}, {dir_}')

    print(f'result: {result}')


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


    calculate_dir_size(fs)
