import os.path
import sys

def main():
    f1 = input("Enter a source file: ").strip()
    f2 = input("Enter a target file: ").strip()

    if os.path.isfile(f2):
        print(f'{f2} already exist')
        sys.exit()

    infile = open(f1, 'r')
    outfile = open(f2, 'w')

    countLines = countChar = 0
    for line in infile:
        countLines += 1
        countChar += len(line)
        outfile.write(line)
    print(f"{countLines} lines and {countChar} char copied")

    infile.close()
    outfile.close()

main()
