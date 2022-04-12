class DynamicArray(object):
    def __init__(self, grow_factor):
        self.__grow_factor = grow_factor
        self.__length = 0
        self.__capacity = 10  # Initialize chunk size to 10
        self.__chunk = [None] * self.__capacity

    def add(self, element):
        if self.__length == self.__capacity:
            self.__capacity = self.__capacity * self.__grow_factor
            new_chunk = [None] * self.__capacity
            for i, k in enumerate(self.__chunk):
                new_chunk[i] = k
            self.__chunk = new_chunk
        self.__chunk[self.__length] = element
        self.__length += 1

    def set(self, pos, value):
        if pos < 0 or pos >= self.__length:
            raise Exception('The location accessed is not in the array!')
        self.__chunk[pos] = value

    def remove(self, value):
        for i, k in enumerate(self.__chunk):
            if k == value:
                self.__length -= 1
                while i < self.__length:
                    self.__chunk[i] = self.__chunk[i + 1]
                    i += 1
                return

    def size(self):
        return self.__length

    def member(self):
        # llq
        pass

    def reverse(self):
        # llq
        pass

    def from_list(self):
        # llq
        pass

    def to_list(self):
        # llq
        pass

    def filter(self):
        # wzm
        pass

    def map(self):
        # wzm
        pass

    def reduce(self):
        # wzm
        pass

    def __iter__(self):
        # wzm
        pass

    def __next__(self):
        # wzm
        pass

    def __add__(self, other):
        # llq
        pass
