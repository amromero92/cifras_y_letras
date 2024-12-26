
## Números para jugar y objetivo
numeros = [6,50,9,8,4,10]
objetivo = 617
## En principio no tienes que cambiar más

## -----------------------------------------------------------

def evaluate_ops(numbers, operations):
    if len(operations) != len(numbers) - 1:
        raise ValueError("Number of operations must be one fewer than the number of numbers.")

    result = numbers[0]
    for i in range(len(operations)):
        if operations[i] == '+':
            result += numbers[i + 1]
        elif operations[i] == '-':
            result -= numbers[i + 1]
        elif operations[i] == '*':
            result *= numbers[i + 1]
        elif operations[i] == '/':
            if numbers[i + 1] == 0:
                raise ZeroDivisionError("Division by zero")
            result /= numbers[i + 1]
        else:
            raise ValueError(f"Supported operations are +,-,*,/")
    return result

def find_operations(numbers, target):
 from itertools import product, permutations
 ops = ['+', '-', '*', '/']

 for k in range(2,len(numbers)+1):
  for num_perm in permutations(numbers,k):
   for ops_perm in product(ops, repeat=k-1):
    if (evaluate_ops(num_perm, ops_perm) == target): return num_perm, ops_perm

 return None

def print_results(found_num, found_ops):
 result = "Operaciones: \n"
 res0 = found_num[0]
 res = res0
 for i in range(len(found_ops)):
  fop = found_ops[i]
  if fop == '+':
   res = res + found_num[i+1]
  elif fop == '-':
   res = res - found_num[i+1]
  elif fop == '*':
   res = res * found_num[i+1]
  else:
   res = res / found_num[i+1]

  result += str(i+1) + '. ' + str(res0) + fop + str(found_num[i+1]) + ' = ' + str(res) + '\n'
  res0 = res
  

 return result 


def print_head():
 print("==================================================================")
 print("  ____ _  __                         _         _                 ")
 print(" / ___(_)/ _|_ __ __ _ ___   _   _  | |    ___| |_ _ __ __ _ ___ ")
 print("| |   | | |_| '__/ _` / __| | | | | | |   / _ \ __| '__/ _` / __|")
 print("| |___| |  _| | | (_| \__ \ | |_| | | |__|  __/ |_| | | (_| \__ \ ")
 print(" \____|_|_| |_|  \__,_|___/  \__, | |_____\___|\__|_|  \__,_|___/")
 print("                             |___/                               ")
 print("==================================================================")

print_head()
print(" ")



print("Cifras: ", numeros)
print("Objetivo: ", objetivo)
print("\n")

nums_sol, ops_sol = find_operations(numeros, objetivo)


print( print_results(nums_sol, ops_sol) )







