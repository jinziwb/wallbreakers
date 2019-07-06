class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        
        paragraph = paragraph.replace(",", " ")
        paragraph = paragraph.replace(".", " ")
        paragraph = paragraph.replace("!", " ")
        paragraph = paragraph.replace("?", " ")
        paragraph = paragraph.replace(";", " ")
        paragraph = paragraph.replace("'", " ")
        words = paragraph.split(" ")

        lower_words = []
        for word in words:
            lower_words.append(word.lower())
        
        pCount = collections.Counter(lower_words)

        for word in banned:
            del pCount[word]
        del pCount[""]
        
        return (pCount).most_common(1)[0][0]
