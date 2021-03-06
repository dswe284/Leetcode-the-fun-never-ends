# Leetcode 22. Generate Parentheses 
# Medium 12/26/20

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

 

# Constraints:

#     1 <= n <= 8

# Solution 1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.gen(n,n,"")
        
        return self.ans

    # o means total no. of reamining OP availabel to append.
    # c total no. of remaining CP available to append
    # s currently constructed string.
    
    def gen(self, o,c,s):
        if o> c:
            return
        if o == 0 and c == 0:
            self.ans.append(s)
            return
        if o == 0:
            self.gen(o, c-1, s+")")
        else:
            self.gen(o-1, c, s+"(")
            self.gen(o,c-1,s+")")
        



# Solution Python DP solution 
# Basically the same with approach 3, but we can see generateParenthesis(k) is called multiple times for a certain value k. So we can use recursion+memo to perform a DP, which takes more memory but much faster.
# BTW, c means how many parenthesis in the left part of "({}){}" format.

# Solution 2
class Solution:
    def generateParenthesis(self, n:int ):
        dp = {}
        dp[0] = [""]
        dp[1] = ["()"]

        def helper(k):
            ans = []
            if k in dp:
                return dp[k]
            for c in range(k):
                left = helper(c)
                right = helper(k-c-1)
                for item1 in left:
                    for item2 in right:
                        ans.append("({}){}".format(item1, item2))
            return ans

        ans = helper(n)
        return ans


# Solution 3 another DP solution


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp={1:set()}
        dp[1].add("()")
        for i in range(1,n):
            dp[i+1]=set()
            for j in dp[i]:
                dp[i+1].add("("+j+")")
            for j in range((i+1)//2):
                for k in dp[j+1]:
                    for l in dp[i-j]:
                        dp[i+1].add(k+l)
                        dp[i+1].add(l+k)
                        
        return list(dp[n])





# Solution 4
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def gen(o,c,s):
            if o > c: 
                return
            if o == 0 and c == 0:
                ans.append(s)
                return
            if o == 0:
                gen(o,c-1,s+")")
            else:
                gen(o-1,c,s+"(")
                gen(o,c-1,s+")")
        gen(n,n,"")
        return ans

    # T: O(a)
    # S: O(a)



# Solution 5
# 12 ms
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        cache = [set() for _ in range(n + 1)]
        for i in range(1, n + 1):
            if i == 1:
                cache[i].add("()")
            else:
                for j in range(1, i // 2 + 1):
                    for a in cache[j]:
                        for b in cache[i - j]:
                            cache[i].add(a + b)
                            cache[i].add(b + a)
                            if j == 1:
                                cache[i].add("(" + b + ")")
        return cache[-1]


# Solution 6
# sample 16 ms submission

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = set()
        if n == 1:
            return ["()"]
        for p in self.generateParenthesis(n - 1):
            for i,c in enumerate(p):
                if c == '(':
                    result.add(p[:i+1] + "()" + p[i+1:])
            result.add(p + "()")
        return list(result)  
        


# Solution 5
# 20 ms
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def helper(num_open, num_close, slate):
            
            if num_open > num_close:
                return
            
            if num_open == num_close == 0:
                result.append("".join(slate))
                return
            
            if num_open:
                slate.append('(')
                helper(num_open-1, num_close, slate)
                slate.pop()
            
            if num_close:
                slate.append(')')
                helper(num_open, num_close-1, slate)
                slate.pop()
            
        result = []
        helper(n, n, [])
        return result
                         


# Solution 6
# 32 ms
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]


# Solution 7
# 40 ms

from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        deq = deque([(n, n, ''),])
        all_parens = []
        while deq:
            p, q, parens = deq.popleft()
            if p < 0 or q < 0:
                continue
            if p == 0 and q == 0:  
                all_parens.append(parens)
            if q > 0 and p <= q:
                deq.append((p-1, q, parens + "("))
                deq.append((p, q-1, parens + ")"))
                           
        return all_parens
        

# Solution 8
# 96 ms
class Solution:
    def generateParenthesis(self, n: int):
        last_list=[]
        last_list.append("()")
        k=1
        self.insert(last_list,k+1,n)
        return last_list
    def insert(self,last_list,k,n):
        if k>n:
            return None
        list_len=len(last_list)
        for i in range(list_len):
            temp=last_list.pop(0)
            temp_len=len(temp)
            for j in range(1,temp_len):
                s=temp[0:j]+"()"+temp[j::]
                if not s in last_list:
                    last_list.append(s)
            s=temp[0:temp_len]+"()"
            if not s in last_list:
                last_list.append(s)
        self.insert(last_list,k+1,n)