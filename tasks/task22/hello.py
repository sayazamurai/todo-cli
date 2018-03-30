import fire


def hello(name):
    print(f"Hello, {name}")


def bye(name):
    print(f"Bye, {name}")


if __name__ == "__main__":
    fire.Fire()

# sexy呪文
# if __name__ == "__main__":
#    fire.Fire()
# ...定義した関数をterminalのコマンドラインで使える！
#
# terminalで
# python3.6 hello.py hello saya
#(python3.6 ファイル名　関数名　変数の値)
# を実行すると
# 関数hello(saya)が実行される
# =>
# Hello, saya
#
# python3.6 hello.py bye vic
# =>
# Bye, vic
