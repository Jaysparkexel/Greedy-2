
# Time Complexity: O (n)(Where n is total numbers) 
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Three line explanation of solution in plain english:
# greedy approach can be used here

class Solution:
    def candy(self, ratings: List[int]) -> int:
#       Assign one candies to all child at first
        candies = [1] * len(ratings)
        
#       Now check from the left side, If current child's rating is more than rating of child on left side, give current child 1 more candies than left side child's candies.
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
                
#       Now check from the right side, If current child's rating is more than rating of child on right side, give current child max of current candies and 1 more candies than right side child's candies.
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
                
#       Return the sum of the candies
        return sum(candies)
