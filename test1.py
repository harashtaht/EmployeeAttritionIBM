# No 4

def divisible(dictNum):
    results = 0
    for i in range(dictNum["A"], dictNum["B"]+1):
        if i%dictNum["K"] == 0:
            results+=1
        else:
            results+=0
    return results

test_A = input()
num_T = int(test_A)

if (1<=num_T<=100):
    dictOutput = {}
    for i in range(1, num_T+1):
        dictNum = {}
        dictNum["A"] = int(input())
        dictNum["B"] = int(input())
        dictNum["K"] = int(input())
        dictOutput[i] = divisible(dictNum)
else:
    breakpoint

    # print(dictNum)
    # print(f'Case {i}: {divisible(dictNum)}')
# print(dictOutput)
# dictOutput = {1: 3, 2: 4}

# for i in range(1, len(dictOutput)+1):
#     print(f'Case {i}: {dictOutput[i]}')

