#!/usr/bin/python

import sys
import re
import subprocess

if len(sys.argv) != 2:
    sys.exit("Missing filename!")
else:
    movie_file = sys.argv[1]

def callQnapi():
    subprocess.call(["qnapi",sys.argv[1]])

def getFilename(movie_file):
    match_filename = re.match(r'(.*)\.', movie_file)
    txt_filename = match_filename.group(1)
    return txt_filename

def main():
    callQnapi()
    with open('.'.join([getFilename(movie_file),'txt']), 'r') as input_txt:
        encoded_filename = '.'.join([getFilename(movie_file),'encoded','txt'])
        with open(encoded_filename, 'w') as output_txt:
            for line in input_txt.readlines():
                output_txt.write(line.decode('windows-1250').encode('utf-8'))
    print "Done!"

if __name__ == "__main__":
    main()
