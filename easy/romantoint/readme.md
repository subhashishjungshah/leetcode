# 0013. Roman to Integer

🔗 [View on LeetCode](https://leetcode.com/problems/)

---

## 🧩 Problem Statement

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written from largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five, we subtract it making four. The same principle applies to the number nine, which is written as IX.

There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.

X can be placed before L (50) and C (100) to make 40 and 90.

C can be placed before D (500) and M (1000) to make 400 and 900.

Given a Roman numeral, convert it to an integer.

## 💡 Approach 1: Left-to-Right with Lookahead

We iterate through the string from left to right. For each character, we check if its value is less than the next character's. If so, we subtract its value; otherwise, we add it.
This approach leverages the subtraction rule in Roman numerals and avoids double-counting by smartly deciding when to subtract.

### Time Complexity: O(n)

### Space Complexity: O(1)
