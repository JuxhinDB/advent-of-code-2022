

with open('input', 'r') as input_:
    packet = input_.read().replace('\n', '')

    i = 0

    while i + 4 < len(packet):
        chunk = packet[i:i+4]

        if len(chunk) == len(set(chunk)):
            print(f'part 1: {i + 4}')
            break

        i += 1


with open('input', 'r') as input_:
    packet = input_.read().replace('\n', '')

    i = 0

    while i + 14 < len(packet):
        chunk = packet[i:i+14]

        if len(chunk) == len(set(chunk)):
            print(f'part 1: {i + 14}')
            break

        i += 1
