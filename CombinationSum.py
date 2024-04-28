# https://www.instagram.com/reel/C6MBpAUpmU_/


class Solution:
    def combination_sum(self, numbers: list[int], target: int):
        res = []

        def recursion(current_list: list[int], i: int):
            if sum(current_list) == target:
                res.append(current_list)

            current_list.append(numbers[i])
            
            # TO BE CONTINUED...

        recursion([], 0)

        return res
