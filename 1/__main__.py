with open('input', 'r') as input_:
    buf = [c.split('\n') for c in input_.read().split("\n\n")]

    # We remove the last element of the last chunk as it includes
    # an empty string. We do this to avoid a lot of other boilerplate
    # crap to handle type conversion.
    del buf[-1][-1]
    result = []
    for chunk in buf:
        result.append(sum([int(c) for c in chunk]))
    result = sorted(result)

    print(f'Elf with highest calories is {max(result)}')

    print(f'Top three elves are {result[-3:]} ...')
    print(f'... containing a total of {sum(result[-3:])} calories')
