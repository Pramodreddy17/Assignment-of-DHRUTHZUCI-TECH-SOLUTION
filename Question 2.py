from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


arr1 = [1,2,2,1]
arr2 = [2,2]
print(intersection(arr1,arr2))
