from functools import partial

with open('input', 'r') as input_:
    forest = input_.read()[:-1]

    rows = [[int(r) for r in row] for row in forest.split('\n')]
    width = len(rows[0])
    cols = [[int(r[i]) for r in rows] for i in range(0, width)]
    height = len(cols[0])

    visible_trees = []
    scenic_scores = {}

    for i, r in enumerate(rows):
        for j, t in enumerate(r):
            if i in [0, width - 1] or j in [0, height - 1]:
                visible_trees.append(t)
                continue

            # Determine the shortest edge
            # Make max() call happy with empty seqs
            vertical = cols[j][0:i] if (i + 1) <= (height / 2) else cols[j][(i+1):]
            horizontal = r[0:j] if (j + 1) <= (width / 2) else r[(j+1):]

            left, right = r[0:j], r[j+1:]
            up, down = cols[j][0:i], cols[j][(i+1):]

            max_hor = min([max(left), max(right)])
            max_ver = min([max(up), max(down)])

            print(f'max_hor: {max_hor}, max_ver: {max_ver}')

            f = lambda u, d, l, r: u * d * l * r
            f_ = partial(f)

            if t > max_ver or t > max_hor:
                visible_trees.append(t)

                left.reverse()
                up.reverse()

                # Calculate scenic scenic score
                for i, l in enumerate(left):
                    if l >= t:
                        f_ = partial(f_, i + 1)

                for i, r, in enumerate(right):
                    if r >= t:
                        f_ = partial(f_, i + 1)

                for i, u in enumerate(up):
                    if u >= t:
                        f_ = partial(f_, i + 1)

                for i, d in enumerate(down):
                    if d >= t:
                        f_ = partial(f_, i + 1)

    print(f'Total visible trees: {len(visible_trees)}')

