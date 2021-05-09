from collections import deque

class Solution:
    def is_palindrome(self, integer):
        word = str(integer)
        length = len(word)
        for l in range(length // 2):
            if word[l] != word[length - 1 - l]:
                return False
        return True
            
    def superpalindromesInRange(self, left: str, right: str) -> int:
        """
        We can find rule for super-palindrome
        (1, 1)
        (2, 4)
        (3, 9)
        (11, 121)
        (22, 484)
        (101, 10201)
        (111, 12321)
        (121, 14641)
        (202, 40804)
        (212, 44944)
        (1001, 1002001)
        (1111, 1234321)
        (2002, 4008004)
        The root number is concated based on 0, 1, 2, and some rule breakers like 1, 2, 3.
        so we can concat these three numbers as the candidate of super-palindrome as BFS(Breadth-First Search).
        Or if we use Brute-force attack, it will exceed time limit.
        """
        queue = deque(["11", "22"])
        candi = set()
        r = int(right)
        l = int(left)
        while queue:
            size = len(queue)
            for _ in range(size):
                i = queue.popleft()
                candi.add(i)
                if int(i) ** 2 > r:
                    continue
                for j in ["0", "1", "2"]:
                    new_i = i[:len(i) // 2] + j + i[len(i) // 2:]
                    queue.append(new_i)
        
        # some rule breaker
        candi.add("1")
        candi.add("2")
        candi.add("3")
        count = 0
        for i in candi:
            int_i = int(i)
            if l <= int_i ** 2 <= r and self.is_palindrome(int_i ** 2):
                count += 1
        
        
        return count
