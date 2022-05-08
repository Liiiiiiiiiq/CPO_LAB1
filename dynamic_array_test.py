import unittest
import random
from hypothesis import given

import hypothesis.strategies as st

from dynamic_array import DynamicArray
from functools import reduce


class TestDynamicArray(unittest.TestCase):

    def test_add(self):
        # llq
        a = [1, 4, 4, None]
        b = DynamicArray()
        b.from_list([1, 4, 4])
        b.add(None)
        self.assertEqual(b.to_list(), a)
        b.add(44)
        self.assertEqual(b.to_list(), [1, 4, 4, None, 44])

    def test_set(self):
        # llq
        a = [1, None, 5]
        b = DynamicArray()
        b.from_list([1, 4, 5])
        b.set(1, None)
        self.assertEqual(b.to_list(), a)
        b.set(2, 44)
        self.assertEqual(b.to_list(), [1, None, 44])

    def test_remove(self):
        # llq
        a = [3, 5, 6, 3, 2]
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

    def test_member(self):
        # llq
        a = [1, None, 7]
        b = DynamicArray()
        b.from_list(a)
        self.assertTrue(b.member(None))
        self.assertTrue(b.member(1))

    def test_reverse(self):
        # llq
        a = [3, 4, 1, 3, 4, 5, 6]
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
        arr.filter(lambda x: x % 2 == 0)
        self.assertEqual(arr.to_list(), result)
        arr1 = DynamicArray()
        arr1.from_list(a)
        result = list(filter(lambda x: x % 2 != 0, a))
        arr1.filter(lambda x: x % 2 != 0)
        self.assertEqual(arr1.to_list(), result)

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
        arr0 = DynamicArray()
        arr0.from_list(a)
        arr1 = DynamicArray()
        arr1.from_list(b)
        result = list(map(lambda x, y: x + y, a, b))
        arr0.map(lambda x, y: x + y, arr1)
        self.assertEqual(arr0.to_list(), result)
        arr0 = DynamicArray()
        arr0.from_list(a)
        arr2 = DynamicArray()
        arr2.from_list(c)
        result = list(map(lambda x, y, z: x + y - z, a, b, c))
        arr0.map(lambda x, y, z: x + y - z, arr1, arr2)
        self.assertEqual(arr0.to_list(), result)
        a = [1, 2, 3]
        arr_0 = DynamicArray()
        arr_0.from_list(a)
        b = [1, None, 9]
        arr_1 = DynamicArray()
        arr_1.from_list(b)
        with self.assertRaises(TypeError):
            arr_0.map(lambda x, y: x + y, arr_1)

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
        da0 = DynamicArray()
        da1 = DynamicArray()
        db = DynamicArray()
        dc = DynamicArray()
        da0.from_list(a)
        da1.from_list(a)
        db.from_list(b)
        dc.from_list(c)
        # test Associativity
        da0 += db
        da0 += dc  # (a + b) + c
        db += dc
        da1 += db  # a + (b + c)
        self.assertEqual(da0.to_list(), da1.to_list())
        # test Identity element
        dd = DynamicArray()
        da2 = DynamicArray()
        da2.from_list(a)
        da2 += dd
        dd += da2
        self.assertEqual(dd.to_list(), da2.to_list())
