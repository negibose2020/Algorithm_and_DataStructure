"""Modint

・つかい方
mint = Modint(998244353)
value = mint(10)

https://qiita.com/hyouchun/items/4024845d6783c8dacc77
"""

class Modint():
    def __init__(self, mod: int):
        self.mod: int = mod

    def __call__(self, num: int):
        return NumberMint(num, self.mod)


class NumberMint():
    def __init__(self, num: int, mod: int):
        self.num: int = num
        self.mod: int = mod
        if self.num < 0 or self.mod <= self.num:
            self.num %= self.mod
        self.__inverse = None  # 逆数

    def __int__(self) -> int:
        return self.num

    def __str__(self) -> str:
        return str(self.num)

    def __repr__(self) -> str:
        return "Modint({})".format(self.num)

    def __add__(self, other):
        if isinstance(other, NumberMint):
            new_value = self.num + other.num
        else:
            new_value = self.num + other
        if self.mod <= new_value:
            new_value -= self.mod
        return NumberMint(new_value, self.mod)

    def __sub__(self, other):
        if isinstance(other, NumberMint):
            new_value = self.num - other.num
        else:
            new_value = self.num - other
        if new_value < 0:
            new_value += self.mod
        return NumberMint(new_value, self.mod)

    def __mul__(self, other):
        if isinstance(other, NumberMint):
            new_value = self.num * other.num % self.mod
        else:
            new_value = other % self.mod * self.num % self.mod
        return NumberMint(new_value, self.mod)

    def __truediv__(self, other):
        if isinstance(other, NumberMint):
            new_value = self.num * other.inverse % self.mod
        else:
            other_inverse = pow(other, self.mod - 2, self.mod)
            new_value = self.num * other_inverse % self.mod
        return NumberMint(new_value, self.mod)

    def __floordiv__(self, other):
        return self / other

    def __pow__(self, power):
        return pow(self.num, power, self.mod)

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def __itruediv__(self, other):
        return self / other

    def __ifloordiv__(self, other):
        return self / other

    def __radd__(self, other):
        return self + other

    def __rsub__(self, other):
        return NumberMint(other, self.mod) - self

    def __rmul__(self, other):
        return self * other

    def __rtruediv__(self, other):
        return NumberMint(other, self.mod) / self

    def __rfloordiv__(self, other):
        return NumberMint(other, self.mod) / self

    def __eq__(self, other) -> bool:
        if isinstance(other, NumberMint):
            return self.num == other.num
        return self.num == other % self.mod

    def __ne__(self, other) -> bool:
        if isinstance(other, NumberMint):
            return self.num != other.num
        return self.num != other % self.mod

    def __inverse_generator(self):
        return pow(self.num, self.mod - 2, self.mod)

    @property
    def inverse(self) -> int:
        if self.__inverse is None:
            self.__inverse = self.__inverse_generator()
        return self.__inverse