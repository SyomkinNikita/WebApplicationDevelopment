from OOP.Circle import Circle
from OOP.Rectangle import Rectangle
from OOP.Square import Square


def main():
    r = Rectangle("red", 3, 1)
    c = Circle("blue", 5)
    s = Square("black", 10)

    print(r)
    print(c)
    print(s)


if __name__ == "__main__":
    main()
