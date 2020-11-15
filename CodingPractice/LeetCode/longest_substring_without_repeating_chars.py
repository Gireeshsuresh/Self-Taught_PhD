class Solution:
    def lengthOfLongestSubstring(self, s):
        sub_string = {}
        cur_substring_start = 0
        cur_len = 0
        longest = 0
        for index,letter in enumerate(s):
            if letter in sub_string and sub_string[letter] >= cur_substring_start:
                cur_substring_start = sub_string[letter] + 1
                cur_len = index - sub_string[letter]
                sub_string[letter] = index

            else:
                sub_string[letter] = index
                cur_len += 1
                if cur_len > longest:
                    longest = cur_len
                    
        return longest



if __name__ == "__main__":
    sample_sol = Solution()

    input_str = "abaqrs"
    output_len = sample_sol.lengthOfLongestSubstring(input_str)
    print("Output = {}".format(output_len))