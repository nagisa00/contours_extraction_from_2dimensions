#Reference web page
#https://matsu7874.hatenablog.com/entry/2018/12/17/025713
#2019/4/27 access

def det(p, q):
    return p[0]*q[1] - p[1]*q[0]


def sub(p, q):
    return (p[0]-q[0], p[1]-q[1])


def get_convex_hull(points):
    # どの3点も直線上に並んでいないと仮定する。
    n = len(points)
    points.sort()
    size_convex_hull = 0
    ch = []
    for i in range(n):
        while size_convex_hull > 1:
            v_cur = sub(ch[-1], ch[-2])
            v_new = sub(points[i], ch[-2])
            if det(v_cur, v_new) > 0:
                break
            size_convex_hull -= 1
            ch.pop()
        ch.append(points[i])
        size_convex_hull += 1

    t = size_convex_hull
    for i in range(n-2, -1, -1):
        while size_convex_hull > t:
            v_cur = sub(ch[-1], ch[-2])
            v_new = sub(points[i], ch[-2])
            if det(v_cur, v_new) > 0:
                break
            size_convex_hull -= 1
            ch.pop()
        ch.append(points[i])
        size_convex_hull += 1

    return ch[:-1]
