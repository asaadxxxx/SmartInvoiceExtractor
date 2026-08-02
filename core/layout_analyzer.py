from collections import defaultdict


class LayoutAnalyzer:

    def __init__(self, words):
        self.words = words

    def center(self, box):
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]

        return (
            sum(xs) / len(xs),
            sum(ys) / len(ys)
        )

    def sort_words(self):

        return sorted(
            self.words,
            key=lambda w: (
                self.center(w["box"])[1],
                self.center(w["box"])[0]
            )
        )

    def build_lines(self, tolerance=18):

        rows = defaultdict(list)

        for word in self.sort_words():

            _, y = self.center(word["box"])

            key = None

            for r in rows:

                if abs(r - y) <= tolerance:
                    key = r
                    break

            if key is None:
                key = y

            rows[key].append(word)

        result = []

        for y in sorted(rows):

            row = sorted(
                rows[y],
                key=lambda w: self.center(w["box"])[0]
            )

            result.append(row)

        return result