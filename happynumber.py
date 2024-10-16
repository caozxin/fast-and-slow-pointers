#my working version:
class Solution:
    def isHappy(self, n: int) -> bool:
        
        test = 19
        def sum_d_sq(test):
            s_test = str(test)
            res = 0
            for each in s_test:
                # print(each)
                curr_sq = int(each) ** 2
                res = res + curr_sq
                # print(each, curr_sq, sum_d_sq)
            # print(res)
            return res

        # sum_d_sq(test)
        # n = test

        slow, fast = n, sum_d_sq(n)
        slow_list = []

        # print(slow, fast, type(slow), type(fast))

        while fast != 1 or fast != slow:
            slow_list.append(slow)
            if fast not in slow_list:
                slow = fast
                fast = sum_d_sq(slow)
            else:
                print("break")
                break
            # slow = sum_d_sq(slow)
            # fast = sum_d_sq(sum_d_sq(fast))
            # print(slow, fast, type(slow), type(fast))
        
        if fast == 1:
            return True
        else:
            return False
        
        # exit()
#improved version:
class Solution:
    def isHappy(self, n: int) -> bool:
        
        test = 19
        def sum_d_sq(test):
            s_test = str(test)
            res = 0
            for each in s_test:
                # print(each)
                curr_sq = int(each) ** 2
                res = res + curr_sq
                # print(each, curr_sq, sum_d_sq)
            # print(res)
            return res

        # sum_d_sq(test)
        # n = test

        slow, fast = n, sum_d_sq(n)
        # slow_list = []

        # print(slow, fast, type(slow), type(fast))

        while fast != 1 and fast != slow:
            slow = sum_d_sq(slow)
            fast = sum_d_sq(sum_d_sq(fast))
        
        if fast == 1:
            return True
        else:
            return False
        
        # exit()

