# namedtuple
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

Box = namedtuple('Box', ['x', 'y', 'z'])


# deque
from collections import deque

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素很慢，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
print('--deque--')
q = deque(['c', 'd', 'e'])
print(q)
q.append('f')
print(q)
q.appendleft('a')
print(q)
q.popleft()
print(q)


# defaultdict
from collections import defaultdict

print('--defaultdict--')
dd = defaultdict(lambda: 'N/A')
dd['a'] = 'aa'
print(dd['a'])
print(dd['b'])


# OrderedDict
from collections import OrderedDict

print('--OrderedDict--')
d = dict([('a', 1), ('c', 2), ('b', 3)])
print(d)
print(d.keys())
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
ood = OrderedDict()
ood['z'] = 'zz'
ood['y'] = 'yy'
ood['x'] = 'xx'
print(ood.keys())

# Counter
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
    print(c)