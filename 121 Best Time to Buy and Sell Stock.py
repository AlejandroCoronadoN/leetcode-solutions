class Solution:
  def maxProfit2(self, prices) -> int:
    max_gain = 0
    while p < len(prices):
      price_p = prices[p]
      min_pricesindex_since_p = p
      p+=1
      while s < len(prices):
        #print('{} {} '.format( prices[p], prices[s]))
        price_s =  prices[s]
        if price_s < price_p:
          #This means price_s at time s is better option to but and is strictly better than p
          min_pricesindex_since_p
          p=s
          price_p = price_s
        else:
          #I can amke a proffit selling buying at p and selling at s
          gain =  price_s-price_p
          if gain > max_gain:
            max_gain = gain
          s+=1
    
    return max_gain
        


prices = [7,1,5,3,6,4]
sol = Solution()
sol.maxProfit(prices)
                    