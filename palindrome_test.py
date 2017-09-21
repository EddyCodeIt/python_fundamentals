
# Ref.: https://stackoverflow.com/questions/17331290/how-to-check-for-palindrome-using-python-logic

# In python language, this problem is relitevly easy to solve if you know the
# approach python uses to inverting a string.
# What we need to do is to check if a passed string is equals to an
# inverted representation of this string
# [::-1] is a peace of code that takes care of inverting a string.
# Check script reverse_string.py to see how it works

def isItPalindrome(word):
    if(str(word) == str(word)[::-1]):
        return True
    else:
        return False

print(isItPalindrome("asdcdsa"))

