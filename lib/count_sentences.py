#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""    # use a "private" attribute
        self.value = value  # go through setter for validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ""

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")

    def count_sentences(self):
        if not self.value:
            return 0

        # Normalize punctuation: replace ?, ! with .
        text = self.value.replace("?", ".").replace("!", ".")

        # Split on periods
        parts = text.split(".")

        # Filter out empty "sentences"
        sentences = [p.strip() for p in parts if p.strip() != ""]

        return len(sentences)
