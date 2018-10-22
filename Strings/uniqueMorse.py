class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        # ord('a') = 97
        morseAlphabet = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        transformList = []
        for word in words:
            morseWord = ''
            for ch in word:
                morseWord += morseAlphabet[ord(ch) - 97]
            transformList.append(morseWord)
        print(set(transformList))
        return len(set(transformList))
