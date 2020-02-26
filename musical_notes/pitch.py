from math import log2

A0 = 440
C0 = A0 * (2 ** -4.75)
notes = [ "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B", ]


def pitch(frequence):
    height = round(12 * log2(frequence/C0))
    octave = height // 12
    number = height % 12
    return notes[number] + str(octave)


if __name__ == '__main__':
    f = int(input('freq: '))
    print(pitch(f))

