def solution(phone_book):
    pb = sorted(phone_book)
    for p1, p2 in zip(pb, pb[1:]):
        if p2.startswith(p1):
            return False
    return True