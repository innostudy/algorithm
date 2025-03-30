def solution(chicken):
    coupon = chicken
    t_chicken = 0
    while coupon >= 10:
        s_chicken = coupon//10
        r_coupon = coupon % 10
        n_coupon = s_chicken
        coupon = r_coupon + n_coupon
        t_chicken += s_chicken

    return t_chicken
