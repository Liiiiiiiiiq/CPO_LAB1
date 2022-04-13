class DynamicArray(object):
    def __init__(self, grow_factor=1.2):
        self.__grow_factor = grow_factor
        self.__length = 0
        self.__capacity = 10  # Initialize chunk size to 10
        self.__chunk = [None] * self.__capacity

    def add(self, element):
        # llq
        if self.__length == self.__capacity:
            self.__capacity = int(self.__capacity * self.__grow_factor)
            new_chunk = [None] * self.__capacity
            for i, k in enumerate(self.__chunk):
                new_chunk[i] = k
            self.__chunk = new_chunk
        self.__chunk[self.__length] = element
        self.__length += 1

    def set(self, pos, value):
        # llq
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
            self.add(k)

    def to_list(self):
        # llq
        res = []
        for i in range(self.__length):
            res.append(self.__chunk[i])
        return res

    def filter(self, predicate):
        # wzm
        result = []
        for i in range(self.__length):
            if not predicate(self.__chunk[i]):
                result.append(self.__chunk[i])
            else:
                i += 1
        return result

    def map(self, function):
        # wzm
        result = [None] * self.__length
        i = 0
        while i < self.__length:
            result[i] = function(self.__chunk[i])
            i += 1
        return result

    def reduce(self, function, initializer=None):
        # wzm
        if self.__length == 0:
            raise Exception("The array length cannot be 0!")
        if self.__length == 1 and initializer is None:
            return self.__chunk[0]
        if initializer is None:
            value = 0
        else:
            value = initializer
        for i in range(self.__length):
            value = function(value, self.__chunk[i])
        return value

    def __iter__(self):
        # wzm
        self.__start_num = -1
        return self

    def __next__(self):
        # wzm
        self.__start_num += 1
        if self.__start_num >= self.__length:
            raise StopIteration()
        return self.__chunk[self.__start_num]

    def __add__(self, other):
        # llq
        if type(other) != DynamicArray:
            raise Exception('The type of connection is not DynamicArray!')
        lst_other = other.to_list()
        res = DynamicArray()
        res.from_list(self.to_list())
        for k in lst_other:
            res.add(k)
        return res
