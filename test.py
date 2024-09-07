def crackSafe(n, k):
    seen = set()
    ans = []

    def dfs(node):
        for x in range(k):
            nei = node + str(x)
            if nei not in seen:
                seen.add(nei)
                dfs(nei[1:])
                ans.append(str(x))

    # Start DFS with initial node of n-1 zeros
    dfs('0' * (n - 1))
    
    # Return the shortest sequence that unlocks the safe
    return ''.join(ans) + '0' * (n - 1)

# Example usage
n = 2
k = 2
print(crackSafe(n, k))  # Output: "01100"
