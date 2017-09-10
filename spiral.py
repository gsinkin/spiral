import argparse


def print_result(result):
    for row in result:
        print "".join(row)


def make_spiral(height, width):
    assert height >= 4
    assert width >= 4
    result = []
    for _ in range(height):
        result.append([" "] * width)
    x_dir = 1
    y_dir = 0
    have_next = True
    x_pos = 0
    y_pos = 0
    y_min = 2
    y_max = height - 1
    x_min = 0
    x_max = width - 1
    while have_next:
        current_value = result[y_pos][x_pos]
        if current_value == " ":
            result[y_pos][x_pos] = "X"
        x_pos += x_dir
        y_pos += y_dir
        if y_pos > y_max and y_dir == 1:
            y_dir = 0
            x_dir = -1
            y_pos = y_max
            y_max -= 2
            # Fixed
            have_next = x_pos >= x_min and y_pos >= y_min
        elif y_pos < y_min and y_dir == -1:
            y_dir = 0
            x_dir = 1
            y_pos = y_min
            y_min += 2
            # Fixed
            have_next = x_pos <= x_max and y_pos <= y_max
        if x_pos > x_max and x_dir == 1:
            x_dir = 0
            y_dir = 1
            x_pos = x_max
            x_max -= 2
            # Fixed
            have_next = y_pos <= y_max and x_pos >= x_min
        elif x_pos < x_min and x_dir == -1:
            x_dir = 0
            y_dir = -1
            x_pos = x_min
            x_min += 2
            # Fixed
            have_next = y_pos >= y_min and x_pos <= x_max

    print_result(result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Draw a spiral.')
    parser.add_argument('--width', default=4, type=int, help='Spiral columns')
    parser.add_argument('--height', default=4, type=int, help='Spiral rows')
    args = parser.parse_args()
    make_spiral(args.height, args.width)
