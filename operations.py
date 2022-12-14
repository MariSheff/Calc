
def calculation(s,a,b):
        if s == '+':
            result = (a+b)
        elif s == '-':
            result = (a-b)
        elif s == '*':
            result = (a*b)
        elif s == '/':
            try:
                result = (round(a/b, 2))
            except ZeroDivisionError:
                result = ("Деление на 0")
        elif s == '^':
            result = (a**b)

        return result
