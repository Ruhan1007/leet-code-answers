class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_map = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[:j]
                right = word[j:]

                if left == left[::-1]:
                    rev = right[::-1]
                    if rev in word_map and word_map[rev] != i:
                        result.append([word_map[rev], i])

                if j != len(word) and right == right[::-1]:
                    rev = left[::-1]
                    if rev in word_map and word_map[rev] != i:
                        result.append([i, word_map[rev]])

        return result