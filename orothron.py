#!/usr/bin/env python
"""
Orothron
A word/name generator by inky.
http://github.com/inky/orothron

"""
import random
import sys

class NameGenerator:
    def __init__(self, names, prefixlen=2):
        assert prefixlen > 0
        self.prefixlen = prefixlen
        self.markov = {}
        for name in filter(lambda n: len(n) > prefixlen, names):
            name = name.strip().lower()
            id = ''
            for char in list(name) + ['']:
                self.markov.setdefault(id, []).append(char)
                id = (id + char)[-prefixlen:]

    def generate(self):
        name, id, char = [], '', '^'
        while char:
            char = random.choice(self.markov.get(id, ''))
            name.append(char)
            id = (id + char)[-self.prefixlen:]
        words = ''.join(name).split()
        return ' '.join(word.capitalize() for word in words)

def main():
    names = NameGenerator(sys.stdin.read().split('\n'))
    for i in range(10):
        print(names.generate())

if __name__ == '__main__':
    main()
