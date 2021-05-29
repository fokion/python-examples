import sys
import time


class AnimatedBlock:
    indent = 0
    indentIncreasing = True
    MAX_INDENT = None

    def __init__(self, val):
        self.MAX_INDENT = val

    def next_frame(self):
        value = ""
        for i in range(self.indent):
            value += " "
        print(value, "*********", "")
        if self.indentIncreasing:
            self.indent += 1
            if self.indent >= self.MAX_INDENT:
                self.indentIncreasing = False
        else:
            self.indent -= 1
            if self.indent <= 0:
                self.indentIncreasing = True


def main():
    block = AnimatedBlock(30)
    try:
        while True:
            block.next_frame()
            time.sleep(0.1)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
