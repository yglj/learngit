"""
背包问题
先解决子问题，再逐步解决大问题

"""
# 最长公共子序列


def public_seq(word_a, word_b):
    seq = ''
    cell = [[0 for a in range(len(word_b)+1)] for b in range(len(word_a)+1) ]
    for i in range(1, len(word_a)+1):
        for j in range(1, len(word_b)+1):
            if word_a[i-1] == word_b[j-1]:
                cell[i][j] = cell[i-1][j-1] + 1
            else:
                if cell[i][j-1] > cell[i-1][j]:
                    cell[i][j] = cell[i][j-1]
                else:
                    cell[i][j] = cell[i-1][j]
    print(cell)
    print(seq)

if __name__ == '__main__':
    public_seq('accomplish', 'action')
