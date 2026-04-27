def solve_tsp(cost):
    n = len(cost)
    memo = {}

    def tsp(mask, pos):
        if mask == (1 << n) - 1:
            return cost[pos][0]
        
        state = (mask, pos)
        if state in memo:
            return memo[state]
        
        ans = float('inf')
        for city in range(n):
            if (mask & (1 << city)) == 0:
                new_cost = cost[pos][city] + tsp(mask | (1 << city), city)
                ans = min(ans, new_cost)
        
        memo[state] = ans
        return ans

    return tsp(1, 0)

cost = [[0, 111], [112, 0]]
print(f"Minimum Cost: {solve_tsp(cost)}")
