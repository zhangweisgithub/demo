"""
参考：
https://www.bilibili.com/video/BV1U4411j7xb?from=search&seid=3388872340225112052
官方文档：
https://docs.python.org/3/library/argparse.html#default
添加互斥组的时候， 两个参数只能选择其中的一个参数作为输入
verbose： 冗余的
"""

import math
import argparse
parse = argparse.ArgumentParser(description="Calculate volume of Cylinder")
parse.add_argument("-r", "--radius", type=int, metavar="", required=True, help="Radius of Cylinder")
parse.add_argument("-H", "--height", type=int, metavar="", required=True, help="Height of Cylinder")
group = parse.add_mutually_exclusive_group()
group.add_argument("-q", "--quiet", action="store_true", help="print quiet")
group.add_argument("-v", "--verbose", action="store_true", help="print verbose")
args = parse.parse_args()

def cylinder_volume(radius, height):
    vol = math.pi * radius**2 * height
    return vol


if __name__ == "__main__":
    volume = cylinder_volume(args.radius, args.height)
    if args.quiet:
        print(volume)
    elif args.verbose:
        print("Volume of a Cylinder with radius %s and height %s if %s" % (args.radius, args.height, volume))
    else:
        print("Volume of Cylinder = %s" % volume)




# python3 case1.py -h
"""
usage: case1.py [-h] -r  -H  [-q | -v]

Calculate volume of Cylinder

optional arguments:
  -h, --help      show this help message and exit
  -r , --radius   Radius of Cylinder
  -H , --height   Height of Cylinder
  -q, --quiet     print quiet
  -v, --verbose   print verbose
"""

# python3 case1.py -r 2 -H 5 -v
"""
Volume of a Cylinder with radius 2 and height 5 if 62.83185307179586
"""

