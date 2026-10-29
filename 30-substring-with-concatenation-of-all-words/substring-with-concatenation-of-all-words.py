
from typing import List
from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        word_len = len(words[0])
        word_count = len(words)
        total_len = word_len * word_count

        if len(s) < total_len:
            return []

        word_freq = Counter(words)
        result = []

        # Try each possible alignment of word-sized chunks
        for offset in range(word_len):
            left = offset
            seen = Counter()
            count = 0

            for right in range(offset, len(s) - word_len + 1, word_len):
                word = s[right:right + word_len]

                if word not in word_freq:
                    seen.clear()
                    count = 0
                    left = right + word_len
                    continue

                seen[word] += 1
                count += 1

                # Remove extra occurrences of a word
                while seen[word] > word_freq[word]:
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

                # All words matched
                if count == word_count:
                    result.append(left)

                    # Move window forward to search for overlapping matches
                    left_word = s[left:left + word_len]
                    seen[left_word] -= 1
                    count -= 1
                    left += word_len

        return result
