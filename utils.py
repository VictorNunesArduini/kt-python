import json

y = {'nome': 'Victor', 'age': 24}
j = json.dumps(y)  # Dict -> String
print(j)

s = json.loads(j)  # String -> Dict
print(s['nome'])


