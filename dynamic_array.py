from typing import Callable
from typing import Optional


class DynamicArrayIterator(object):
    """ An iterator object of DynamicArray. """

    def __init__(self, lst: list[Optional[int]], lng: int) -> None:
        self.__chunk = lst
        self.__length = lng
        self.__start_num = -1

    def __iter__(self) -> 'DynamicArrayIterator':
        """ Implement iter(self). """
        return self

    def __next__(self) -> Optional[int]:
        """ Implement next(self). """
        self.__start_num += 1
        if self.__start_num >= self.__length:
            raise StopIteration()
        return self.__chunk[self.__start_num]


class DynamicArray(object):
    """ Mutable dynamic array Implementation """

    def __init__(self, capacity: int = 10, grow_factor: float = 1.2):
        """Create an instance of DynamicArray

        :param capacity: a chunk of memory how many elements it can contain.
        :param grow_factor: when 'capacity == length' and  don’t have space
            for a new element, allocate a new chunk of memory according to
            grow_factor ([None]*(capacity * growth_factor)).
        """
        self.__grow_factor = grow_factor
        self.__length = 0
        self.__capacity = capacity  # Initialize chunk size to 10
        self.__chunk: list[Optional[int]] = [None] * self.__capacity

    def add(self, element: Optional[int]) -> None:
        """ Add an element at the end of the array.

        :param element: int or None.
        """
        if element is not None and type(element) != int:
            raise Exception('Input data must be int or None')
        if self.__length == self.__capacity:
            new_chunk_size = int(self.__capacity * self.__grow_factor) \
                             - self.__capacity
            self.__chunk += [None] * new_chunk_size
            self.__capacity = self.__capacity + new_chunk_size
        if element is None:
            pass
        else:
            self.__chunk[self.__length] = element
        self.__length += 1

    def set(self, pos: int, value: Optional[int]) -> None:
        """ Add an element into the array at specified position.

        :param pos: Index of the array.
        :param value: The value of element, int or None.
        """
        if value is not None and type(value) != int:
            raise Exception('Input data must be int or None')
        if pos < 0 or pos >= self.__length:
            raise Exception('The location accessed is not in the array!')
        self.__chunk[pos] = value

    def remove(self, pos: int) -> None:
        """ Remove an element of array at specified position.

        :param pos: Index of the array.
        """
        if pos < 0 or pos >= self.__length:
            raise Exception('The location accessed is not in the array!')
        self.__length -= 1
        while pos < self.__length:
            self.__chunk[pos] = self.__chunk[pos + 1]
            pos += 1

    def size(self) -> int:
        """ Return the length of array. """
        return self.__length

    def member(self, value: int) -> bool:
        """ Determines whether the given value is a member of the array.

        :param value: The given value.
        :return: Value is member if return True, else not.
        """
        if value is not None and type(value) != int:
            raise Exception('Input data must be int or None')
        for k in self.__chunk:
            if value == k:
                return True
        return False

    def reverse(self) -> None:
        """ Reverse the array. """
        left = 0
        right = self.__length - 1
        while left < right:
            t = self.__chunk[right]
            self.__chunk[right] = self.__chunk[left]
            self.__chunk[left] = t
            right -= 1
            left += 1

    def from_list(self, lst: list[Optional[int]]) -> None:
        """ Add elements from a list to the empty array. """
        if lst is None:
            raise Exception('The input array is empty!')
        for k in lst:
            if k is not None and type(k) != int:
                raise Exception('Input data must be int or None')
        self.__length = len(lst)
        self.__capacity = self.__length + 10
        self.__chunk = lst + [None] * 10

    def to_list(self) -> list[Optional[int]]:
        """ Transform the array to a list. """
        return [self.__chunk[i] for i in range(self.__length)]

    def filter(self, predicate: Callable[[Optional[int]], bool]) -> None:
        """ Filter the array by specific predicate. """
        for i in range(self.__length-1, -1, -1):
            if not predicate(self.__chunk[i]):
                self.remove(i)

    def map(self, function: Callable[..., int],
            *iters: tuple['DynamicArray', ...]) -> None:
        """ Applied function to every item of instances of DynamicArray,
         yielding the results. If additional instance arguments are passed,
         function must take that many arguments and is applied to the items
         from all instances in parallel. With multiple instances, the map
         stops when the shortest instance is exhausted.
         """
        if self.__length == 0:
            pass
        if len(iters) > 0:
            i = 0
            for args in zip(*iters):
                if i < self.__length:
                    self.__chunk[i] = function(self.__chunk[i], *args)
                    i += 1
            if i < self.__length:
                for j in range(self.__length-1, i-1, -1):
                    self.remove(j)
        else:
            for i in range(self.__length):
                self.__chunk[i] = function(self.__chunk[i])

    def reduce(self, function: Callable[[Optional[int], Optional[int]], int],
               initial: Optional[int] = None) -> Optional[int]:
        """ Apply function of two arguments cumulatively to the items of the
            array, from left to right, to reduce the array to a single value.

        :param function: Callable.
        :param initial: If the optional initializer is present, it is placed
            before the items of the array in the calculation, and serves as
            a default when the array is empty. If initializer is not given
            and array contains only one item, the first item is returned.
        """
        it = iter(self)
        if initial is None:
            try:
                value = next(it)
            except StopIteration:
                raise TypeError("reduce() of empty sequence with no "
                                "initial value") from None
        else:
            value = initial
        for element in it:
            value = function(value, element)
        return value

    def __iter__(self) -> 'DynamicArrayIterator':
        """ Return an iterator object. """
        return DynamicArrayIterator(self.__chunk, self.__length)

    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        """ Operator '+' overloading, concat self with
        other instance of DynamicArray. """
        if type(other) != DynamicArray:
            raise Exception('The type of concatenation is not DynamicArray!')
        for k in other:
            self.add(k)
        return self
