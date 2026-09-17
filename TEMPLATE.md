# 刷题提交模板

> 每做一道新题，复制下面的模板，改 6 个地方即可。

---

## 一、文件命名规范

```
专题目录/题号-英文题名.py
```

| 要求 | 正确 ✅ | 错误 ❌ |
|---|---|---|
| 题号补足 3 位 | `027-remove-element.py` | `27-remove-element.py` |
| 全小写 | `027-remove-element.py` | `027-Remove-Element.py` |
| 单词用 `-` 连接 | `026-remove-duplicates-from-sorted-array.py` | `026-Remove Duplicates.py` |
| 不要空格 | `001-two-sum.py` | `001-Two Sum.py` |

**专题目录**：`array` / `string` / `hash` / `linkedlist` / `stack-queue` / `tree` / `backtracking` / `dp` / `greedy` / `graph`

---

## 二、文件内容模板（复制这段）

```python
# 27. Remove Element / 移除元素
# 链接: https://leetcode.cn/problems/remove-element/
# 思路: 双指针，j 指向下一个要写入的位置，遍历时把不等于 val 的元素往前搬
# 复杂度: 时间 O(n) / 空间 O(1)
# 易错点: 返回的是 j（新长度），不是 len(nums)-j；原地修改不要新建数组

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
```

### 需要改的 6 个地方

| 位置 | 改成 |
|---|---|
| 第 1 行 | 题号 + 英文题名 + 中文题名 |
| 第 2 行 | 题目链接 |
| 第 3 行 | **自己的话**说清核心思路 |
| 第 4 行 | 时间/空间复杂度 |
| 第 5 行 | 边界条件、容易写错的地方 |
| 第 9~10 行 | 方法名、参数、返回类型（照抄 LeetCode 给的） |

> ⚠️ **注释不能空着。** 这四行是你两个月后复习、面试前过题的唯一依据。

---

## 三、提交命令模板（复制这段）

```powershell
git add .
git commit -m "feat: 027 移除元素"
git push
```

### commit message 格式

```
前缀: 题号 中文题名
```

| 前缀 | 什么时候用 | 例子 |
|---|---|---|
| `feat:` | 新增题解 | `feat: 027 移除元素` |
| `fix:` | 修改已有题解 | `fix: 001 补上哈希表解法` |
| `docs:` | 改文档 | `docs: 更新进度表` |
| `refactor:` | 重写代码（结果不变） | `refactor: 026 简化双指针写法` |

**一次提交多道题也行**：`feat: 027-028 两道数组题`

---

## 四、提交前自检（4 条）

- [ ] LeetCode 上点过「**提交**」并通过（不是只点「运行」）
- [ ] 文件名符合 `题号-英文题名.py`（全小写、连字符、题号 3 位）
- [ ] 顶部四要素注释写全，**没有留空**
- [ ] 代码里没有无用残留（多余的 `pass`、算出来没用的变量）

---

## 五、卡住时的排查顺序

```
1. git status              ← 先看状态，它永远告诉你发生了什么
2. 文件标签页有小圆点 ●？   ← 有圆点 = 没保存
3. 是不是不在仓库目录？      ← 看提示符有没有 dsa-practice
4. push 失败？             ← 重试一次；仍失败查「环境配置记录.md」
```
