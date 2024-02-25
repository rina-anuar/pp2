import re

def test(pattern, testData, testNumber, expectedResult):
    if re.search(pattern, testData) == expectedResult:
        print(testNumber + " is passed!")
    elif re.search(pattern, testData) != None:
        print(testNumber + " is passed!")
    else: 
        print(testNumber + " is not passed!")

pattern = '^[a-z]+_[a-z]+$'
test(pattern, "apple_apple_mandarin_ghsg", "test1", True)
test(pattern, "aplle_banana", "test2", True)
test(pattern, "_banan_mandarin", "test3", True)
test(pattern, "mandarin_mandarin__apple", "test4", True)
test(pattern, "_banan_", "test5", True)