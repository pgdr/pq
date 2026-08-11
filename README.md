# pq

Can you implement a priority queue without mistakes on the first attempt?

```python
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
    e = q[1]
    q[1] = q[len(q) - 1]
    del q[len(q) - 1]
    _bubble_down(q, 1)
    return q, e
```

The answer is no.
