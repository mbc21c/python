import textwrap

if True:
    test = """\
    이런저런
    문자열을
    생성해요"""

print("- test:" , test)
print("- textwrap.dedent(test):", textwrap.dedent(test))
