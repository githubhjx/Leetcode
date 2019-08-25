“”“
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
”“”

# 动态规划法
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        if size <= 1:
            return s
        # 二维 dp 问题
        # 状态：dp[l,r]: s[l:r] 包括 l，r ，表示的字符串是不是回文串
        # 设置为 None 是为了方便调试，看清楚代码执行流程
        dp = [[False for _ in range(size)] for _ in range(size)]

        longest_l = 1
        res = s[0]

        # 因为只有 1 个字符的情况在最开始做了判断
        # 左边界一定要比右边界小，因此右边界从 1 开始
        for r in range(1, size):
            for l in range(r):
                # 状态转移方程：如果头尾字符相等并且中间也是回文
                # 在头尾字符相等的前提下，如果收缩以后不构成区间（最多只有 1 个元素），直接返回 True 即可
                # 否则要继续看收缩以后的区间的回文性
                # 重点理解 or 的短路性质在这里的作用
                if s[l] == s[r] and (r - l <= 2 or dp[l + 1][r - 1]):
                    dp[l][r] = True
                    cur_len = r - l + 1
                    if cur_len > longest_l:
                        longest_l = cur_len
                        res = s[l:r + 1]
            # 调试语句
            # for item in dp:
            #     print(item)
            # print('---')
        return res
 

# 中心扩散法，易理解
class Solution:
    def longestPalindrome(self, s):
        size = len(s)
        if size == 0:
            return ''

        # 至少是 1
        longest_palindrome = 1
        longest_palindrome_str = s[0]

        for i in range(size):
            palindrome_odd, odd_len = self.__center_spread(s, size, i, i)
            palindrome_even, even_len = self.__center_spread(s, size, i, i + 1)

            # 当前找到的最长回文子串
            cur_max_sub = palindrome_odd if odd_len >= even_len else palindrome_even
            if len(cur_max_sub) > longest_palindrome:
                longest_palindrome = len(cur_max_sub)
                longest_palindrome_str = cur_max_sub

        return longest_palindrome_str

    def __center_spread(self, s, size, left, right):
        """
        left = right 的时候，此时回文中心是一条线，回文串的长度是奇数
        right = left + 1 的时候，此时回文中心是任意一个字符，回文串的长度是偶数
        """
        l = left
        r = right

        while l >= 0 and r < size and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r], r - l - 1

# Manacher 算法
public class Solution {

/**
 * 创建分隔符分割的字符串
 *
 * @param s      原始字符串
 * @param divide 分隔字符
 * @return 使用分隔字符处理以后得到的字符串
 */
private String generateSDivided(String s, char divide) {
    int len = s.length();
    if (len == 0) {
        return "";
    }
    if (s.indexOf(divide) != -1) {
        throw new IllegalArgumentException("参数错误，您传递的分割字符，在输入字符串中存在！");
    }
    StringBuilder sBuilder = new StringBuilder();
    sBuilder.append(divide);
    for (int i = 0; i < len; i++) {
        sBuilder.append(s.charAt(i));
        sBuilder.append(divide);
    }
    return sBuilder.toString();
}

public String longestPalindrome(String s) {
    int len = s.length();
    if (len == 0) {
        return "";
    }
    String sDivided = generateSDivided(s, '#');
    int slen = sDivided.length();
    int[] p = new int[slen];
    int mx = 0;
    // id 是由 mx 决定的，所以不用初始化，只要声明就可以了
    int id = 0;
    int longestPalindrome = 1;
    String longestPalindromeStr = s.substring(0, 1);
    for (int i = 0; i < slen; i++) {
        if (i < mx) {
            // 这一步是 Manacher 算法的关键所在，一定要结合图形来理解
            // 这一行代码是关键，可以把两种分类讨论的情况合并
            p[i] = Integer.min(p[2 * id - i], mx - i);
        } else {
            // 走到这里，只可能是因为 i = mx
            if (i > mx) {
                throw new IllegalArgumentException("程序出错！");
            }
            p[i] = 1;
        }
        // 老老实实去匹配，看新的字符
        while (i - p[i] >= 0 && i + p[i] < slen && sDivided.charAt(i - p[i]) == sDivided.charAt(i + p[i])) {
            p[i]++;
        }
        // 我们想象 mx 的定义，它是遍历过的 i 的 i + p[i] 的最大者
        // 写到这里，我们发现，如果 mx 的值越大，
        // 进入上面 i < mx 的判断的可能性就越大，这样就可以重复利用之前判断过的回文信息了
        if (i + p[i] > mx) {
            mx = i + p[i];
            id = i;
        }

        if (p[i] - 1 > longestPalindrome) {
            longestPalindrome = p[i] - 1;
            longestPalindromeStr = sDivided.substring(i - p[i] + 1, i + p[i]).replace("#", "");
        }
    }
    return longestPalindromeStr;
}
}
