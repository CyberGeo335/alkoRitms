"""
You are given three arrays of length n that describe the properties of n coupons: code, businessLine, and isActive. The ith coupon has:

code[i]: a string representing the coupon identifier.
businessLine[i]: a string denoting the business category of the coupon.
isActive[i]: a boolean indicating whether the coupon is currently active.
A coupon is considered valid if all of the following conditions hold:

code[i] is non-empty and consists only of alphanumeric characters (a-z, A-Z, 0-9) and underscores (_).
businessLine[i] is one of the following four categories: "electronics", "grocery", "pharmacy", "restaurant".
isActive[i] is true.
Return an array of the codes of all valid coupons, sorted first by their businessLine in the order:
"electronics", "grocery", "pharmacy", "restaurant", and then by code in lexicographical (ascending)
order within each category.
"""

import re
CATEGORIES = ["electronics", "grocery", "pharmacy", "restaurant"]
VALID = True

class Solution(object):
    def validateCoupons(self, code, businessLine, isActive):
        finalARR = {cat: [] for cat in CATEGORIES}

        for i in range(len(code)):
            if (businessLine[i] in finalARR and
                    isActive[i] == VALID and
                    re.match(r'^[a-zA-Z0-9_]+$', code[i])):
                finalARR[businessLine[i]].append(code[i])

        res = []
        for cat in CATEGORIES:
            finalARR[cat].sort()
            res.extend(finalARR[cat])


        return res

test = Solution()
res = test.validateCoupons(
    code = ["SAVE20","","PHARMA5","SAVE@20"],
    businessLine = ["restaurant","grocery","pharmacy","restaurant"],
    isActive = [True,True,True,True],
)
print(res)