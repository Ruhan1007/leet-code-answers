class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            line = []
            line_length = 0

            # Greedily select as many words as possible
            while i < n and line_length + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_length += len(words[i])
                i += 1

            # Last line or line with only one word
            if i == n or len(line) == 1:
                text = " ".join(line)
                text += " " * (maxWidth - len(text))

            else:
                # Calculate spaces between words
                total_spaces = maxWidth - line_length
                gaps = len(line) - 1

                spaces = total_spaces // gaps
                extra = total_spaces % gaps

                text = ""

                for j in range(gaps):
                    text += line[j]
                    text += " " * (spaces + (1 if j < extra else 0))

                text += line[-1]

            result.append(text)

        return result