class Solution:
    def __init__(self):
        self.lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num //= 1000
        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.lessThan20[num] + " "
        elif num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.lessThan20[num // 100] + " Hundred " + self.helper(num % 100)

class Solution:
    ''' ANOTHER '''
    def numberToWords(self, num):
        thousands = ['', 'Thousand', 'Million', 'Billion']
        tens = ['', 'ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        less_than_20 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 
                'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

        def helper(num):
            if num < 20:
                return less_than_20[num]
            elif num < 100:
                return tens[num // 10] + " " + less_than_20[num % 10]
            else:
                return ' '.join([less_than_20[num // 100], 'Hundred', helper(num % 100)])

        count = 0  # to see which index in thousands to use
        result = ''
        if num == 0:
            return 'Zero'

        while num > 0:
            if num % 1000 == 0:
                count += 1
                num //= 1000
                continue
            result = ' '.join([helper(num % 1000).strip(), thousands[count], result]).strip()
            count += 1
            num //= 1000
        return result.strip()

# Python 2 Solution, bug: Line 41: TypeError: slice indices must be integers or None or have an __index__ method
# class Solution2:
#     ''' RECURSIVE '''
#     def numberToWords2(self, num):
#         to19 = 'One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve ' \
#                'Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen'.split()
#         tens = 'Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety'.split()

#         def words(n):
#             if n < 20:
#                 return to19[n-1:n]
#             if n < 100:
#                 return [tens[n//10-2]] + words(n % 10)
#             if n < 1000:
#                 return [to19[n//100-1]] + ['Hundred'] + words(n % 100)
#             for p, w in enumerate(('Thousand', 'Million', 'Billion'), 1):
#                 if n < 1000**(p+1):
#                     return words(n/1000**p) + [w] + words(n%1000**p)
#         return ' '.join(words(num)) or 'Zero'
