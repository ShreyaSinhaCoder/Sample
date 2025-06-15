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
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    if value == "add":
      print(A(a,b))
    elif value == "subtract":
      print(B(a,b))
    elif value == "multiply":
      print(C(a,b))
    else:
      print(D(a,b))
    
    #print(method_run(a, b))
