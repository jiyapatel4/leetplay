class Solution():
    def longestConsecutive(self, nums):
        hm = {}
        curr_max = 0
        for i in range(len(nums)):
            curr_num = nums[i]
            right = curr_num + 1
            left = curr_num - 1
            if curr_num not in hm:
                hm[curr_num] = 1
                if curr_max < hm[curr_num]:
                    curr_max = 1
            else:
                continue
            if left in hm and right in hm:
                hm[curr_num] = hm[left] + 1
                total_length = hm[right] + hm[left] + 1
                if hm[right] == 1:
                    hm[right] = total_length
                else:
                    last_index = right + (hm[right] - 1)
                    hm[last_index] = total_length

                if hm[left] == 1:
                    hm[left] = total_length
                else:
                    last_index = left - (hm[left] - 1)
                    hm[last_index] = total_length
                if curr_max < total_length:
                    curr_max = total_length
            elif right in hm:
                hm[curr_num] = hm[right] + 1
                if hm[right] == 1:
                    hm[right] = hm[curr_num] 
                else:
                    last_index = right + (hm[right] - 1)
                    hm[last_index] = hm[last_index] + 1
                if curr_max < hm[curr_num]:
                    curr_max = hm[curr_num]
            elif left in hm:
                hm[curr_num] = hm[left] + 1
                if hm[left] == 1:
                    hm[left] = hm[curr_num] 
                else:
                    last_index = left - (hm[left] - 1)
                    hm[last_index] = hm[curr_num]
                if curr_max < hm[curr_num]:
                    curr_max = hm[curr_num]
            
        return curr_max
