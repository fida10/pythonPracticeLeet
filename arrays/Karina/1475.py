# 1475. Final Prices With a Special Discount in a Shop
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        LP = len(prices)
        answers = [0] * LP
        for i in range(0, LP):
            counter = 0;
            for j in range((i + 1), LP):
                if prices[i] >= prices[j]:
                    answers[i] = prices[i] - prices[j]
                    break
                else:
                    answers[i] = prices[i]
        if i == (LP - 1):
            answers[i] = prices[i]
        return (answers)


