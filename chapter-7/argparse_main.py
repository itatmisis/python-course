#!/usr/bin/env python3

import argparse
import sys

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Калькулятор!")
    parser.add_argument("--sum", action="store_true", help="складывает")
    parser.add_argument("--prod", action="store_true", help="умножает")
    parser.add_argument("operands", nargs="*", action="store", type=int, help="операнды")
    args = parser.parse_args()

    if args.sum:
        print(sum(args.operands))
        sys.exit()

    if args.prod:
        from functools import reduce

        result = reduce(lambda x, y: x * y, args.operands)
        print(result)
        sys.exit()
