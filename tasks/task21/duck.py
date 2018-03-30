class Duck:
    def __init__(self, something):
        self.x = something

    def say(self):
        print(f"Hello, I'm {self.x}")


# ↓この行を書くことで、他のファイルでDuckをimportした時に
# ifの中身が実行されない
# このファイルduck.pyを実行したときだけifの中身が実行される
# classの変数が何であってもif __name__ == "__main__":
if __name__ == "__main__":
    vic = Duck("vic")
    vic.say()

    gakky = Duck("gakky")
    gakky.say()
