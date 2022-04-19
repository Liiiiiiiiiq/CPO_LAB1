import unittest
import random
from hypothesis import given

import hypothesis.strategies as st

from dynamic_array import DynamicArray
from functools import reduce


class TestDynamicArray(unittest.TestCase):

    @given(st.lists(st.integers()), st.integers())
    def test_add(self, a, k):
        # llq
        b = DynamicArray()
        b.from_list(a)
        b.add(k)
        self.assertEqual(b.to_list(), a + [k])

    def test_add_none(self):
        # llq
        a = [1, 4, 4, None]
        b = DynamicArray()
        b.from_list([1, 4, 4])
        b.add(None)
        self.assertEqual(b.to_list(), a)

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

    def test_set_none(self):
        # llq
        a = [1, None, 5]
        b = DynamicArray()
        b.from_list([1, 4, 5])
        b.set(1, None)
        self.assertEqual(b.to_list(), a)

    @given(st.lists(st.integers()))
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

    def test_member_none(self):
        # llq
        a = [1, None, 7]
        b = DynamicArray()
        b.from_list(a)
        self.assertTrue(b.member(None))

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

    @given(st.lists(st.integers()))
    def test_filter(self, a):
        # wzm
        arr = DynamicArray()
        arr.from_list(a)
        result = list(filter(lambda x: x % 2 == 0, a))
        self.assertEqual(arr.filter(lambda x: x % 2 == 0), result)
        result = list(filter(lambda x: x % 2 != 0, a))
        self.assertEqual(arr.filter(lambda x: x % 2 != 0), result)

    @given(st.lists(st.integers()),
           st.lists(st.integers()),
           st.lists(st.integers()))
    def test_map(self, a, b, c):
        # wzm
        arr0 = DynamicArray()
        arr0.from_list(a)
        result = list(map(lambda x: x ** 2, a))
        arr0.map(lambda x: x ** 2)
        self.assertEqual(arr0.to_list(), result)
        arr1 = DynamicArray()
        arr1.from_list(a)
        result = list(map(str, a))
        arr1.map(str)
        self.assertEqual(arr1.to_list(), result)
        arr2 = DynamicArray()
        arr2.from_list(a)
        result = list(map(lambda x, y: x + y, a, b))
        arr2.map(lambda x, y: x + y, b)
        self.assertEqual(arr2.to_list(), result)
        arr3 = DynamicArray()
        arr3.from_list(a)
        result = list(map(lambda x, y, z: x + y - z, a, b, c))
        arr3.map(lambda x, y, z: x + y - z, b, c)
        self.assertEqual(arr3.to_list(), result)

    def test_map_none(self):
        # wzm
        a = [1, 2, 3]
        arr_0 = DynamicArray()
        arr_0.from_list(a)
        c = [1, None, 9]
        d = [1, 2, None]
        arr_0.map(lambda x, y, z: x + y + z, c, d)
        self.assertEqual(arr_0.to_list(), [3, None, None])
        arr_1 = DynamicArray()
        arr_1.from_list(c)
        arr_1.map(lambda x: x ** 2)
        self.assertEqual(arr_1.to_list(), [1, None, 81])
        arr_2 = DynamicArray()
        arr_2.from_list(c)
        arr_2.map(lambda x, y: x + y, d)
        self.assertEqual(arr_2.to_list(), [2, None, None])

    @given(st.lists(st.integers()), st.integers())
    def test_reduce(self, a, b):
        # wzm
        arr = DynamicArray()
        arr.from_list(a)
        if len(a) == 0:
            with self.assertRaises(Exception):
                arr.reduce(lambda x, y: x + y)
        else:
            result = reduce(lambda x, y: x + y, a)
            self.assertEqual(arr.reduce(lambda x, y: x + y), result)
            result = reduce(lambda x, y: x + y, a, b)
            self.assertEqual(arr.reduce(lambda x, y: x + y, b), result)

    @given(st.lists(st.integers()))
    def test_iter(self, a):
        # wzm
        arr = DynamicArray()
        arr.from_list(a)
        temp = []
        for elem in arr:
            temp.append(elem)
        self.assertEqual(temp, a)
        self.assertEqual(arr.to_list(), temp)
        i = iter(DynamicArray())
        with self.assertRaises(StopIteration):
            next(i)

    @given(st.lists(st.integers()),
           st.lists(st.integers()),
           st.lists(st.integers()))
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
