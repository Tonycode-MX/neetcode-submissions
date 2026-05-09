class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for token in tokens:
            if token == "+":
                num1 = res.pop()
                num2 = res.pop()
                res.append(num2+num1)
            elif token == "-":
                num1 = res.pop()
                num2 = res.pop()
                res.append(num2-num1)
            elif token == "*":
                num1 = res.pop()
                num2 = res.pop()
                res.append(num2*num1)
            elif token == "/":
                num1 = res.pop()
                num2 = res.pop()
                res.append(int(num2/num1))
            else:
                res.append(int(token))

        return res[0]







        