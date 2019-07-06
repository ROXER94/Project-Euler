# Calculates the sum of numbers under 1,000,000 that are palindromes in both decimal and binary

# Determines if a number is palindromic
def palindrome(n):
    return str(n) == str(n)[::-1]

palindromes = [i for i in range(1,1000000) if palindrome(i)]
binary = [int(bin(i)[2:]) for i in palindromes]
print(sum([int(str(i),2) for i in [j for j in binary if palindrome(j)]]))
