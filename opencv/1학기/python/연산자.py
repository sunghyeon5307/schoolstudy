width=3
height=5
RectArea=width*height
TriangleArea=width*height/2

print(RectArea)
print(width, '*', height, '=', RectArea)

# 중괄호 {}를 이용해서 format method를 이용해 출력
print('{0} : {1}*{2}/2={3}'.format('Triangle Area', width, height, TriangleArea))