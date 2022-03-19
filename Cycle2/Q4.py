import random


class Box:
    def __init__(self, l, b=None, h=None):
        self.l = l
        self.b = l if not b else b
        self.h = l if not h else h

    def area(self):
        return self.l * self.b + self.l * self.h + self.b * self.h

    def volume(self):
        return self.l * self.b * self.h

    def __str__(self):
        return f"Box(l={self.l}, b={self.b}, h={self.h})"


if __name__ == "__main__":
    N = int(input("Enter N: "))
    min_, max_ = list(map(int, input("Enter measurement range: ").split()))
    boxes = []
    for i in range(N):
        l, b, h = (random.randint(min_, max_) for _ in range(3))
        boxes.append(Box(l, b, h))

    max_ratio = 0
    max_box = None
    for box in boxes:
        ratio = box.volume() / box.area()
        if ratio > max_ratio:
            max_ratio = ratio
            max_box = box

    print("Box with highest volume : area ratio:", max_box)
