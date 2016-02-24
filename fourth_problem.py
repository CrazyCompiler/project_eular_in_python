
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrome(number):
    return str(number)[::-1] == str(number)


def getLargstPalindrome():
    i=999
    palyndromList = [];

    while i>=100:
        j=999
        while j>=100:
            product = i*j
            if isPalindrome(product):
                palyndromList.append(product)
            j -= 1
        i -= 1
    return palyndromList



print max(getLargstPalindrome())
