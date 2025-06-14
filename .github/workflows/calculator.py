#Calculator app
def A(a, b):
  return a+b 

def B(a,b):
  return a-b

def C(a, b):
  return a*b

def D(a,b):
  if b == 0: 
    return "Error: Invalid output"
  else:
    return a/b 

diction = { "add" : "A", "subtract" : "B", "mulitply" : "C", "divide" :"D" } 

method_run = diction.get(value) 

print(method_run())


