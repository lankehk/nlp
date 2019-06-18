from mindmeld.components import QuestionAnswerer

qa = QuestionAnswerer('.')
qa.load_kb('myapp','companies','./data/companies.json')

print(qa.get(index = 'companies'))
qa2 = QuestionAnswerer('.')
qa2.load_kb('myapp','salary','./data/salary.json')

a = list(qa2.get(index = 'salary'))
print(a)
