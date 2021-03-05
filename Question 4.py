from typing import List


def singleNumber(ar: List[int]) -> int:
        for i in ar:
            if(ar.count(i) == 1):
                return(i)
                
ar = [2,2,1]
ar1 = [4,1,2,1,2]
print(singleNumber(ar))
print(singleNumber(ar1))
