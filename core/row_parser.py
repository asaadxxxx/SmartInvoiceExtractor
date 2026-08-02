from collections import defaultdict


class RowParser:

    def __init__(self, words):
        self.words = words

    def center(self, box):
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]

        return (
            sum(xs) / len(xs),
            sum(ys) / len(ys)
        )

    def rows(self):

        groups = defaultdict(list)

        for word in self.words:

            _, y = self.center(word["box"])

            key = round(y / 15) * 15

            groups[key].append(word)

        rows = []

        for key in sorted(groups.keys()):

            row = sorted(
                groups[key],
                key=lambda w: self.center(w["box"])[0]
            )

            rows.append(row)

        return rows

    def print_rows(self):

        for row in self.rows():

            print("=" * 80)

            print(
                " | ".join(
                    w["text"] for w in row
                )
            )