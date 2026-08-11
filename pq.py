pq = lambda: [None]
left = lambda i: i * 2
right = lambda i: i * 2 + 1
parent = lambda i: i // 2
leaf = lambda q, i: left(i) >= len(q)


def _bubble_up(q, i):
    while parent(i) and q[parent(i)] > q[i]:
        q[parent(i)], q[i] = q[i], q[parent(i)]
        i = parent(i)


def _minchild(q, i):
    l = left(i)
    r = right(i)
    if r >= len(q):
        return l
    return l if q[l] < q[r] else r


def _bubble_down(q, i):
    while not leaf(q, i) and q[_minchild(q, i)] < q[i]:
        c = _minchild(q, i)
        q[c], q[i] = q[i], q[c]
        i = c


def insert(q, e):
    q.append(e)
    _bubble_up(q, len(q) - 1)


def pop(q):
    if len(q) == 1:
        raise IndexError("pop from empty priority queue")
    e = q[1]
    q[1] = q[len(q) - 1]
    del q[len(q) - 1]
    _bubble_down(q, 1)
    return q, e


if __name__ == "__main__":
    from random import randint as R

    N = 1000
    Q = pq()
    for _ in range(N):
        insert(Q, R(N * 10, N * 100 - 1))

    prev = 0
    for _ in range(N):
        Q, e = pop(Q)
        assert e >= prev, f"last pop = {prev}, this pop = {e}"
        prev = e
