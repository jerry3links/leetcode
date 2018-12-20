# \[Note] LeetCode / Clean Code Handbook

My [Git Repo.](https://github.com/jerry3links/leetcode) for leetcoding

## 本日解 (Accepted)

\[ ]


## 進行中 (優先待解, 還沒參透, 或想繼續鑽研的)

\[[**6.** ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/),   [(M)**39**. Combination Sum](https://leetcode.com/problems/combination-sum/),   [**129**. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/),  , , [**459**. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/),   ,   [(M)**539**. Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/)  , [(M)**468**. Validate IP Address](https://leetcode.com/problems/validate-ip-address/),    [(H)**41**. n-queens](https://leetcode.com/problems/n-queens/),    ]

## 目前已解 (32)

### Easy (13)

\[ **1**. Two Sum, **7**. Reverse Integer, **9**. Palindrome Number, **14**. Longest Common Prefix, **27**. Remove Element, **108**. Convert Sorted Array to Binary Search Tree,  (E)**155**. Min Stack ,   [(E)**840**. Magic Squares in Grid](https://leetcode.com/problems/magic-squares-in-grid/submissions/)    ,   **700**. Search In a Binary Search Tree, [**771**. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/submissions/), [**896**. Monotonic Array](https://leetcode.com/problems/monotonic-array/) ,   (E)905. Sort Array by Parity  , [**929**. Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/submissions/), ]

### Medium (17)

\[ [**11**. Container With Most Water](https://leetcode.com/problems/container-with-most-water/), [**33**. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/), **98**. Validate BST, **103**. Binary Tree Zigzag Level Order Traversal, [**109**. Convert Sorted List To Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/), **120**. Triangle,  [**142**. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/),   [**179**. Largest Number](https://leetcode.com/problems/largest-number/submissions/), **200**. Number of Islands, **279**. Perfect Squares, [**300**. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/), [(M)**322**. Coin Change](https://leetcode.com/problems/coin-change/),  **622**. Design Circular Queue, **338**. Counting Bits, [(M)**518**. Coin Change II](https://leetcode.com/problems/coin-change-2/),   [**785**. Is Graph a Bipartite](https://leetcode.com/problems/is-graph-bipartite/)  ,  [**907**. Sum of subarray minimums](https://leetcode.com/problems/sum-of-subarray-minimums/), ]

### Hard (2)

\[[ **45**. Jump Game II](https://leetcode.com/problems/jump-game-ii/)(很難, py不能用DP, 目前看GA有比之前看理解), [**224**. Basic Calculator](https://leetcode.com/problems/basic-calculator/), ]


## Note


問題分難中易，難通常是演算法性質的問題，又分出現頻率，這是根據用戶面試遇到題目次數的統計而得，每題又會配幾個延伸問題，面試時是可以問面試官的。適時的問問題可以呈現你的思路。通常作答超過30行，表示程式碼不夠簡潔，本書題目的參考答案通常都在20~30行之間。

至於acceptance, 大概是所有submit次數中通過的百分比, 目前理解百分比愈高, 可能就是題目偏簡單~~或者這個題目出現頻率非常高~~ (其實要看submit次數)



### Ch 1. Array/String

#### [1. Two Sum | Easy](https://leetcode.com/problems/two-sum/submissions/)

給定list和target, 找出兩個元素的索引, 其sum等於target, map的組成以元素值為key, 索引為value
(~~前提: 如果元素不重複, 就可以用元素當key~~)


<details><summary>Solution</summary><p>

```python=
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        tab = {}
        for idx in range(len(nums)):
            val = nums[idx]
            if (target - val) in tab:
                return [tab[target - val], idx]
            tab[val] = idx
        return []
```

</p></details>

上面是O(n)解之一, 注意return的順序`[tab[target - val], idx]`, idx排在後面, 這是因為一定要跑完一次全部元素, key-value的pair才會全部建立完成, 另外重複元素的case(例如`list = [3,3], target = 6`)也可以通過的原因是因為, hashmap剛好可以檢查到重複項

#### [27. Remove Element | Easy](https://leetcode.com/problems/remove-element/submissions/)
<details><summary>Solution</summary><p>

```python=
class Solution:
    def removeElement(self, nums, val):
        idxes = [i for i in range(len(nums)) if nums[i] == val]
        for i in range(len(idxes)):
            del(nums[idxes[i]-i])
        return len(nums)
```
</p></details>
第三行是類似partition裡的pivot ([QuickSort](https://openhome.cc/Gossip/AlgorithmGossip/QuickSort3.htm))

或是用索引去逼近, 也有機會達99%的faster, 不過這兩種寫法, 都有可能遇到16%的faster, 這可能是這題反讚數特高的原因, 個人猜測是test case或題型設計未展現鑑別度吧?



### Ch 2. Math

, **7**. Reverse Integer, **9**. Palindrome Number,

### Ch 3. Linked List

#### [142. Linked List | Medium](https://leetcode.com/problems/linked-list-cycle-ii/)

Python 用set或用dict都可以, 注意題目要求的回傳形式, 然後也要注意edge case (空陣列), 第一次做花了一小時

### Ch 4. Binary Tree

#### [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/)
<details><summary>Solution</summary><p>

```python=
class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if len(nums) >= 1:
            mid = int(len(nums) / 2)
            root = TreeNode(nums[mid])
            root.left = self.sortedArrayToBST(nums[:mid])
            root.right = self.sortedArrayToBST(nums[mid+1:])
            return root
        else:
            return None

```

</p></details>

#### [109. Convert Sorted List to Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/submissions/)

暴力解, 將linked list轉換成array, 取中間點當root,再把剩下的array切開轉成兩個linked list, recursively進行下去 


### Ch 5. Bit Manipulation

除以2, 餘數就會是LSB, 重複對商做, 直到無法除


### Ch 6. MISC



### Ch 7. Stack
#### [155. Min Stack]()

最簡單的解法如下, 就是都用builtin function, 但是這會有1%的速度, 應該主要min()的關係

<details><summary>Solution</summary><p>

```python=
    class MinStack:

        def __init__(self): self.stack = []
        def push(self, x): self.stack.append(x)
        def pop(self): if self.stack:self.stack.pop()
        def top(self): if self.stack: return self.stack[-1]
        def getMin(self): if self.stack: return min(self.stack)
```

</p></details>

O(1)的解就是每加一個元素多用它旁邊的空間來記錄最小值, 所以可以用-2來存取, 空間複雜度會是2N, 快很多

<details><summary>Solution</summary><p>

```python=
TBA
```

</p></details>

### Ch 8. Dynamic Programming

- 針對可用DP演算法解的問題, 例子為背包問題或旅行推銷員問題, 其問題性質有二
  - **Optimal Substructure**: 這個問題的最佳解也包含在其子問題的最佳解 (最佳解由子問題的最佳解組成, 或說經由子問題的最佳解可找到最佳解)
  - **Overlapping Subproblem**: 子問題會重複出現, DP法對此性質的對策之一是bottom-up, 透過table來儲存問題解 (稱為Memorization)

- DP和**Divide-and-Conquer**的差別, 在於D&C的會重複處理同樣問題很多次, 相對地DP會把問題的解儲存起來
- DP和**Greedy Algorithm**的差別, 在於GA是top-down, 此外DP有時多此一舉 (Overkill, 效果不彰, 可能反而多花時間)
  - 針對Greedy Algorithm可解的問題性質, 其問題性質有二
    - Optimal Substructure: 同DP
    - **Greedy Choice Property**: 當下的最佳解 (選擇) 是基於之前的最佳解, 而非之後所有可能子問題的解, 可用此法解的問題會被此法不斷化約, 此法不會重新考慮之前的解, 這也就是GA與DP的最大差別



### Ch 9. Binay Search

#### [98. Validate Binary Search Tree | Medium](https://leetcode.com/problems/validate-binary-search-tree/submissions/)

練習:
<details><summary>Solution</summary><p>

```python=
class Solution:

def isValidNode(self, root, minVal, maxVal):
    if not root:
        return True
    if root.val > minVal and maxVal > root.val:
        L = self.isValidNode(root.left, minVal, root.val)
        R = self.isValidNode(root.right, root.val, maxVal)
        return L and R
    else:
        return False
def getMin(self, root):
    while root.left:
        root = root.left
    return root.val
def getMax(self, root):
    while root.right:
        root = root.right
    return root.val


def isValidBST(self, root):
    if not root:
        return True
    minV = self.getMin(root)
    maxV = self.getMax(root)
    return self.isValidNode(root, minV-1, maxV+1)
```

</p></details>

#### [700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)

先檢查edge case (none), 再檢查val, 是就return這個node, 否則分大小去recursive右或左邊 (記得return)





### Other

#### 重點概念

**Binary Search vs Binary Tree**,  **Linked List**,  **DP**,  **Stack & Queue**, **Algorithm**, **Combination and Permutation**

O(n): big o表示法, 用來為演算法做分類, 用來形容: 隨著input的量增加, 花費時間 或 花費記憶體 會如何增長

#### 其它各題解法雜記

- [322\. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/submissions/)
  可以用list, pop作為dequeue, 或用索引0和-1來dequeue, 第一版的解法感覺沒有circular(或ring)的概念在內, 下面是有head和tail的索引寫法, tail用shift之後就有ring的感覺

    <details><summary>Solution</summary><p>

    ```python
    class MyCircularQueue:
        def __init__(self, k):
            self.maxS = k
            self.head = 0
            self.tail = 0
            self.list = []
            self.size = 0  
        def enQueue(self, value):  
            if self.isFull():
                return False  
            self.list.append(value)
            self.tail = (self.tail + 1) % self.maxS
            self.size += 1
            return True
        def deQueue(self):
            if self.isEmpty():
                return False
            del(self.list[self.head])
            self.tail = (self.tail - 1) % self.maxS
            self.size -= 1
            return True
        def Front(self):
            if self.isEmpty():
                return -1
            return self.list[self.head]
        def Rear(self):
            if self.isEmpty():
                return -1
            return self.list[(self.tail-1) % self.maxS]
        def isEmpty(self):
            return self.size == 0
        def isFull(self):
            return self.size >= self.maxS
    ```
    </p></details>



- [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

	- DP解
      和322. Coin Change類似, 把square number當作硬幣集合, n就是要找的錢量, 找出最少的硬幣組合, 就是最少的平方數組合
	- BFS解
    <details><summary>BFS Solution</summary><p>

    ```python=
    
    class Solution:
        def numSquares(self, n):
            """
            :type n: int
            :rtype: int
            """
            box = [i*i for i in range(1,n+1)]
    
            # edge case
            if 2 >n:
                return n
    
            toCheck = {n}
    
            cnt = 0
            while toCheck:
                cnt += 1
                temp = set()
                for x in toCheck:
                    for y in box:
                        if y > x:
                            break
                        if x == y:
                            return cnt
                        temp.add(x - y)
                toCheck = temp
    
            return cnt
    ```
    ​                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                </p></details>

- [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/submissions/)
    <details><summary>Solution (Without String)</summary><p>

    ```python=
    class Solution:
        def longestCommonPrefix(self, strs):
            """
            :type strs: List[str]
            :rtype: str
            """
            if 0 >= len(strs):
                return ""
            elif len(strs) == 1:
                return strs[0]
            base = strs[0]
            cnt = 0
            cm_map = {}
            for trgt in strs[1:]:
    
                idx = 0
                flag = True
                cstr = ""
                while flag and len(trgt) > idx and len(base) > idx:
                    if base[idx] != trgt[idx]:
                        flag = False
                        break
                    cstr += base[idx]
                    idx +=1
                cm_len = idx
                if cm_len > 0:
                    cm_map[cm_len] = cstr
                else:
                    return ""
            if 0 >= len(cm_map):
                return ""
            a = min(cm_map.keys())
            return cm_map[a]
    
    ```

    </p></details>
    暴力解, 因為要每個都有共通, 所以一遇到有common為0就可以return空字串, 另外要注意幾個邊際case, 例如空list, 只有一個字串等等

- [338. Counting Bits](https://leetcode.com/problems/counting-bits/)
    <details><summary>Solution (Brute Force)</summary><p>

    ```python=
    class Solution:
        def countBits(self, num):
            """
            :type num: int
            :rtype: List[int]
            """
            ans = []        
            for val in range(0, num+1):
                cnt = 0
                rem = int(val / 2)
                mod = val % 2
                cnt += 1 if mod == 1 else False
                while rem > 0:
                    mod = rem % 2
                    cnt += 1 if mod == 1 else False
                    rem = int(rem / 2)
                ans.append(cnt)
            return ans
    ```

    </p></details>

    <details><summary>Solution (Better)</summary><p>

    ```python=
    class Solution:
        def countBits(self, num):
            ans=[0]
            i=1
            while lt(i,num+1):
                i *= 2
                for j in range(len(ans)):
                    ans.append(ans[j]+1)
            return ans[:num+1]
    ```

    </p></details>

- [103. Binart Tree Zigzag Lvel Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)
    <details><summary>Solution</summary><p>

    ```python=
    
    class Solution:
    
        depthMap = {}
    
        def pushTree(self, root, d):
    
            if not root:
                return
    
            if d in self.depthMap:
                self.depthMap[d].append(root)
            else:
                self.depthMap[d] = [root]
    
            self.pushTree(root.left, d+1)
            self.pushTree(root.right, d+1)
    
        def zigzagLevelOrder(self, root):
            """
            :type root: TreeNode
            :rtype: List[List[int]]
            """
    
            self.pushTree(root, 0)
    
            depths = self.depthMap.keys()
    
            L = []
            if not depths:
                return L
    
            for d in range(0, max(depths) + 1):
                nodeLst = self.depthMap[d]
                if d % 2 == 0:
                    l = []
                    for i in range(0, len(nodeLst)):
                        l.append(nodeLst[i].val)
                    L.append(l)
                else:
                    nodeLstR = list(reversed(nodeLst))
                    l = []
                    for i in range(0, len(nodeLstR)):
                        l.append(nodeLstR[i].val)
                    L.append(l)
            self.depthMap.clear()
            return L
    
    ```

    </p></details>

- [120. Triangle](https://leetcode.com/problems/triangle/)
    <details><summary>Solution</summary><p>

    ```python=
    class Solution:
        def minimumTotal(self, trg):
            l=len(trg)
            for i in range(l):
                trg[i]+=[0]*(l-(i+1)) # 為了方便加值, 把"三角形"擴增為fix的陣列
            for i in range(l-2, -1, -1): # 從最下層開始
                for j in range(i+1): # 每個元素都做, 找最小的往上加
                    if trg[i+1][j+1] >= trg[i+1][j]: # 0 1 2
                        trg[i][j]+= trg[i+1][j]
                    else:
                        trg[i][j]+= trg[i+1][j+1]
            return trg[0][0] # 加到最後一層 只會有一個最佳解
    ```

    </p></details>

- [179. Largest Number]()

    <details><summary>Solution</summary><p>

    ```python=
    class Solution:
        def largestNumber(self, nums):
    
            # map will return nums' iterable using str()
            nums = map(str,nums)
            # sort list using self defined cmp, and using descending order
            nums.sort(cmp=lambda a,b : cmp(a+b,b+a), reverse=True)
    
            # join vs split
            # note the A or B, will return B if A is empty string
            return ''.join(nums).lstrip('0') or '0'
    ```

    </p></details>
- [200. Number of Islands](https://leetcode.com/problems/number-of-islands/submissions/)
  用dfs, 將拜訪過的位置標為0, 注意index out of range的問題, 效率可達60%

- [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/submissions/)
  解題想法就是用shift, 為了應付負號, 先取一個signed的變數, 最後要記得檢查是否超過有號的32bit範圍 (0x7fffffff), 因為我已經取負號, 所以其實不需要用abs
    <details><summary>Solution</summary><p>

    ```python=
    class Solution:
        def reverse(self, x):
            """
            :type x: int
            :rtype: int
            """
            signed = 1 if x >= 0 else -1
            x *= signed
            ans = 0
            while x != 0:
  
                m = x % 10
                x = int(x / 10)
                ans = ans * 10 + m
            if abs(ans) > 0x7fffffff:
                return 0
  
            return ans * signed
    ```

    </p></details>

- [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
  解題的想法就是shift不斷拆解digit, 為了拿到長度先go through一次, 用array或hash, 第二次只要做到一半長度即可
  要注意的testcase是0~9還有負數
    <details><summary>Solution (Without String)</summary><p>

    ```python=
    class Solution:
        def isPalindrome(self, x):
            """
            :type x: int
            :rtype: bool
            """
            if x less than 0 :
                return False
            elif x less than 10:
                return True
  
            l = 0
  
            tab = {}
            while x != 0:
                m = x % 10
                tab[l] = m
                x = int(x/10)
  
                l += 1
  
            flag = True
            idx = 0
            while flag == True and idx less than int(l/2): #
                print("{}vs{}:{}".format(tab[idx],tab[l-idx-1],flag))
                if tab[idx] == tab[l-idx-1]:
                    flag = True
                else:
                    flag = False
                idx += 1 
  
            return flag
    ```

    </p></details>

- [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

    <details><summary>Solution</summary><p>

    ```python=
    class Solution:
        def maxArea(self, height, result = 0, L = 0):
            if not height: return 0
            R = len(height)-1
            while L != R:
                result = max(result, min(height[L], height[R])*(R-L))
                if height[L] < height[R]:
                    L += 1
                else:
                    R -= 1
            return result
    ```

    </p></details>


- [**224**. Basic Calculator](https://leetcode.com/problems/basic-calculator/)

  或者先轉成後序([ref.](http://www2.lssh.tp.edu.tw/~hlf/class-1/lang-c/stack2.htm))

    <details><summary>Solution</summary><p>

    ```python=
    class Solution:
        def calculate(self, s):
            # 準備一個計算用的stack
            stack = []
            # 取代空白字元
            s = s.replace(" ", "")
            # 讀取字串
            for c in s:
                # 遇到括號就開始計算
                if c == ")":
                    # ...
    
                # 遇到運算子或運算元就放到stack
                elif c.isdigit():
                    if stack:
                        tail = stack[-1]
                        # 處理長度大於1的運算元
    
                    else:
                        stack.append(c)
                else:
                    stack.append(c)
    
            # 再清空一次stack
            res = 0
            while stack:
                # ...
            return res
    ```
    </p></details>

- [785. Is Graph a Bipartite](https://leetcode.com/problems/is-graph-bipartite/)

    <details><summary>Solution</summary><p>

    ```python=
    class Solution:
    
        def isBipartite(self, graph):
            """
            :type graph: List[List[int]]
            :rtype: bool
            """
            print("Initialize ...")
            colors = [-1 for i in graph]
            for v in range(len(graph)):
                if colors[v] == -1:
                    colors[v] = 0
                    if self.sameOccur(v, graph, colors):
                        return False
            return True
    
        def sameOccur(self, v, graph, colors):
            for w in graph[v]:
                if colors[w] == -1:
                    colors[w] = int(not colors[v])
                    if self.sameOccur(w, graph, colors):
                        return True
                else:
                    if colors[w] == colors[v]:
                        return True
            return False
    ```

    </p></details>

- [**300**. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

    下面是n平方的遞迴解法, 仍然會遇到TLE, 注意python 迴圈中能不要用append就不用

    <details><summary>Solution</summary><p>

    ```python=
        def LIS(self, nums):
    
            if len(nums) < 1:
                return 0
            T = [1 for v in range(len(nums))]
            LIS = 0
            for i in range(len(num)):
                for j in range(i):
                    if num[j] > num[i]:
                        T[i] = max(T[i], T[j] + 1)
                if T[i] > LIS:
                    LIS = T[i]
            return LIS
            
    ```

    </p></details>


- [45. Jump Game II]()

  以nums = [2,2,3,1,1,4]為例, 第二層while的意義是尋找從定點i跳一次後能達到的最大距離(next_reach), 當i和curr_reach為0時, 代表是初次執行還沒開始跳, 第一次執行 (跳) 後, next_reach就會是nums[0] = 2, 這裡都會檢查能達到的最大距離是否到終點, 是就直接回傳結果cnt並結束, 否則就會檢查每一個能達到的點, i用來記錄位置 (第一次跳只有0, 第二次跳時因為curr_reach是2, 所以延續上次從1開始到2共二次, 檢查到nums[2]時已經可以跳到終點了所以結束), 第一層while就是每跳完一次會對cnt加一, 並記錄上次能達的最大距離 (curr_next = next_reach)
    <details><summary>Solution</summary><p>

    ```python=
        def jump(self, nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if len(nums) <= 1:
                return 0
            curr_reach = next_reach = cnt = i = 0
            while True:
                while i <= curr_reach:
                    next_reach = max(i+nums[i], next_reach)
                    if next_reach >= len(nums) - 1:
                        return cnt + 1
                    i += 1
                curr_reach = next_reach
                cnt += 1
    ```

    </p></details>

- [**896**. Monotonic Array](https://leetcode.com/problems/monotonic-array/)
  這題麻煩的是非嚴格遞增, 要處理開頭的相同元素

- [**907**. Sum of Subarray Minimum](https://leetcode.com/problems/sum-of-subarray-minimums/)

  - 用兩個for loop列出所有sub array, 然後加總每一個陣列的最小值, 可解但會在leetcode上TLE
  - 利用monotonic stack (單調遞增或遞減的stack), 可在O(n)時間內找到PLE和NLE (next less element),  找到每個元素與PLE和NLE的距離, 就可以推算出以此元素為最小值的所有陣列, 每個元素都找過就是所有陣列, 相乘後加總就是答案, 最後要注意要取mod = 1e9 * 7, 然後轉成整數 ([參考教學](https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step))


- [(M)**322**. Coin Change](https://leetcode.com/problems/coin-change/)
  - BFS解
    用279. Perfect Squares的概念來解, 但要注意set的成本, 不能放在while loop裡面, 可以在while裡用append, 不要每個loop都重新創set
  - DP解([參考教學](https://www.youtube.com/watch?v=za2bgJLHmxI&t=1277s))
    根據目標量列出一張DP表 (0~amount), 0就設為0 (沒有硬幣找), 初值可用2**32 (表INVALID) 或無限大 float("inf"), 最後跑完如果沒變, 表示現有硬幣集合中無法組合出該量. 這個方式可以不用先對硬幣集合排序, 每種硬幣從1開始填表, 填到這個幣值再挑下一個硬幣, 每個硬幣都做完就結束了, 式子是dp[i] = min(dp[i], dp[i - coin] + 1), 舉例來說: 有{1,2,5}三種硬幣目標是3元, 挑1元硬幣填時, dp[1] = min(dp[1], dp[1-1元] + 1), dp[2] = min(dp[2], dp[2-1元] + 1), ..., 就是用1元硬幣找的所有解, 當挑到2元硬幣時, 就會再填一次dp[2] = min(dp[2], dp[2-2元] + 1), 全部跑完這格就是解

- [(M)**518**. Coin Change II](https://leetcode.com/problems/coin-change-2/submissions/)
  DP解([參考教學](https://leetcode.com/problems/coin-change-2/discuss/200847/Python-easy-to-understand-dp-solution)), 方法是先將coin由小到大排序, coins[0]就是第一種錢幣, coins[1]就是前兩種錢幣 ... , f(i,j)就是coin set i可以換成錢j的方法數, 可被化約成兩種可能:

  - 如果coins[i]的最大幣值大於j, 則f(i,j) = f(i-1, j)

    例如f($2, $3 to $2), 最大幣值無法組成2, 所以其實就是f($2 to $2)的答案

  - 如果coins[i]的最大幣值小於等於j, 則f(i,j) = f(i,j-最大幣值) + f(i-1,j)

    f($2, $3 to $4), 最大幣值可以從目標量扣除, 變成答案的一部分, 所以相當於 f($2, $3 to $2) + f($2 to $4), 前者是就是同一排左邊的答案, 後者就是上排 (較小的那些幣值) 對同樣目標量的答案


### Todo

https://leetcode.com/problemset/all/
https://interviews.skype.com/zh/Interviews?code=72a9eaf2-a055-9048-1a18-b527fcb4fbad
http://www.raychase.net/tag/leetcode
https://codingcompetitions.withgoogle.com/codejam/archive
[偷看幾摳的repo](https://github.com/eagle0401)

Code Block範本
<details><summary>Solution</summary><p>

```python=

```

</p></details>

BST題型範本

<details><summary>Solution</summary><p>

```python=


def stringToIntegerList(input):
    return json.loads(input)

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().sortedArrayToBST(nums)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

```

</p></details>