from easyocr import Reader

reader = Reader(['en']) # specify the language  

result1 = reader.readtext('name.jpg')
result2 = reader.detect('name.jpg')
result3 = reader.recognize('name.jpg')

print("Readtext:")
for (bbox, text, prob) in result1:
    print(f'Text: {text}, Probability: {prob}')

print("Detect:")
for (bbox, text, prob) in result2:
    print(f'Text: {text}, Probability: {prob}')

print("Recognize:")
for (bbox, text, prob) in result3:
    print(f'Text: {text}, Probability: {prob}')