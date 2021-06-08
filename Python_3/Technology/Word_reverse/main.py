# 역으로 문자를 저장하는 방법 (속도 순위: 1)
def is_palindrome(word):
    return word[::-1] == word


# 리스트를 reverse 함수를 사용하여, 변경하느 방법 (속도 순위: 2)
def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)


# 첫 문자부터 하나씩 저장하는 방법 (속도 순위: 3)
def reverse_for_loop(word):
    s1 = ''
    for c in word:
        # print(f"첫번째 문장: {c}")
        s1 = c + s1  # appending chars in reverse order
        # print(f"두번째 문장: {s1}")
    return s1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(reverse_for_loop("토마타"))
    # print(is_palindrome("racecar"))
    # print(is_palindrome("stars"))
    # print(is_palindrome("토마토"))
    # print(is_palindrome("kayak"))
    # print(is_palindrome("hello"))

