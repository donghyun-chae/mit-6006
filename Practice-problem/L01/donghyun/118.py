#!/usr/bin/env python3

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        def pascal_list(n):
            if n == 1:
                return [[1]]
            if n == 2:
                return [[1], [1,1]]

            result = pascal_list(n-1)
            prev_row = result[-1]
            new_row = [1]

            for i in range(len(prev_row)-1):
                new_row.append(prev_row[i] + prev_row[i+1])

            new_row.append(1)
            result.append(new_row)
            return result

        if numRows == 0:
            return []
        return pascal_list(numRows)
