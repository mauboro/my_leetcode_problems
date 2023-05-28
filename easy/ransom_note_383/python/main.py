#those two solutions were made without external help, due to that fact and the other interesting fact that is my lack of intelligence, I'm currently not able to assert the time complexity of those two due to the use of the count method. The only thing I suppose I know is that the space complexity of the first one is O(2n) (MAYBE) and the space complexity of the second one is O(1) because I do not create any data structures proportional to the input, or I could be wrong, I do not know the inner workings of the count method

class solution(object):
    def canconstruct(self, ransomnote, magazine):
        """
        :type ransomnote: str
        :type magazine: str
        :rtype: bool
        """
        r_letters = {l:ransomnote.count(l) for l in ransomnote}
        m_letters = {l:magazine.count(l) for l in ransomnote}
        print(r_letters)
        print(m_letters)
        for k, v in r_letters.items():
            if m_letters.get(k) - v < 0:
                return false
        return true

class SolutionRefactored(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomnote: str
        :type magazine: str
        :rtype: bool
        """
        for l in ransomNote:
            if magazine.count(l) - ransomNote.count(l) < 0:
                return False
        return True


#TODO implement the solutions brought by the video.
