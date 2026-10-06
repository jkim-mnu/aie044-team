# calc 의 덧셈과 뺄셈이 맞는지 검사한다
from calc import add, sub

if add(2, 3) == 5 and sub(5, 3) == 2:
    print("정상")
    raise SystemExit(0)
print("고장: add(2, 3) ->", add(2, 3))
raise SystemExit(1)
