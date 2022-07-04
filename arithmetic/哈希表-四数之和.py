"""
给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：

答案中不可以包含重复的四元组。

示例：

给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/4sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # # 在三数之和的基础上增加一个for循环即可
        # res = []
        # length = len(nums)
        # if length < 4: return res
        # # 如果有4个以上的0时，如何处理
        # if set(nums) == 0: return [[0,0,0,0]]
        # # 对数组进行从小到大排序，只有排序之后，下面的方法才成立
        # nums.sort()
        # for i in range(length - 3):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     for j in range(i + 1,length - 2):     # 这里得时i+1，j的范围从i+1开始
        #         if j > 1+i and nums[j] == nums[j-1]:  # 这里判断的时候j得大于i+1而不是大于1
        #             continue
        #         start = j + 1
        #         end = length - 1

        #         while start < end:
        #             summary = nums[i] + nums[j] + nums[start] + nums[end]
        #             if summary == target:
        #                 res.append([nums[i],nums[j],nums[start],nums[end]])
        #                 while start < end and nums[start] == nums[start+1]: start += 1 # 当后一个值与本次值相等，则跳过，这样下次计算的时候
        #                 # 可以跳过这个，为了去除结果中重复项
        #                 while start < end and nums[end] == nums[end-1]: end -= 1
        #                 # 当符合条件之后 左右指针都向中间移动一个
        #                 start += 1
        #                 end -= 1
        #             # 当和小于目标值时，需要将start指针向右移动，这样summary才有可能等于target
        #             elif summary < target: start += 1     # 这里得时elif  之前写成if了 会丢掉部分答案
        #             else: end -= 1
        # return res

        # 使用哈希表和集合的方法

        # 执行用时 :48 ms, 在所有 Python3 提交中击败了100.00%的用户
        # 内存消耗 :13.7 MB, 在所有 Python3 提交中击败了6.30%的用户

        nums.sort()  # 排序放在前面，建立字典得是在排序之后建立
        length = len(nums)
        if length == 0:
            return []
        hashmap = dict(
            (value, index) for index, value in enumerate(nums)
        )  # 注意 这么创建完字典后，重复的值都将被覆盖
        # print(hashmap)
        # 设置一个集合，用于放最终结果，使用集合可以产生去重复的效果
        res = set()

        max_num = nums[-1]
        for i in range(length - 3):
            a = nums[i]
            if a + 3 * max_num < target:
                continue  # 当最小的数和3倍最大的数加一起还比目标值小的话，证明这个数a和其他的组合也不可能达到目标值，所以需要更大的数，则开始下一次循环
            if 4 * a > target:
                break  # 如果当最小的数的4倍就比目标值大，则退出循环，直接输出没有符合答案的解
            for j in range(i + 1, length - 2):
                b = nums[j]
                if a + b + 2 * max_num < target:
                    continue
                if a + 3 * b > target:
                    break
                for k in range(j + 1, length - 1):
                    c = nums[k]
                    d = target - (a + b + c)
                    if d > max_num:
                        continue
                    if d < c:
                        break
                    if d in hashmap and hashmap[d] > k:
                        res.add([a, b, c, d])
        return list(res)
