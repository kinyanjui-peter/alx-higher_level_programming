#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    x = dir(hidden_4)
        for counter in range(0, len(x)):
            if x[counter][0:2] != "__":
                print("{}".format(x[counter]))
