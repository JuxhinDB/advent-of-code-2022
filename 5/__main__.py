import re


def parse_header(lines: str) -> dict:
    # We want to build our stack from the bottom up
    lines.reverse()

    stacks = {
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
    }

    for line in lines:
        i = 0
        column = 0

        # Napkin solution:
        #   1. Parse in chunks of 3 offset by 1 (space)
        #   2. If contains [  ] then push the character to that index
        while i + 3 <= len(line):
            column += 1
            assert column < 10

            chunk = line[i:i + 3]

            # Hacky
            if '[' in chunk:
                stacks[column].append(chunk[1])

            i += 4

    return stacks


with open('input', 'r') as input_:
    lines = [line.rstrip('\n') for line in input_.readlines()]
    stacks = parse_header(lines[0:8])
    print(f'1: {stacks[1]}\n2: {stacks[2]}\n3: {stacks[3]}\n4: {stacks[4]}\n5: {stacks[5]}\n6: {stacks[6]}\n7: {stacks[7]}\n8: {stacks[8]}\n9: {stacks[9]}')

    for procedure in lines[10:]:
        parsed_procedure = re.search(r'move\s([0-9].?)\sfrom\s([0-9].?)\sto\s([0-9].?)', procedure)

        amount = int(parsed_procedure.group(1))
        from_ = int(parsed_procedure.group(2))
        to_ = int(parsed_procedure.group(3))

        temp = []

        for _ in range(0, amount):
            temp.append(stacks[from_].pop())

        [stacks[to_].append(t) for t in temp]



    print(f'\nPart 1\n1: {stacks[1]}\n2: {stacks[2]}\n3: {stacks[3]}\n4: {stacks[4]}\n5: {stacks[5]}\n6: {stacks[6]}\n7: {stacks[7]}\n8: {stacks[8]}\n9: {stacks[9]}')



with open('input', 'r') as input_:
    lines = [line.rstrip('\n') for line in input_.readlines()]
    stacks = parse_header(lines[0:8])

    for procedure in lines[10:]:
        parsed_procedure = re.search(r'move\s([0-9].?)\sfrom\s([0-9].?)\sto\s([0-9].?)', procedure)

        amount = int(parsed_procedure.group(1))
        from_ = int(parsed_procedure.group(2))
        to_ = int(parsed_procedure.group(3))

        temp = []
        temp_index = len(stacks[from_]) - amount

        temp = stacks[from_][temp_index:]
        del stacks[from_][temp_index:]

        [stacks[to_].append(t) for t in temp]


    print(f'\nPart 2\n1: {stacks[1]}\n2: {stacks[2]}\n3: {stacks[3]}\n4: {stacks[4]}\n5: {stacks[5]}\n6: {stacks[6]}\n7: {stacks[7]}\n8: {stacks[8]}\n9: {stacks[9]}')




