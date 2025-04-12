# <problem-number>. <problem-title>

🔗 [View on LeetCode](https://leetcode.com/problems/<slug>/)

---

## 🧩 Problem Statement

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

An integer is a palindrome when it reads the same backward as forward.

## 💡 Approach 1: Description

We convert the integer to a string and check if the string is the same when reversed. This is the most straightforward and readable approach.

### Time Complexity: O(n)

### Space Complexity: O(n)

## Approach 2: Reverse Half of the Number (Optimized)

We can optimize the approach by only reversing half of the number. This is because if the number is a palindrome, then the first half of the digits will be the same as the second half of the digits when reversed.

### Time Complexity: O(log n)

### Space Complexity: O(1)
