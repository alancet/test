from pywebio.input import input, PASSWORD, FLOAT
from pywebio.output import put_text
put_text("hello こんにちは")
number = input("1.2 + 0.5 =", type=FLOAT, placeholder='計算結果を入力', required=True)


password = input("enter pass", type=PASSWORD, help_text="useless help doc")

put_text(f"1.2+0.5={number}")
put_text(f"pass is ={password}")
