def main():
    with open("../inputs/day7.txt") as file:
        inputs = file.readline().split(",")
        span = [0]
        for x in inputs:
            y = int(x) 
            if y >= len(span):
                span += [0 for i in range(y - len(span) + 1)]
            span[y] += 1
        sorted_span = [(span[x], x) for x in range(len(span))]
        sorted_span.sort(reverse=True)
        target = sorted_span[0][1]
        # initial_cost = calc_cost_to_position(span, target)
        print(brute_force_search(span, 0))
        # left = iterative_search(span, target - 1, initial_cost, -1)
        # right = iterative_search(span, target + 1, initial_cost, 1)
        # if left[1] < right[1]:
        #     print(left)
        # else:
        #     print(right)


# this gave an off by one error...
def iterative_search(span, target, currentMinimum, direction):
    if target == 1 or target == (len(span) - 1):
        return (target, currentMinimum)
    cost = calc_cost_to_position(span, target)
    if cost < currentMinimum:
        return iterative_search(span, target + direction, cost, direction)
    else:
        return (target - direction, currentMinimum)


# this works for part 1:
def brute_force_search(span, start):
    currentMinimum = (0, 999999999999)
    for i in range(len(span)):
        cost = calc_cost_to_position(span, i)
        if cost < currentMinimum[1]:
            currentMinimum = (i, cost)
    return currentMinimum


def calc_cost_to_position(span, target):
    cost = 0
    for x in range(len(span)):
        distance = int(abs(x - target))
        cost += (distance * (distance + 1) // 2) * span[x]
    return cost


if __name__ == "__main__":
    main()
