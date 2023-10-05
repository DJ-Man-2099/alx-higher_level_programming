#!/usr/bin/python3
def main(add):
    a = 1
    b = 2
    c = add(a, b)
    print(f"{a:d} + {b:d} = {c:d}")


if __name__ == "__main__":
    import add_0
    main(add_0.add)
