''' function to check string is
palindrome or not'''
def isPalindrome(str):
    my_str = str.casefold()

    # reverse the string
    rev_str = reversed(my_str)

    # check if the string is equal to its reverse
    if list(my_str) == list(rev_str):
        return True
    else:
        return False


# main function
s = input("Enter the word you want to check\n")
ans = isPalindrome(s)

if (ans):
	print("Yes")
else:
	print("No")
