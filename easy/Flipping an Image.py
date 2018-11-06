class Solution(object):
    def flipAndInvertImage(self, A):
        temp = []
        output = []
        for i in A:
            i.reverse()
        for i in A:
            for j in i:
                temp.append(1-j)
            output.append(temp)
            temp = []
        return output