from typing import Any, Generator
from typing_extensions import LiteralString, Self

from sympy.core import Basic

class GrayCode(Basic):
    _skip = ...
    _current = ...
    _rank = ...
    def __new__(cls, n, *args, **kw_args) -> Self: ...
    def next(self, delta=...) -> GrayCode: ...
    @property
    def selections(self): ...
    @property
    def n(self) -> Basic: ...
    def generate_gray(self, **hints) -> Generator[str, Any, None]: ...
    def skip(self) -> None: ...
    @property
    def rank(self) -> int: ...
    @property
    def current(self) -> str: ...
    @classmethod
    def unrank(cls, n, rank) -> str: ...

def random_bitstring(n) -> str: ...
def gray_to_bin(bin_list) -> LiteralString: ...
def bin_to_gray(bin_list) -> LiteralString: ...
def get_subset_from_bitstring(super_set, bitstring) -> list[Any]: ...
def graycode_subsets(gray_code_set) -> Generator[list[Any], Any, None]: ...