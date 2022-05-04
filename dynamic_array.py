class DynamicArray(object):
    def __init__(self, capacity=10, grow_factor=1.2):
        self.__grow_factor = grow_factor
        self.__length = 0
        self.__capacity = capacity  # Initialize chunk size to 10
        self.__chunk = [None] * self.__capacity

    def add(self, element):
        # llq
        if element is not None and type(element) != int:
            raise Exception('Input data must be int or None')
        if self.__length == self.__capacity:
            new_chunk_size = int(self.__capacity * self.__grow_factor) \
                             - self.__capacity
            self.__chunk += [None] * new_chunk_size
            self.__capacity = self.__capacity + new_chunk_size
        self.__chunk[self.__length] = element
        self.__length += 1

    def set(self, pos, value):
        # llq
        if value is not None and type(value) != int:
            raise Exception('Input data must be int or None')
        if pos < 0 or pos >= self.__length:
            raise Exception('The location accessed is not in the array!')
        self.__chunk[pos] = value

    def remove(self, pos):
        # llq
        if pos < 0 or pos >= self.__length:
            raise Exception('The location accessed is not in the array!')
        self.__length -= 1
        while pos < self.__length:
            self.__chunk[pos] = self.__chunk[pos + 1]
            pos += 1

    def size(self):
        # llq
        return self.__length

    def member(self, value):
        # llq
        if value is not None and type(value) != int:
            raise Exception('Input data must be int or None')
        for k in self.__chunk:
            if value == k:
                return True
        return False

    def reverse(self):
        # llq
        left = 0
        right = self.__length - 1
        while left < right:
            t = self.__chunk[right]
            self.__chunk[right] = self.__chunk[left]
            self.__chunk[left] = t
            right -= 1
            left += 1

    def from_list(self, lst):
        # llq
        if lst is None:
            raise Exception('The input array is empty!')
        for k in lst:
            if k is not None and type(k) != int:
                raise Exception('Input data must be int or None')
        self.__length = len(lst)
        self.__capacity = self.__length + 10
        self.__chunk = lst + [None] * 10

    def to_list(self):
        # llq
        return [self.__chunk[i] for i in range(self.__length)]

    def filter(self, predicate):
        # wzm
        result = []
        for i in range(self.__length):
            if predicate(self.__chunk[i]):
                result.append(self.__chunk[i])
            else:
                i += 1
        return result

    def map(self, function, *iterables):
        # wzm
        if self.__length == 0:
            return
        i = 0
        min_len = 1e10
        for it in iterables:
            if min_len > len(it):
                min_len = len(it)
        length = self.__length
        if length > min_len:
            for pos in range(length - 1, min_len - 1, -1):
                self.remove(pos)
        if len(iterables) > 0:
            for args in zip(*iterables):
                if i < self.__length:
                    if self.__chunk[i] is None:
                        pass
                    else:
                        if None in args:
                            self.__chunk[i] = None
                        else:
                            self.__chunk[i] = function(self.__chunk[i], *args)
                    i += 1
                else:
                    break
        else:
            while i < self.__length:
                if self.__chunk[i] is None:
                    pass
                else:
                    self.__chunk[i] = function(self.__chunk[i])
                i += 1

    def reduce(self, function, initial=None):
        # wzm
        if self.__length == 0:
            raise Exception("The array length cannot be 0!")
        if self.__length == 1 and initial is None:
            return self.__chunk[0]
        if initial is None:
            value = 0
        else:
            value = initial
        for i in range(self.__length):
            value = function(value, self.__chunk[i])
        return value

    def __iter__(self):
        # wzm
        return DynamicArrayIterator(self.__chunk, self.__length)

    def __add__(self, other):
        # llq
        if type(other) != DynamicArray:
            raise Exception('The type of connection is not DynamicArray!')
        for k in other:
            self.add(k)
        return self


class DynamicArrayIterator(object):
    def __init__(self, lst, lng):
        self.__chunk = lst
        self.__length = lng
        self.__start_num = -1

    def __iter__(self):
        return self

    def __next__(self):
        # wzm
        self.__start_num += 1
        if self.__start_num >= self.__length:
            raise StopIteration()
        return self.__chunk[self.__start_num]
