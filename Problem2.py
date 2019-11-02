# Time Complexity: O (n)(Where n is length of numbers) 
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# greedy approach can be used here

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        max_freq = 0
        max_count = 0
        freq = {}
#       store frequency count and find max frequency along with it.
        for i in range(len(tasks)):
            freq[tasks[i]] = freq.get(tasks[i], 0) + 1
            max_freq = max(max_freq, freq[tasks[i]])
            
#       From max frequency find number of tasks that has frequency same as max frequency
        for val in freq.values():
            if val == max_freq:
                max_count += 1
                
#       Count parts between tasks ad max frequency minus 1
        part_count = max_freq - 1
#       Empty slots would be equal to n minus max count plus 1 and multiplied by part count.
        empty_slots = (n - (max_count - 1)) * part_count
#       We can find available slots from length of tasks minus multiplication of max frequency and max count.
        avail_slots = len(tasks) - (max_freq * max_count)
#       Calculate idle slot by substituting availabale slots from empty slots and if it is negative we have o idle slots
        idle = max(0, empty_slots - avail_slots)
        
#       Return answer as number of tasks plus idle slots.
        return len(tasks) + idle
