a,b,c = 2,3,0
"""
print(a ** b == b ** a) 
#false 2^3 = 8 3^2 = 9

print(a < b or b < a)
# only the second part of function is true so the function is true

print('dog' > 'cat' + 'mouse')
#true because dog ascii number is higher than cat and mouse combined

print('Car' < 'Train')
#true because train ascii is higher than car

print((a == b) and ((a * a < b * b) or (b < a) and (2 * a < b)))"""
#false              #true = false      #false         #true
#false because the and statement is false however, the second part is another and statement which has false thus making entire statement false
print((a <= b) or ((a * a < b * b) or (b < a) and (2 * a < b)))
