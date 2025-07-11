'''
Problem Description

Say you have an array, A, for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Return the maximum possible profit.
'''


class Solution:
	# @param A : tuple of integers
	# @return an integer
	def maxProfit(self, A):
        N = len(A)

        if N == 0:
            return 0
            
        min_price = A[0]
        profit = 0
        current_profit = 0

        for i in range(1, N):
            current_price = A[i]
            if current_price < min_price:
                min_price = current_price
            if current_price > min_price:
                current_profit = current_price - min_price

                if current_profit > profit:
                    profit = current_profit
        
        return profit
