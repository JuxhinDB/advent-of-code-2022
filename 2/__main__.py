pairs = {
    'A': 'B',
    'B': 'C',
    'C': 'A',
}

# Map X, Y, Z to A, B, C
ASCII_START = 65
ASCII_OFFSET = 23


def score(first: chr, second: chr) -> int:
    # A lot of golf
    second = chr(ord(second) - ASCII_OFFSET)
    base = ord(second) - ASCII_START + 1
    beats = lambda first, second : 6 if pairs[first] == second else 0
    score = 3 if first == second else beats(first, second)

    return base + score


with open('input', 'r') as input_:
    games = input_.readlines()
    print(f"Part 1 score: {sum([score(g.split(' ')[0], g.split(' ')[1][0]) for g in games])}")

    part_two = 0
    for g in games:
        g = g.split(' ')
        first, second = g[0], g[1][0]

        match second:
            case 'X':
                # Lose
                second = chr(67 + ASCII_OFFSET) if ord(first) - 1 == (ASCII_START - 1) else chr(ord(first) - 1 + ASCII_OFFSET)
            case 'Y':
                # Draw
                second = chr(ord(first) + ASCII_OFFSET)
            case 'Z':
                # Win
                second = chr(65 + ASCII_OFFSET) if ord(first) + 1 == (ASCII_START + 3) else chr(ord(first) + 1 + ASCII_OFFSET)
                print(f'Winning {first} against {second}')
            case _: exit('?')

        part_two += score(first, second)

    print(f'Part 2 score: {part_two}')
