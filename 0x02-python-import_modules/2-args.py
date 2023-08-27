#!usr/bin/python3

if__name__== '__main__':
    from sys import argv
    num = len(argv) -1
    if num == 0:
        print("{} argument".format(num)
                elif n = 1:
                print("{} argument:".format(num))
                print("1: {}".format(argv[1]))
                else:
                print("{} arguments:".format(n))
                x = 1
                for arg in argv[1:]:
                    print("{}: {}".format(x, arg))
                    x += 1
