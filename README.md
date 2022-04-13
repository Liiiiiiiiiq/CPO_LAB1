# CPO_LW - lab 1 - variant 1

In lab 1, *Mutable Algorithms and Data Structure Implementation*, our 
variant 1 aims to implement dynamic array using Python.

## Project structure

- `dynamic_array.py` -- implementation of `DynamicArray` class with `add`,
 `set`,`remove`,`filter`,`map` and other features.

- `dynamic_array_test.py` -- unit and PBT tests for `DynamicArray`.

## Features

- add(elem): Add a new element to the end of array. If `capacity == length`,
it will allocate a new chunk of memory by user-specified growing factor.
- set(pos, elem): Set an element with specific index.
- remove(pos): Remove an element by index.
- size(): Return the length of array.
- member(elem): Return a boolean indicating whether the element is a member of the array.
- reverse(): reverse the array.
- from_list(list): Conversion from built-in `list`.
- to_list(): Conversion to built-in `list`.
- filter(pre): Filter data structure by specific predicate.
- map(fun): Map elements of the array by specific function.
- reduce(fun): Process elements of the array to build a return value by specific function.
- \__iter\__ and \__next\__: Implementation of iterator in Python style.
- \__add\__: Operator `+` overloading, implement two arrays concatenate.

## Contribution

- Li Liquan (212320016@hdu.edu.cn)
  - GitHub repository created
  - Source code framework construction
  - implement features and tests: `add`, `set`, `remove`, `size`, `member`,
  `reverse`, `from_list`, `to_list`, `__add__`

- Wang Zimeng (1372178297@qq.com)
  - implement features and tests: `filter`, `map`, `reduce`, `__iter__`, `__next__`
  - write `README.md`

## Changelog

- 12.04.2022 23:05 - 3
  - Wang Zimeng uploaded `README.md`.
- 12.04.2022 23:00 - 2
  - Wang Zimeng uploaded codes that implement features and tests.
- 12.04.2022 18:50 - 1
  - Li Liquan uploaded codes that implement features.
- 12.04.2022 17:50 - 0
  - Initial

## Design notes

- ...
