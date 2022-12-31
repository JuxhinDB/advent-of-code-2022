

def section_to_set(section: str) -> set:
    parts = section.split('-')
    assert len(parts) == 2

    floor, ceiling = int(parts[0]), int(parts[1])

    # Inclusive bound
    return set(range(floor, ceiling + 1))


with open('input', 'r') as input_:
    result = 0

    for line in input_.readlines():
        sections = line.split(',')
        assert len(sections) == 2

        first, second = section_to_set(sections[0]), section_to_set(sections[1])

        # Is the second a subset of first?
        if first.issubset(second) or second.issubset(first):
            result += 1

    print(f'part 1 result: {result}')


with open('input', 'r') as input_:
    result = 0

    for line in input_.readlines():
        sections = line.split(',')
        assert len(sections) == 2

        first, second = section_to_set(sections[0]), section_to_set(sections[1])

        if len(first & second) > 0:
            result += 1

    print(f'part 2 result: {result}')
