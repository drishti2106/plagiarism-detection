Plagiarism Detection System (LCS-Based)

A terminal-based Python utility to detect code similarity using Longest Common Subsequence (LCS) of tokens. Built as a DSA Final Project to help evaluate and compare student submissions with clarity and accuracy.

---

Features

1. Comment-aware Preprocessing: Strips out single-line and multi-line comments while preserving structure.
2. Tokenization: Converts code into logical token sequences to focus on logic over formatting.
3. LCS-Based Similarity Metric: Uses dynamic programming to measure real similarity (%).
4. Cleaned Code View: View normalized versions of compared files.
5. Smart Suggestions: Offers helpful advice for reducing detected similarity.
6. Color-coded CLI: Clear terminal output with colored similarity levels (High, Medium, Low).

---

Working

1. You input a reference file (e.g., ref_factorial.py).
2. You choose how many files you want to compare with.
3. For each file, the tool:
   - Loads and cleans the code.
   - Tokenizes and compares it with reference using LCS.
   - Reports similarity percentage.
   - Optionally shows cleaned version and improvement tips.

---

Installation

This is a pure Python 3 project — no external libraries needed!

---

Prerequisites

Python 3.6+

---
