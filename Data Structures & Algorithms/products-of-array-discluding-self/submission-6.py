class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_prod = 1
        zeroes = 0
        for num in nums:
            if num == 0:
                zeroes += 1
                continue
            total_prod *= num
        
        print(zeroes)

        if zeroes > 1:
            result = [0 for i in range(len(nums))]
            print("Hello")
            print(result)
            return result
        
        result = []

        for num in nums:
            if num == 0:
                result.append(total_prod)
            elif zeroes == 1:
                result.append(0)
            else:
                result.append(int(total_prod/num))

        return result
        