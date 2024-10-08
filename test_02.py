
# This works, but gives 'Time Limit Exceeded' error. Must be made more performant.
def daily_temperatures(temperatures: list[int]) -> list[int]:
    tests = []
    for i, val in enumerate(temperatures):
        num = 1_000
        add_val = 1
        while num >= 0 and (i + add_val) < len(temperatures):
            num = val - temperatures[i + add_val]
            if num < 0:
                break
            else:
                add_val += 1

        if num < 0:
            tests.append(add_val)
        elif num >= 0:
            tests.append(0)

    return tests


# This one is much faster. Still have to fully understand it but it works.
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    results = [0] * len(temperatures)  # e.g. [0, 0, 0, 0]
    stack: list[int] = []
    for i, val in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < val:
            index = stack.pop()
            results[index] = i - index
        stack.append(i)

    return results


def main() -> None:
    print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))


if __name__ == '__main__':
    main()

# [73,74,75,71,69,72,76,73]                 -> [1,1,4,2,1,1,0,0]
# [89, 62, 70, 58, 47, 47, 46, 76, 100, 70] -> [8,1,5,4,3,2,1,1,0,0]
# [34,80,80,80,34,80,80,80,34,34]           -> [1,0,0,0,1,0,0,0,0,0]
