#leetcode 1.两数之和 难度：easy
class Solution:
    def Two_sum(self,nums: list[int],target: int):
        hashtable = dict()
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target-num],i]
            hashtable[nums[i]] = i
        return []

if __name__ == '__main__':
    nums = []
    a = int(input("请输入数组长度："))
    target = int(input("请输入目标值："))
    for i in range(0,a):
        nums.append(int(input()))
    sol = Solution()
    res = sol.Two_sum(nums,target)
    print(res)


