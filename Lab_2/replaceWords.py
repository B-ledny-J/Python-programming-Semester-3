import re

N = 5
text = ("Програміст — фахівець, що займається програмуванням, виконує розробку програмного забезпечення "
        "(в простіших випадках — окремих програм) для програмованих пристроїв, "
        "які, як правило містять один процесор чи більше")

words = list(re.finditer(r'\w+', text))
words1 = words[N-1]
words2 = words[19-N]

offset1, end1 = words1.span()
offset2, end2 = words2.span()
text = text[:offset1] + words2.group(0) + text[end1:offset2] + words1.group(0) + text[end2:]

print("Нове речення:", text)