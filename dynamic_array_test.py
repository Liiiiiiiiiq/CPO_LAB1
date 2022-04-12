import unittest

from hypothesis import given

import hypothesis.strategies as st

from dynamic_array import DynamicArray


class TestDynamicArray(unittest.TestCase):

    def test_add(self):
        # llq
        pass

    def test_set(self):
        # llq
        pass

    def test_remove(self):
        # llq
        pass

    def test_size(self):
        # llq
        pass

    def test_member(self):
        # llq
        pass

    def test_reverse(self):
        # llq
        pass

    def test_from_list_to_list_equality(self):
        # llq
        pass

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
        self.assertEqual(arr.map(lambda x: x**2), [1, 4, 9, 16, 25, 36])
        self.assertEqual(arr.map(str), ['1', '2', '3', '4', '5', '6'])

    def test_reduce(self):
        # wzm
        arr0 = DynamicArray()
        with self.assertRaises(Exception):
            arr0.reduce(lambda x, y: x+y)
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

    def test_monoid(self):
        # llq
        pass
