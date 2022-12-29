UPPERCASE_ASCII_START = 65
LOWERCASE_ASCII_START = 97


def priority(c: chr) -> int:
    if ord(c) < LOWERCASE_ASCII_START:
        return (ord(c) - UPPERCASE_ASCII_START) + 26 + 1
    else:
        return ord(c) - LOWERCASE_ASCII_START + 1


with open('input', 'r') as input_:
    result = 0

    lines = input_.readlines()
    assert(len(lines) % 3 == 0)

    for i in range(0, int(len(lines) / 3)):
        group = lines[i * 3: (i * 3) + 3]
        group = [l.rstrip('\n') for l in group]

        badge = set(group[0]) & set(group[1]) & set(group[2])
        assert len(badge) == 1

        result += priority(list(badge)[0])

    print(str(result))

