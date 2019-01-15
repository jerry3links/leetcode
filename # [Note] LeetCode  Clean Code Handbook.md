# \[Note] LeetCode / Clean Code Handbook

My [Git Repo.](https://github.com/jerry3links/leetcode) for leetcoding

## 本日解 (Accepted)

\[ ]


## 進行中 (優先待解, 還沒參透, 或想繼續鑽研的)

\[    

, 

 , ,    ,  ,    ,    ]

## 目前已解 (55+1)

### Easy (24+1)

\[ **1**. Two Sum, **7**. Reverse Integer, **9**. Palindrome Number,   [**13**. Roman to Integer](https://leetcode.com/problems/roman-to-integer/submissions/)  ,  **14**. Longest Common Prefix,  [(E)**20**. Valid Parenthesis](https://leetcode.com/problems/valid-parentheses/),   [(E)**21**. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/submissions/),  **27**. Remove Element, **108**. Convert Sorted Array to Binary Search Tree,  [(E)**28**. strStr](https://leetcode.com/problems/implement-strstr/),    [(E)**125**. Valid Palindrome](https://leetcode.com/problems/valid-palindrome/)   ,  (E)**155**. Min Stack , [(E)**167**. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/),   (E)**170**. Two Sum - Data Structure ,    [(E)**189**. Rotate Array](https://leetcode.com/problems/rotate-array/),    [(E)**226**. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/),    [(E)**237**. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/), [(E)**459**. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/),    ,   **700**. Search In a Binary Search Tree, [**771**. Jewels and Stones](https://leetcode.com/problems/jewels-and-stones/submissions/),[(E)**840**. Magic Squares in Grid](https://leetcode.com/problems/magic-squares-in-grid/submissions/) ,   [**896**. Monotonic Array](https://leetcode.com/problems/monotonic-array/) ,   (E)905. Sort Array by Parity  , [**929**. Unique Email Addresses](https://leetcode.com/problems/unique-email-addresses/submissions/),   ] 170是付費題目

### Medium (27)

\[ [(M)**3**. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/),     [(M)**6.** ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/), [(M)**8**. String to Integer](https://leetcode.com/problems/string-to-integer-atoi/submissions/),   [**11**. Container With Most Water](https://leetcode.com/problems/container-with-most-water/), [**33**. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/),  [(M)**39**. Combination Sum](https://leetcode.com/problems/combination-sum/), [(M)**54**. Spiral Matrix](https://leetcode.com/problems/spiral-matrix/submissions/),  **98**. Validate BST, **103**. Binary Tree Zigzag Level Order Traversal, [**109**. Convert Sorted List To Binary Search Tree](https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/), **120**. Triangle, [(M)**129**. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/),  [**142**. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/),  [(M)**151**. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/submissions/),   [**179**. Largest Number](https://leetcode.com/problems/largest-number/submissions/),    **200**. Number of Islands, **279**. Perfect Squares, [**300**. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/), [(M)**322**. Coin Change](https://leetcode.com/problems/coin-change/), **338**. Counting Bits,  [(M)**468**. Validate IP Address](https://leetcode.com/problems/validate-ip-address/),  [(M)**518**. Coin Change II](https://leetcode.com/problems/coin-change-2/),  **622**. Design Circular Queue,   [**785**. Is Graph a Bipartite](https://leetcode.com/problems/is-graph-bipartite/)  ,  [(M)**863**. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/) , [**907**. Sum of subarray minimums](https://leetcode.com/problems/sum-of-subarray-minimums/), ]

### Hard (4)

\[ [(H)**41**. n-queens](https://leetcode.com/problems/n-queens/),   [**45**. Jump Game II](https://leetcode.com/problems/jump-game-ii/)(很難, py不能用DP, 目前看GA有比之前看理解), [**224**. Basic Calculator](https://leetcode.com/problems/basic-calculator/), [(H)**65**. Valid Number](https://leetcode.com/problems/valid-number/submissions/),  ]


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

####  [167. Two Sum II | Easy](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/)

輸入的序列是排序過的序列, 三種解法

1. 同上繼續使用HashMap, time和space complexity都是O(n), 但是這樣沒有利用到排序的特性
2. 利用binary search, 單找一個number的time complexity會是O(logn), 基本上有用到二元搜尋的算法都脫離不了logn, 最終的time complexity會是O(nlogn), 至於space complexity和brute force一樣是O(1)
3. two pointer, 有點像binary search, 並記錄頭尾兩端的索引一次改一邊, 往中間逼近, time comp.是O(n), 而因為只有紀錄前後索引, 所以space comp.是O(1)

#### 170. Two Sum III | Easy

付費才能解, 不過概念仍然是利用hash map, key就是number, value則是記錄key的出現次數

####  [28. Implement strStr() | Easy](https://leetcode.com/problems/implement-strstr/)

time comp.勢必為O(nm), space comp.為O(1), 暴力解不難, 要小心的是如何確保不TLE, 特殊case的if不加的話, 最簡潔的implementation如下 (加了會快一點):

```python
def strStr(self, haystack, needle):
    for i in range(len(haystack) + 1): # 原意是i和j都不設上限, 終止條件會在inner loop裡
        for j in range(len(needle) + 1):
            if j == len(needle): return i # j 能夠順利遞加到needle的長度表示都相同
            if i+j >= len(haystack): return -1 # haystack的剩餘長度已無法涵蓋needle的長度
            if haystack[i + j] != needle[j]: break # 一旦遇到不符就放棄, 從下個i開始
```
#### 1-7. [(M)**151**. Reverse Words in a String](https://leetcode.com/problems/reverse-words-in-a-string/submissions/)
注意edge case: `s="   "`

#### 1-8. [(M)**8**. String to Integer](https://leetcode.com/problems/string-to-integer-atoi/submissions/)

直觀解: 先取號(正或負), 在此之前遇到空白都跳過, 遇到正負號或第一個數值字元就取號, 一旦取號後, 遇到非數值字元 (含空白)就跳出, 數值處理完, 就乘上正負號再檢查是否溢位, 另外在迴圈中檢查溢位和迴圈後檢查效率沒有太大差別, 可能因為是 by 字元處理, 或條件判斷的語句沒有精簡會更費工, 不過大部份解法都差不多效率

#### 1-9. [(H)**65**. Valid Number](https://leetcode.com/problems/valid-number/submissions/)

這題很容易寫成太多if else, 所以得整理好規則, 再review一下, char by char進行

* 先檢查指數, 指數e後也可以有正負號, 但不可有小數點, 另外指數前要有digits
* 再來檢查正負號, 如出現過指數, 正負號可以再出現一次 
* 最後檢查小數點, 如果前面沒有指數才能存在小數點, 然後小數點後只能出現一次指數

把Iinput s 當作list, s[i]去檢查每個字元:

1. 有空白字元就往前進
2. 檢查正負號
3. 有數字就往前進, 並計數
4. 檢查是否有指數, 有就檢查前面是否有數字
    1. 檢查正負號
    2. 有數字就往前進, 並計數
5. 檢查是否有小數點
    1. 有數字就往前進, 並計數
    2. 類似4. 檢查指數
    3. 有指數再檢查正負號
    4. 有數字就往前進, 並計數
6. 有空白字元就前進, 做到結尾檢查是否符合指數或小數點的規則就是有效


#### 1-10. [(M)**3**. Longest Substring Without Repeating Characters](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

準備一張table, 用來列出此字串中所有字元是否出現過, 用head和tail兩個pointer來access, 以head = 0, tail從0到1去檢查, 如果遇到重複字元, 就從head + 1 開始再走一遍, 這個方法的時間複雜度是O(n)

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

#### [(E)**189**. Rotate Array](https://leetcode.com/problems/rotate-array/)

(寫超過一小時) 第1個規則是k與nums的長度, 如果k > len(num), 就有可能不用rotate, 所以加上 `k = k % len(nums)` , k 如果等於nums的長度就不用作任何事, 第2個是將nums拆成 `head = nums[-k:]` 和`tail = nums[:len(nums)-k]`, 將head與tail接在一起就是rotate後的結果, 另外題目要求modify in place, 所以一個個copy

#### [(E)**459**. Repeated Substring Pattern](https://leetcode.com/problems/repeated-substring-pattern/description/)

蠻有趣的, 從頭開始寫, 執行時間從 6000ms -> 500ms -> 100ms -> 62ms, 基本概念是, 讓題目要求可以成立的substring (注意整個字串不算substring), 其長度一定是整個字串的因數 , 所以可以用2開始切字串, 從最長的substring開始檢查, 一旦符合就結束, 虛擬碼為:
```
	len_sub = int(len(s) / 2) # 若input長度為奇數, 無法整除一定會被跳過
	while len_sub > 0: # 一直檢查到單個字元比較N次 (worst case)
		if len(s) % len_sub != 0:
			len_sub -= 1
			continue
		if s[:len_sub] * (len(s) / len_sub) == s:
			return True
		len_sub -= 1
```
####  [(M)**468**. Validate IP Address](https://leetcode.com/problems/validate-ip-address/)

1. 先區分是v4或v6,
2. for v4, 檢查leading zero和non-digit
3. for v4, 檢查0~255
4. for v6, 檢查leading zero和non-digit (hex)
5. for v6, 檢查0~65535


####  [(M)**539**. Minimum Time Difference](https://leetcode.com/problems/minimum-time-difference/) 

所有時間點換算成minutes都是不脫0~1439的值, 將各時點轉成序列成A序列, 排序後rotate (shift)成B序列, 其實就能快速形成一個所有時點的成對序列, 這比用`itertools.combinations(iterable, r)`快多了, 另外注意rotate後的B, 其最後一值要設成A[0] + 1440, 相當於過24H回頭一步做比較


### Ch 2. Math

#### **7**. Reverse Integer, 

#### [**9**. Palindrome Number | Easy ](https://leetcode.com/problems/palindrome-number/submissions/)

```python
while x != 0:
	sum = (sum * 10) + (x % 10)
	x /= 10
```



### Ch 3. Linked List

#### [142. Linked List | Medium](https://leetcode.com/problems/linked-list-cycle-ii/)

Python 用set或用dict都可以, 注意題目要求的回傳形式, 然後也要注意edge case (空陣列), (note: 第一次做花了一小時)

#### [(E)**237**. Delete Node in a Linked List](https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/)

有趣, 只給你要刪除的node, 不給你node list, 此題test case和output都已有定義, 要求是modify in-place, 概念解如下

```
	previous = None
	while node != None:
		if node.next == None
			if previous != None:
				previous.next = None
			break
		node.val = node.next.val
		previous = node
		node = node.next
```

概念是不要去更動next, 只去更新node的value, 上解不將if結合成一個的理由是這樣設計的前提是input list一定要有兩個node, 若node只有一個, previous就不會有內容, 這個方法的時間複雜度是O(n)

####  [(E)**21**. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/submissions/)

Note: python的用新的變數儲存已有的instance, 會重新分配一個instance
例如 `track.next = node1`這會新建一個instance放在next中, 和node1放的是不一樣的instance, 另外`track.next = node1 or node2`有看到這種更簡短的寫法


### Ch 4. Binary Tree

#### [(E)**226**. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/)

名題([max howell的教訓](https://www.zhihu.com/question/31202353)), 解這題時有對python的語言特性想久了一點, python的OO也有分物件層級的變數和樣例層級的變數, 針對此題的解法虛擬碼為:
```
invert(root):
    if root:
        tmp = root.left
        root.left = invert(root.right)
        root.right = invert(tmp)
    return root
```
對上例的初步理解是: 宣告tmp時, 會新分配一個instance來存放左邊分枝的內容, 之後就可以遞迴處理左和右, 相當於swap, 如果直接寫成`root.L, root.R = invert(root.R), invert(root.L)`也有相同作用

#### [(M)**129**. Sum Root to Leaf Numbers](https://leetcode.com/problems/sum-root-to-leaf-numbers/description/)

第一次想用DFS解, 解不完, BFS比較可行, 參考的解是遇到leaf就將value加到sum中 (因為可以確定leaf是個位數), 若遇到leaf以外的node, 就將當前的value乘上10, 分別加到子點, 再push 到queue以進行下一輪BFS, pseudo code:

```
queue = [root]
ans = 0
while queue:
	node = queue.pop(0)
	if node.left == node.right is None: # leaf reached!
		ans += node.val
	if node.left:
	    node.left.val += node.val * 10
	    queue.append(node.left)
    if node.right:
	    node.right.val += node.val * 10
	    queue.append(node.right)
```




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

#### [(M)**863**. All Nodes Distance K in Binary Tree](https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/)

策略: 先用DFS建立neighbors map, 將所有邊記錄成list (雙向的, 所以一個邊都會碰到兩次), 之後以target為起點, 用BFS去走訪這個neighbors map, 走到距離K就將點放到basket裡, 超過K就不再進行下去, 回傳basket就是答案, 另外要注意corner case, 例如K = 0, 這種情況就回傳target即可



### Ch 5. Bit Manipulation

除以2, 餘數就會是LSB, 重複對商做, 直到無法除


### Ch 6. Misc

#### 54. Spiral Matrix

用螺旋的方式印出矩陣元素直到中心, 提示: 走訪的方向是水平或垂直在切換, 每切換一次要走的步數都會減少, 又分前進後退, 所以會有4個if, 終止條件就是水平或垂直步數其一減至0

```python
while True:
    for _ in range(n):
        seq.append(matrix[row][++col])
    if (--n == 0): break
    for _ in range(m):
        seq.append(matrix[++row][col])
    if (--m == 0): break
    for _ in range(n):
        seq.append(matrix[row][col--])
    if (--n == 0): break
    for _ in range(m):
        seq.append(matrix[row--][col])
    if (--m == 0): break
```

#### 6-37. [(E)**13**. Roman to Integer](https://leetcode.com/problems/roman-to-integer/submissions/) 
  規則是I -> (V, X), X -> (L, C), C -> (D, M), 所以遇到IXC三種就特別檢查下一個是否為可對應的tuple, 否則就照value map加上去即可, 用while loop比較好控制

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

#### [(E)**20**. Valid Parenthesis](https://leetcode.com/problems/valid-parentheses/)

可以算是計算機的基礎題目, 遇到左括號就push到stack, 一旦遇到右括號就pop出來檢查 (stack是LIFO), 有錯就可以回傳有效作結, 所有字元都檢查完,若沒有錯, 還得檢查stack裡面有沒有沒處理的左括號 , 若有就還是無效, 最後, 空字串是有效的括號



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

##### [322\. Design Circular Queue](https://leetcode.com/problems/design-circular-queue/submissions/)
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



##### [279. Perfect Squares](https://leetcode.com/problems/perfect-squares/)

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
    </p></details>

##### [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/submissions/)

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

##### [338. Counting Bits](https://leetcode.com/problems/counting-bits/)

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

##### [(M)**6.** ZigZag Conversion](https://leetcode.com/problems/zigzag-conversion/)

初次解找到的規則是head + tail, 一開始就先建一個string list `zz = ['' for _ in range(num)]`, head就是照著num的量將橫向的字元依次append上去, tail則是剩下的字元用斜向去拜訪, 依zig zag的規則拜訪, 會少兩個字, 也就是`j in range(num - 2)`, 並且要從倒數第二個的string list開始 (`zz[num - 2 - j]`), 剛開始為了符合範例, 連空格都有印出來, 用了很多append, 執行起來只有5%的效率, 後來發現其實不用空格

##### [103. Binary Tree Zigzag Lvel Order Traversal](https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/)

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

##### [120. Triangle](https://leetcode.com/problems/triangle/)

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

##### [179. Largest Number]()

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

##### [200. Number of Islands](https://leetcode.com/problems/number-of-islands/submissions/)
用dfs, 將拜訪過的位置標為0, 注意index out of range的問題, 效率可達60%

##### [7. Reverse Integer](https://leetcode.com/problems/reverse-integer/submissions/)
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

##### [9. Palindrome Number](https://leetcode.com/problems/palindrome-number/)
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

##### [11. Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

<details><summary>Solution</summary><p>

```python=
class Solution:
    def maxArea(self, height, result = 0, L = 0):
        if not height: return 0
        R = len(height)-1
        while L != R:
            result = max(result, min(height[L], height[R])*(R-L))
            if height[R] > height[L]:
                L += 1
            else:
                R -= 1
        return result
```

</p></details>


##### [**224**. Basic Calculator](https://leetcode.com/problems/basic-calculator/)

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

##### [785. Is Graph a Bipartite](https://leetcode.com/problems/is-graph-bipartite/)

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

##### [**300**. Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)

下面是n平方的遞迴解法, 仍然會遇到TLE, 注意python 迴圈中能不要用append就不用

<details><summary>Solution</summary><p>

```python=
    def LIS(self, nums):

        if 1 > len(nums):
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


##### [45. Jump Game II]()

以nums = \[2,2,3,1,1,4]為例, 第二層while的意義是尋找從定點i跳一次後能達到的最大距離(next_reach), 當i和curr_reach為0時, 代表是初次執行還沒開始跳, 第一次執行 (跳) 後, next_reach就會是nums\[0] = 2, 這裡都會檢查能達到的最大距離是否到終點, 是就直接回傳結果cnt並結束, 否則就會檢查每一個能達到的點, i用來記錄位置 (第一次跳只有0, 第二次跳時因為curr_reach是2, 所以延續上次從1開始到2共二次, 檢查到nums\[2]時已經可以跳到終點了所以結束), 第一層while就是每跳完一次會對cnt加一, 並記錄上次能達的最大距離 (curr_next = next_reach)
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

##### [**896**. Monotonic Array](https://leetcode.com/problems/monotonic-array/)
這題麻煩的是非嚴格遞增, 要處理開頭的相同元素

##### [**907**. Sum of Subarray Minimum](https://leetcode.com/problems/sum-of-subarray-minimums/)

- 用兩個for loop列出所有sub array, 然後加總每一個陣列的最小值, 可解但會在leetcode上TLE
- 利用monotonic stack (單調遞增或遞減的stack), 可在O(n)時間內找到PLE和NLE (next less element),  找到每個元素與PLE和NLE的距離, 就可以推算出以此元素為最小值的所有陣列, 每個元素都找過就是所有陣列, 相乘後加總就是答案, 最後要注意要取mod = 1e9 * 7, 然後轉成整數 ([參考教學](https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step))

##### [(M)**322**. Coin Change](https://leetcode.com/problems/coin-change/)

**這題是求最少硬幣種類組合**, 所以可用279. Perfect Squares來解, 和518. Coin Change 2 不太一樣 (此題類39)

- BFS解
  用279. Perfect Squares的概念來解, 但要注意set的成本, 不能放在while loop裡面, 可以在while裡用append, 不要每個loop都重新創set
- DP解([參考教學](https://www.youtube.com/watch?v=za2bgJLHmxI&t=1277s))
  根據目標量列出一張DP表 (0~amount), 0就設為0 (沒有硬幣找), 初值可用2\*\*32 (表INVALID) 或無限大 float("inf"), 最後跑完如果沒變, 表示現有硬幣集合中無法組合出該量. 這個方式可以不用先對硬幣集合排序, 每種硬幣從1開始填表, 填到這個幣值再挑下一個硬幣, 每個硬幣都做完就結束了, 式子是`dp[i] = min(dp[i], dp[i - coin] + 1)`, 舉例來說: 有{1,2,5}三種硬幣目標是3元, 挑1元硬幣填時, `dp[1] = min(dp[1], dp[1-1元] + 1)`, `dp[2] = min(dp[2], dp[2-1元] + 1)`, ..., 就是用1元硬幣找的所有解, 當挑到2元硬幣時, 就會再填一次`dp[2] = min(dp[2], dp[2-2元] + 1)`, 全部跑完這格就是解

##### [(M)**518**. Coin Change II](https://leetcode.com/problems/coin-change-2/submissions/)

**這題是求所有組合法**, 類似39. Combination Sum, 和279及322 不太一樣. 最常見是DP解([參考教學](https://leetcode.com/problems/coin-change-2/discuss/200847/Python-easy-to-understand-dp-solution)), 方法是先將coin由小到大排序, coins\[0]就是第一種錢幣, coins\[1]就是前兩種錢幣 ... , f(i,j)就是coin set i可以換成錢j的方法數, 可被化約成兩種可能:

- 如果coins\[i]的最大幣值大於j, 則f(i,j) = f(i-1, j)

  例如f($2, $3 to $2), 最大幣值無法組成2, 所以其實就是f($2 to $2)的答案

- 如果coins[i]的最大幣值小於等於j, 則f(i,j) = f(i,j-最大幣值) + f(i-1,j)

  f($2, $3 to $4), 最大幣值可以從目標量扣除, 變成答案的一部分, 所以相當於 f($2, $3 to $2) + f($2 to $4), 前者是就是同一排左邊的答案, 後者就是上排 (較小的那些幣值) 對同樣目標量的答案

##### [(M)**39**. Combination Sum](https://leetcode.com/problems/combination-sum/)

類似518 (將candidates想成coins), 建一張table, column 用amount為索引, row用values set為索引 , 範例如下:

|           | 0    | 1    | 2       | 3       | 4         | 5         | 6                           | 7                |
| --------- | ---- | ---- | ------- | ------- | --------- | --------- | --------------------------- | ---------------- |
| [2]       | []   | None | [2]     | None    | [2,2]     | None      | [2,2,2]                     | None             |
| [2,3]     | []   | None | [**2**] | [**3**] | [**2,2**] | [**2**,3] | [2,2,2]<br />[**3**,3]      | [**2,2**,3]      |
| [2,3,6]   | []   | None | [2]     | [3]     | [2,2]     | [2,3]     | [2,2,2]<br />[3,3]<br />[6] | [2,2,3]          |
| [2,3,6,7] | []   | None | [2]     | [3]     | [2,2]     | [2,3]     | [2,2,2]<br />[3,3]<br />[6] | [2,2,3]<br />[7] |

第一欄和第一列可以直接填, 第一欄是amount = 0, 只有一種組合(不取value), 第一列則是因為只有一種value, 之後按照列填, 可以看到每格的答案都會包含上一列的組合(若有), 以及扣除最大幣值(若在範圍內)的組合, 填完表最右下的欄位就是答案



##### [(H)N-Queens](https://leetcode.com/problems/n-queens/)

Backtracking Algorithm ([參考教學 - 花花](https://youtu.be/Xa-yETqFNEQ), [參考教學 - Geeks](https://www.geeksforgeeks.org/n-queen-problem-backtracking-3/)), 可用遞迴的方式逐列執行, 我的感覺是有點像DFS, pseudo code如下, isSafe要檢查對角線可利用python的zip來達成, 或是用花花的對角線索引 (2n-1 = x + y or x - y + n -1):

```python
def solve(row, board, ans):
  if row == N:
      ans += board
      return
  for col in range(0, N):
      if not isSafe(row, col, board): continue
      board[row][col] = "Q" # 可以放就放 (有過上面檢查), 然後往下一列做
      solve(row + 1, col, board, ans) # 這邊會往下走各種分支, 直到終止 (無解或有解)
      board[row][col] = "." # 放完要清空, 看能否在下一行放 (也就是繼續看各分支)
  return
# 執行時用solve(0, 空棋盤, 空串列)
```
##### [(E)182. Duplicate Emails](https://leetcode.com/problems/duplicate-emails/)

這其實是SQL question, 利用GROUP BY和HAVING及COUNT來達成, 另外題目有指定只列email, 所以要選email不要用*
`SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email)>1;`	


### Reference

- https://leetcode.com/problemset/all/
- https://interviews.skype.com/zh/Interviews?code=72a9eaf2-a055-9048-1a18-b527fcb4fbad
- http://www.raychase.net/tag/leetcode
- https://codingcompetitions.withgoogle.com/codejam/archive
- [偷看幾摳的repo](https://github.com/eagle0401)
- [System Design](https://github.com/qiu-hanqiao/system-design-primer/blob/master/README.md)

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