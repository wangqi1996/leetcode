class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        len_word = len(word)
        len_1, len_2 = len(board), len(board[0])
        visited = [[False for _ in range(len_2)] for _ in range(len_1)]

        def backtrack(i, j, index):
            if index == len_word:
                return True
            visited[i][j] = True

            def condition(a, b):
                return not visited[a][b] and board[a][b] == word[index] and backtrack(a, b, index + 1)

            if i > 0 and condition(i - 1, j):
                return True
            if i < len_1 - 1 and condition(i + 1, j):
                return True
            if j > 0 and condition(i, j - 1):
                return True
            if j < len_2 - 1 and condition(i, j + 1):
                return True

            visited[i][j] = False
            return False

        for i in range(len_1):
            for j in range(len_2):
                if board[i][j] == word[0] and backtrack(i, j, 1):
                    return True

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    # print(Solution().exist(board, "ACCE"))
    a = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    print(Solution().exist(a, "AAB"))
