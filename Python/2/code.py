from typing import List , Tuple
import math

Point = Tuple[float , float]


def distance(a: Point , b: Point):
    """Finds the distance between two points"""
    return math.hypot(a[0] - b[0] , a[1] - b[1])


def search(p , n):
    min_val = float('inf')
    min_a = (0 , 0)
    min_b = (0 , 0)
    for i in range(n):
        for j in range(i + 1 , n):
            if distance(p[i] , p[j]) < min_val:
                min_val = distance(p[i] , p[j])
                min_a , min_b = p[i] , p[j]
    return min_val , min_a , min_b


def find_closest(points):
    n = len(points)

    if n <= 3:
        return search(points , n)[0]

    points_l = [points[x] for x in range(0 , n // 2)]
    points_r = [points[x] for x in range(n // 2 , n)]

    dl = find_closest(points_l)
    dr = find_closest(points_r)

    d = min(dl , dr)
    return d


def corridor(points , mid_point , min_d):
    new_points = []
    for i in range(0 , len(points)):
        if mid_point[0] - min_d <= points[i][0] <= mid_point[0] + min_d:
            new_points.append(points[i])
        else:
            if points[i][0] > mid_point[0] + min_d:
                break
    points = sorted(new_points , key=lambda y: y[1])
    res = search(points , len(points))
    return res


def closest_pair_of_points(points: List[Point]) \
        -> Tuple[float , Point , Point]:
    """Finds the closest pair of points in the list"""
    points = sorted(points , key=lambda x: x[0])
    mid = len(points) // 2
    mid_point = points[mid]
    if len(points) > 3:
        min_d = find_closest(points)
        new_d = corridor(points , mid_point , min_d)
        return new_d
    else:
        return search(points , len(points))
