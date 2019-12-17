# @param {Integer} n
# @return {Integer}
def fib(n)
  dp = {1=>1, 0=>0}
  for i in 2..n
    dp[i] = dp[i-1] + dp[i-2]
  end
  return dp[n]
end
