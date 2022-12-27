
class Calc():
    def add_num(x, y):
        return x + y

    def sub_num(x, y):
        return x - y

    def four_arithmetic_operations(x, y, action=None):
        # 加算
        if action == "add":
            return x + y
        # 減算
        elif action == "sub":
            return x - y
        # 掛け算
        elif action == "mul":
            return x * y
        # 割り算
        elif action == "div":
            return x / y
        # 例外
        else:
            raise ValueError("四則演算以外の操作です")
