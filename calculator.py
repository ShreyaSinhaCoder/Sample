import sys

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


if __name__ == "__main__":
    value = sys.argv[3]
    a = sys.argv[1]
    b = sys.argv[2]
    diction = { "add" : "A", "subtract" : "B", "mulitply" : "C", "divide" :"D" } 
    method_run = diction.get(value) 
    print(method_run(a, b))
