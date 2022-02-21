'''
Author: JIANG Yilun
Date: 2022-02-21 15:25:10
LastEditTime: 2022-02-21 15:33:05
LastEditors: JIANG Yilun
Description: 
FilePath: /UGA_INF/INF101/temp/HAOYU_21/02/22.py
'''

class Solution(object):
    def maxProfit(self, prices) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        zonglirun = 0
        for i in range(1, len(prices)):
            temp = prices[i] - prices[i - 1]
            if temp > 0:
                zonglirun += temp
        return zonglirun
    