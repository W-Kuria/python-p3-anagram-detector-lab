# your code goes here!
class Anagram:
    def __init__(self, word):
        # store the word in lowercase for consistent comparison
        self.word = word.lower()

    def match(self, candidates):
        matches = []
        # sort the letters of the stored word
        sorted_word = sorted(self.word)

        for candidate in candidates:
            candidate_lower = candidate.lower()

            # skip if candidate is exactly the same as the word
            if candidate_lower == self.word:
                continue

            # check if sorted letters match
            if sorted(candidate_lower) == sorted_word:
                matches.append(candidate)

        return matches
