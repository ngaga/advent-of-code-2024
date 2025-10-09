a = [3,
4,
2,
1,
3,
3]


b = [
   4,
   3,
   5,
   3,
   9,
   3]

# TODO efficiency? with numpy? bench?
def sortedDistance(a, b):
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    print(a_sorted)
    print(b_sorted)
    distances = [abs(a_i - b_i) for (a_i, b_i) in zip(a_sorted, b_sorted)]
    print(distances)
    return sum(e for e in distances)


print(sortedDistance(a, b))
