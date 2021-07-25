test: int = 12
test2: bool = True
test3:str = 'hello'
test4 : float = 1.12

test = 'hello'
print(test)


val_e: dict[str, int] = {'size':12, 'age':24}
val_f: list[str] = ['taro', 'jiro']
val_g: tuple[str, int] = ('name', 12)

from typing import Final
TABLE_NAME: Final[str] = 'sample'

TABLE_NAME = "hoge"