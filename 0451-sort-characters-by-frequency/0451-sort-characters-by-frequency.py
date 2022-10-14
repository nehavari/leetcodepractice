from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        inv_counter = {}
        for key, value in counter.items():
            if value not in inv_counter:
                inv_counter[value] = []
            inv_counter[value].append(key)
            
        sorted_keys = sorted(list(inv_counter.keys()), reverse=True)
        
        sorted_s = []
        for val in sorted_keys:
            for char in inv_counter[val]:
                sorted_s.extend([char] * val)
                
        return ''.join(sorted_s)