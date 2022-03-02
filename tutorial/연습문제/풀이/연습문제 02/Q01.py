
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

# 결과: shirt
# 이유: 'shirt' 라는 문자열은 a에 없기 때문에 조건식이 참이 된다.
