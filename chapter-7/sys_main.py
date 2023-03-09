#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    args = sys.argv
    print(args, sum(map(int, args[1:])))
