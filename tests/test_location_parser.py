def find_any(self, keywords):

    for word in self.words:

        text = word["text"].replace(" ", "").strip()

        for key in keywords:

            if key.replace(" ", "") in text:
                return word

    return None