#Выполняю таск 3.6
visitors = ['Женя', 'Кристина', 'Данька']

visitors.insert(0, 'Руслан')
visitors.insert(2, 'Дима')
visitors.append('Ира')

print("К сожалению на обед приглашаются всего лишь два гостя...")
eror_visitors = visitors.pop()
print(eror_visitors+", я искренне сожалею об отмене приглашения...")
eror_visitors = visitors.pop()
print(eror_visitors+", я искренне сожалею об отмене приглашения...")
eror_visitors = visitors.pop()
print(eror_visitors+", я искренне сожалею об отмене приглашения...")
eror_visitors = visitors.pop()
print(eror_visitors+", я искренне сожалею об отмене приглашения...")
print(visitors[0]+", приглашение все еще в силе!")
print(visitors[1]+", приглашение все еще в силе!")

del visitors[1]
del visitors[0]
print(visitors)