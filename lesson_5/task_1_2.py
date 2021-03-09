def odd_nums(n):
    result = (num for num in range(1, n + 1, 2))
    return result
    # for num in range(1, n+1, 2):
    #     yield num

# другой вариант вывода нечетных чисел, при использовании yield
# print(type(result))
# print(odd_nums(7)

# result = odd_nums(7)
# print(next(result), next(result), next(result), next(result), next(result), next(result))

print(*odd_nums(7))


