import unittest
import random
from hypothesis import given

import hypothesis.strategies as st

from dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):

    @given(st.lists(st.integers()), st.integers())
    def test_add(self, a, k):
        # llq
        b = DynamicArray()
        b.from_list(a)
        b.add(k)
        self.assertEqual(b.to_list(), a + [k])

    @given(st.lists(st.integers()), st.integers())
    def test_set(self, a, k):
        # llq
        if len(a) == 0:
            return
        b = DynamicArray()
        b.from_list(a)
        pos = random.randint(0, len(a) - 1)
        b.set(pos, k)
        a[pos] = k
        self.assertEqual(b.to_list(), a)

    @given(st.lists(st.integers()), st.integers())
    def test_remove(self, a):
        # llq
        if len(a) == 0:
            return
        b = DynamicArray()
        b.from_list(a)
        pos = random.randint(0, len(a) - 1)
        b.remove(pos)
        a.pop(pos)
        self.assertEqual(b.to_list(), a)

    @given(st.lists(st.integers()))
    def test_size(self, a):
        # llq
        b = DynamicArray()
        b.from_list(a)
        self.assertEqual(b.size(), len(a))

    @given(st.lists(st.integers()))
    def test_member(self, a):
        # llq
        if len(a) == 0:
            return
        b = DynamicArray()
        b.from_list(a)
        k = random.randint(min(a), max(a))
        self.assertEqual(b.member(k), k in a)

    @given(st.lists(st.integers()))
    def test_reverse(self, a):
        # llq
        b = DynamicArray()
        b.from_list(a)
        b.reverse()
        a.reverse()
        self.assertEqual(b.to_list(), a)

    @given(st.lists(st.integers()))
    def test_from_list_to_list_equality(self, a):
        # llq
        b = DynamicArray()
        b.from_list(a)
        self.assertEqual(b.to_list(), a)

    def test_filter(self):
        # wzm
        arr = DynamicArray()
        arr.from_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(arr.filter(lambda x: x % 2 == 0), [1, 3, 5])
        self.assertEqual(arr.filter(lambda x: x % 2 != 0), [2, 4, 6])

    def test_map(self):
        # wzm
        arr = DynamicArray()
        arr.from_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(arr.map(lambda x: x ** 2), [1, 4, 9, 16, 25, 36])
        self.assertEqual(arr.map(str), ['1', '2', '3', '4', '5', '6'])

    def test_reduce(self):
        # wzm
        arr0 = DynamicArray()
        with self.assertRaises(Exception):
            arr0.reduce(lambda x, y: x + y)
        arr1 = DynamicArray()
        arr1.add(7)
        self.assertEqual(arr1.reduce(lambda x, y: x + y), 7)
        self.assertEqual(arr1.reduce(lambda x, y: x + y, initializer=3), 10)
        arr2 = DynamicArray()
        arr2.from_list([1, 2, 3, 4, 5, 6])
        self.assertEqual(arr2.reduce(lambda x, y: x + y), 21)
        self.assertEqual(arr2.reduce(lambda x, y: x + y, initializer=3), 24)

    def test_iter(self):
        # wzm
        x = [1, 2, 3, 4, 5, 6]
        arr = DynamicArray()
        arr.from_list(x)
        temp = []
        for elem in arr:
            temp.append(elem)
        self.assertEqual(temp, x)
        self.assertEqual(arr.to_list(), temp)
        i = iter(DynamicArray())
        with self.assertRaises(StopIteration):
            next(i)

    @given(st.lists(st.integers()), st.lists(st.integers()), st.lists(st.integers()))
    def test_monoid(self, a, b, c):
        # llq
        da = DynamicArray()
        db = DynamicArray()
        dc = DynamicArray()
        da.from_list(a)
        db.from_list(b)
        dc.from_list(c)
        # test Associativity
        t0 = (da + db) + dc
        t1 = da + (db + dc)
        self.assertEqual(t0.to_list(), t1.to_list())
        # test Identity element
        dd = DynamicArray()
        t2 = da + dd
        t3 = dd + da
        self.assertEqual(t2.to_list(), t3.to_list())
        self.assertEqual(t2.to_list(), da.to_list())
        self.assertEqual(t3.to_list(), da.to_list())
