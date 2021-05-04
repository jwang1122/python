class Converter:
    def int_to_roman(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def roman_to_int(self, s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

if __name__ == '__main__':        
    x = 1
    print(f"Roman Numeral for integer {x} is {Converter().int_to_roman(x)}.")
    x = 4000
    print(f"Roman Numeral for integer {x} is {Converter().int_to_roman(x)}.")
    
    s = 'MMMCMLXXXVI'
    print(f"The integer for Roman Numeral {s} is {Converter().roman_to_int(s)}.")
    s = 'MMMM'
    print(f"The integer for Roman Numeral {s} is {Converter().roman_to_int(s)}.")
