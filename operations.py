
def calculation(s,a,b):
        if s == '+':
            result = (a+b)
        elif s == '-':
            result = (a-b)
        elif s == '*':
            result = (a*b)
        elif s == '/':
            if b==0:
                result = ("Деление на 0")
            else:
                result = (round(a/b, 2))
        elif s == '^':
            result = (a**b)

        return result