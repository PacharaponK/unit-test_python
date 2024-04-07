def caesarCipher(s, k):
    result=""
    for i in range(len(s)):
        if s[i].isalpha():
            if s[i].isupper():
              result+=chr(ord('A')+(ord(s[i])-ord('A')+k)%26)
            else:
              result+=chr(ord('a')+(ord(s[i])-ord('a')+k)%26)    
        else:
            result+=s[i]
    return result