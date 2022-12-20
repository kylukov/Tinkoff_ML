import difflib
import argparse


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
