# Definir uma função para converter uma expressão matemática em uma função Python
def expr_to_func(expr):
  # Substituir ^ por ** para representar a potência
  expr = expr.replace("^", "**")
  # Usar a função eval para avaliar a expressão como uma função Python
  def func(x):
    return eval(expr)
  # Retornar a função criada
  return func

# Definir uma função para compor duas funções
def compose(f, g):
  # Retornar uma função que aplica g e depois f
  return lambda x: f(g(x))

# Pedir ao usuário as expressões para f(x) e g(x)
f_expr = input("Digite a expressão para f(x): ")
g_expr = input("Digite a expressão para g(x): ")

# Converter as expressões em funções Python
f = expr_to_func(f_expr)
g = expr_to_func(g_expr)

# Criar as funções compostas
g_of_f = compose(g, f)
g_of_g = compose(g, g)
f_of_f = compose(f, f)
f_of_g = compose(f, g)

# Pedir ao usuário o valor de x e a operação desejada
x = float(input("Digite o valor de x: "))
op = input("Digite a operação desejada (gof, gog, fof ou fog): ")

# Executar a operação e mostrar o resultado
if op == "gof":
  print(f"(g ° f)({x}) = {g_of_f(x)}")
elif op == "gog":
  print(f"(g ° g)({x}) = {g_of_g(x)}")
elif op == "fof":
  print(f"(f ° f)({x}) = {f_of_f(x)}")
elif op == "fog":
  print(f"(f ° g)({x}) = {f_of_g(x)}")
else:
  print("Operação inválida.")