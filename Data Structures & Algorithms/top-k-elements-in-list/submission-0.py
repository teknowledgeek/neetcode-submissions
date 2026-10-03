class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencyDict = defaultdict(int)
        for i in nums:
            frequencyDict[i] += 1
        # key = lambda  Name of the input variable (representing one element from the list)
        # • item[0] is the Key (the number, e.g., 3)
        # • item[1] is the Value (the frequency, e.g., 3)
        sorted_items = sorted(frequencyDict.items(),key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]