class Solution:

    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        # code here
        stack = []

        for i in range(n):
            stack.append(i)

        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()

            if M[a][b] == 1:
                stack.append(b)
            else:
                stack.append(a)

        celeb = stack.pop()  # possible celebrity

        for i in range(n):
            if celeb != i:
                if M[celeb][i] == 1 or M[i][celeb] == 0:
                    return -1

        return celeb