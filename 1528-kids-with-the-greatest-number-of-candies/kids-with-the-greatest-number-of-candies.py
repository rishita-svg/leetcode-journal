class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result=[]
        maxx=max(candies)
        for i in range(len(candies)):
            if(candies[i]+extraCandies >= maxx):
                result.append(True)

            else:
                result.append(False)
        
        return result