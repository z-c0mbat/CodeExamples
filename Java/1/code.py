def bouncing_ball(h, bounce, window):
    if h > 0 and 0 < bounce < 1 and window < h:
        res = 1
        h *= bounce
        while h > window:
            res += 2
            h *= bounce
        return res
    return -1
