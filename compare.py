import difflib
import argparse

"""
def levenstein_distance(str_1, str_2):
    n, m = len(str_1), len(str_2)
    if n > m:
        str_1, str_2 = str_2, str_1
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if str_1[j - 1] != str_2[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]
"""

def similarity(s1, s2):
    normalized1 = s1.lower()
    normalized2 = s2.lower()
    matcher = difflib.SequenceMatcher(None, normalized1, normalized2)
    return matcher.ratio()


def get_content(path):
    f = open(path, 'r')
    tmp = ''
    for line in f:
        if (line != '\n') and (not '"""' in line) and (not '#' in line):
            tmp += str(line)
    return tmp


def main():
    parser = argparse.ArgumentParser(description='Videos to images')
    parser.add_argument('indir', type=str, help='Input dir for videos')
    parser.add_argument('outdir', type=str, help='Output dir for image')
    args = parser.parse_args()
    f = open(args.indir, 'r')
    result_file = open(args.outdir, '+w')
    for line in f:
        paths = line.split()
        result = str(round(similarity(get_content(paths[0]), get_content(paths[1])), 2))
        result_file.write(result + '\n')

    result_file.close()


if __name__ == '__main__':
    main()
