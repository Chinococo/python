word = input('輸入要檢查的英文單字:')
if not word.isalpha():
    print('這個單字不是英文')
elif word.lower()==word:
    print('這個單字全部都是小寫.')
elif word.upper()==word:
    print('這個單字全部都是大寫.')
else:
    print('這個單字是大小寫混合.')