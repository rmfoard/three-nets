import sys


def find_all(seq, pat):
    """Return a list of indexes of all non-overlapping substrings in 'seq' that match 'pat'.
    """
    assert len(seq) >= len(pat)

    match_xs = []
    seq_x = 0
    while seq_x < len(seq) - len(pat):
        pat_x = 0
        while pat_x < len(pat) and seq[seq_x + pat_x] == pat[pat_x]:
            pat_x += 1
        if pat_x == len(pat):
            match_xs.append(seq_x)
            seq_x += len(pat)
        else:
            seq_x += 1

    return match_xs


def main():
    print(f'main  v0.0  19Mar2023')

    if len(sys.argv) != 3:
        print(f'usage: {sys.argv[0]} <sequence> <pattern>')
    elif len(sys.argv[2]) > len(sys.argv[1]):
        print(f'<sequence> length must be greater than or equal to <pattern> length.')
    else:
        return find_all(sys.argv[1], sys.argv[2])

    return '*error*'


if __name__ == '__main__':
    print(main())
