import easyocr
reader = easyocr.Reader(['en'], gpu= True)
results = reader.readtext('math.jpg')

# print(results)

text = ''
for result in results:
    text+= result[1] + ''
print(text)
result = eval(text)
print(result)