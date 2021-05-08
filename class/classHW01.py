class Converter:
    def int_to_Roman(self, num):
        val = (
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        )
        syb = (
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        )
        roman_num = ''
        i = 0
        while  num > 0:
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
        return roman_num

    def roman2int(self, roman):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(roman)):
            if i > 0 and rom_val[roman[i]] > rom_val[roman[i - 1]]:
                int_val += rom_val[roman[i]] - 2 * rom_val[roman[i - 1]]
            else:
                int_val += rom_val[roman[i]]
        return int_val

print(Converter().int_to_Roman(5))
print(Converter().int_to_Roman(4000))
print(Converter().roman2int('DCLXXVI'))
