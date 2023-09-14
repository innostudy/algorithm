def solution(chicken):
    total = 0
    while chicken >= 10:
        quotient,remainder = divmod(chicken,10)
        total = total + quotient;
        chicken = remainder + quotient;
    return total