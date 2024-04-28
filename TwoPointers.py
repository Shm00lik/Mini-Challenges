# https://www.instagram.com/reel/C6PBtCAr3xp/


class Solution:
    def two_pointers(self, numbers: list[int], target: int):
        left = 0
        right = len(numbers) - 1

        temp_sum = numbers[left] + numbers[right]

        while temp_sum != target:
            if temp_sum < target:
                left += 1
            else:
                right -= 1

            temp_sum = numbers[left] + numbers[right]

        return numbers[left], numbers[right]


print(Solution().two_pointers([2, 7, 11, 15], 18))  # -> (7, 11)
print(Solution().two_pointers([2, 7, 11, 15], 13))  # -> (2, 11)
