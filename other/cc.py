import string

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """

sstr = "A man, a plan, a canal: Panama"
lst = []

for s in sstr:
    if s not in punctuation:
        lst.append(str.lower(s))

''.join(lst) == ''.join(lst[::-1])


def aa(s):
    punct = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
    lst = [c.lower() for c in s if c not in punct]
    return ''.join(lst) == ''.join(lst[::-1])

print(aa('A man, a plan, a canal: Panama'))