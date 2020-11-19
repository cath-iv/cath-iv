class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = 0
        s_verif = set(s)
        if s_verif.issubset(roman):
            for i in range(0, len(s) - 1):
                if roman[s[i]] < roman[s[i + 1]]:
                    res -= roman[s[i]]
                else:
                    res += roman[s[i]]
            res += roman[s[-1]]
            if 0 < res < 4000:
                return res
            else:
                print('Введенное число не соответсвует заданному диапазону')
        else:
            print('Введены некорректные данные')


print('Введите римское число в диапазоне от 1 до 3999')
s = Solution()
print(s.romanToInt(input().upper()))