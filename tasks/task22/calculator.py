import fire

# 関数の中でprintしなくても
# returnだけで結果が表示される


def add(x, y):
    return x + y


# =>terminalで
# python3.6 calculator.py add 10 20
# 30


def multiply(x, y):
    return x * y


# =>terminalで
# python3.6 calculator.py multiply 10 20
# 200

if __name__ == "__main__":
    fire.Fire()