import id3 as model

data = model.pd.read_excel('alexandr.xls')
target = 'y'

answer = model.get_answer(data, list(data.columns), target, True)
print('\n======================')
print('---Финальное дерево---')
model.pprint(answer)
