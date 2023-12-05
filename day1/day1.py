digitWords = { "one":1, "two":2, "three":3, "four":4,
              "five":5, "six":6, "seven":7, "eight":8, "nine":9}
digits = '0123456789'

def findFirstDigit(line: str) -> int:
    queue = ''
    for s in line:
        if s in digits:
            return int(s)
        else:
            queue += s
            for key in digitWords.keys():
                if key in queue:
                    return int(digitWords[key])
                
def findLastDigit(line: str) -> int:
    stack = ''
    for s in line[::-1]:
        if s in digits:
            return int(s)
        else:
            stack = s + stack
            for key in digitWords.keys():
                if key in stack:
                    return int(digitWords[key])

count = 0
number = None

with open("day1/day1.txt") as f:
    for line in f.readlines():
        line = line.rstrip('\n')
        first = findFirstDigit(line)
        last = findLastDigit(line)
        number = 10 * first + last
        count += number
print(count)