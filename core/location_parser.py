import math
import re

from core.field_keywords import FIELD_KEYWORDS


class LocationParser:

    def __init__(self, words):
        self.words = words

    def center(self, box):
        xs = [p[0] for p in box]
        ys = [p[1] for p in box]

        return (
            sum(xs) / len(xs),
            sum(ys) / len(ys)
        )

    def find_any(self, keywords):

        for word in self.words:

            text = word["text"].replace(" ", "").strip()

            for key in keywords:

                if key.replace(" ", "") in text:
                    return word

        return None

    def find_field(self, field):

        if field not in FIELD_KEYWORDS:
            return None

        return self.find_any(FIELD_KEYWORDS[field])

    def is_number(self, text):

        text = text.strip()

        return bool(
            re.fullmatch(r"[0-9٠-٩.,:/-]+", text)
        )

    def nearest_left(self, word):

        cx, cy = self.center(word["box"])

        best = None
        best_distance = float("inf")

        for w in self.words:

            x, y = self.center(w["box"])

            if x >= cx:
                continue

            if abs(y - cy) > 35:
                continue

            d = math.dist((cx, cy), (x, y))

            if d < best_distance:
                best = w
                best_distance = d

        return best

    def nearest_right(self, word):

        cx, cy = self.center(word["box"])

        best = None
        best_distance = float("inf")

        for w in self.words:

            x, y = self.center(w["box"])

            if x <= cx:
                continue

            if abs(y - cy) > 35:
                continue

            d = math.dist((cx, cy), (x, y))

            if d < best_distance:
                best = w
                best_distance = d

        return best

    def nearest_down(self, word):

        cx, cy = self.center(word["box"])

        best = None
        best_distance = float("inf")

        for w in self.words:

            x, y = self.center(w["box"])

            if y <= cy:
                continue

            if abs(x - cx) > 100:
                continue

            d = math.dist((cx, cy), (x, y))

            if d < best_distance:
                best = w
                best_distance = d

        return best

    def nearest_left_number(self, word):

        cx, cy = self.center(word["box"])

        best = None
        best_distance = float("inf")

        for w in self.words:

            x, y = self.center(w["box"])

            if x >= cx:
                continue

            if abs(y - cy) > 40:
                continue

            if not self.is_number(w["text"]):
                continue

            d = math.dist((cx, cy), (x, y))

            if d < best_distance:
                best = w
                best_distance = d

        return best

    def nearest_right_number(self, word):

        cx, cy = self.center(word["box"])

        best = None
        best_distance = float("inf")

        for w in self.words:

            x, y = self.center(w["box"])

            if x <= cx:
                continue

            if abs(y - cy) > 40:
                continue

            if not self.is_number(w["text"]):
                continue

            d = math.dist((cx, cy), (x, y))

            if d < best_distance:
                best = w
                best_distance = d

        return best

    def extract_right_value(self, field):

        label = self.find_field(field)

        if label is None:
            return None

        # الفواتير العربية
        value = self.nearest_left_number(label)

        if value:
            return value["text"]

        # الفواتير الإنجليزية
        value = self.nearest_right_number(label)

        if value:
            return value["text"]

        # احتياطي إذا لم تكن القيمة رقمًا
        value = self.nearest_left(label)

        if value:
            return value["text"]

        value = self.nearest_right(label)

        if value:
            return value["text"]

        return None