import cProfile
import collections
import re

def main():
    # KJV in plaintext can be found at http://printkjv.ifbweb.com/
    with open("/home/dehus/Downloads/AV1611Bible.txt", 'rU') as file:
        lines = file.readlines()

    reg = re.compile('[^a-zA-Z0-9 ]+')
    clean_lines = [reg.sub('', l.lower().strip()) for l in lines if l != "\n"]
    words = [item for l in clean_lines for item in l.split(' ')]
    words_counter = collections.Counter(words)
    print words_counter.most_common(10)

#main()
cProfile.run("main()")
