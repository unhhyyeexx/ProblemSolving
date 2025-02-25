import sys

def solution():

    def postorder(order):
        if not order:
            return
        nonlocal idx, res
        temp = preorder[idx]
        left, right = order.split(preorder[idx])
        idx += 1
        postorder(left)
        postorder(right)
        res += temp

    cases = sys.stdin.readlines()
    for case in cases:
        preorder, inorder = case.split()
        idx = 0
        res = ''
        postorder(inorder)
        print(res)

solution()