"""Fibo"""
def main(num):
    """This is function main"""
    print(recur(num))
def recur(number):
    """This is function recursion"""
    if number == 1 or number == 0:
        return number
    else:
        check = recur(max(number - 1, 0))+recur(max(number - 2, 0))
        return check
main(int(input()))
"""hahahaa"""
