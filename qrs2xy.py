import math
import sys

def main():
    if len(sys.argv) != 4:
        print(f'Please use {sys.argv[0]} <q> <r> <s>')
        sys.exit(1)

    q = float(sys.argv[1])
    r = float(sys.argv[2])
    s = float(sys.argv[3])

    root3_2 = math.sqrt(3) / 2.0
    scale = 1.0

    x = scale * (r + q/2.0 + s/2.0)
    y = scale * (q * root3_2 - s * root3_2)

    x2 = r * 1.5 + q
    y2 = r * root3_2

    print(f'x, x2: {x} ? {x2}')
    print(f'y, y2: {y} ? {y2}')

    print(f'(q, r, s) = ({q}, {r}, {s}) ==> (x, y) = ({x}, {y})')


if __name__ == '__main__':
    main()
