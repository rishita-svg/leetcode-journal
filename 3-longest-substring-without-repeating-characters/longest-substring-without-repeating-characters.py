class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the last seen index of each character
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If the character is already in the map and within the current window
            if char in char_map and char_map[char] >= left:
                # Move the left pointer to the right of the previous occurrence
                left = char_map[char] + 1
            
            # Update the last seen index of the character
            char_map[char] = right
            
            # Calculate the current window length and update max_length
            current_window_size = right - left + 1
            max_length = max(max_length, current_window_size)
            
        return max_length