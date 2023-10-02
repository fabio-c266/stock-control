import os
import pandas

clear = lambda: os.system('cls')
products = []

def add_product():
  name = input('Digite o nome do produto: ')

  if name in products:
    print('Já possui um produto com esse nome')
    clear()
  else:
    category = input('Digite a categoria desse produto: ')
    amount = input('Digite a quantidade desse produto em estoque: ')

    if not amount.isnumeric():
      print('Apenas utilize números na quantidade em estoque')
    else:
      amount = int(amount)

      if amount < 1:
        print('Quantidade inválida.')
      else:
        products.append({
          'name': name,
          'category': category,
          'amount': amount
        })

def get_products():
  if len(products) == 0:
    print('Não possui nenhum produto cadastrado.')
  else:
    products_names = []
    products_categories = []
    products_amount = []

    for product in products:
      products_names.append(product['name'])
      products_categories.append(product['category'])
      products_amount.append(product['amount'])
    
    table = pandas.DataFrame({
      'Produto': products_names,
      'Categoria': products_categories,
      'Quantidade': products_amount
    })

    print('=' * 80)
    print(table)
    print('=' * 80)

def alter_product():
  if not have_products():
    print('Não possui nenhum produto cadastrado')
  else:
    product_target = input(f"Digite o número produto que você deseja alterar:\n{available_products()}")
    if product_target.isnumeric():
      product_target = int(product_target)

    if not isinstance(product_target, int) or (product_target < 0 or product_target > len(products)):
      print('Valor inserido errado.')
    else:
      field = (input('Qual informação você alterar?\n- Nome\n- Categoria\n- Quantidade\n')).lower()
      if field == 'nome':
        new_name = input('Digite o novo nome desse produto: ')
        if new_name in products:
          print('Já possui um produto com esse nome')
        else:
          products[product_target]['name'] = new_name
          clear()

      elif field == 'categoria':
        new_category = input('Qual a nova categoria desse produto: ')
        products[product_target]['category'] = new_category
        clear()
      elif field == 'quantidade':
        new_amount = input('Qual a nova quantidade desse produto: ')
        if not new_amount.isnumeric():
          print("Apenas utilize números")
        else:
          products[product_target]['amount'] = int(new_amount)
      else:
        print('Informação inválida')

def delete_product():
  if not have_products():
    print('Não possui nenhum produto cadastrado')
  else:
    product_to_delete = input(f"Digite o número produto que você deseja deletar:\n{available_products()}")
    if product_to_delete.isnumeric():
      product_to_delete = int(product_to_delete)
    if not isinstance(product_to_delete, int) or (product_to_delete < 0 or product_to_delete > len(products)):
      print('Valor inserido errado.')
    else:
      del products[product_to_delete]
      clear()

def have_products():
  if len(products) == 0:
    return False
  else:
    return True

def available_products():
  available = ''
  for index, product in enumerate(products):
    available += f".{index} {product['name']}\n"

  return available

def initialize_system():
  end_while = False

  while (not end_while):
    option = input('Digite um número:\n1. Adicionar produto\n2. Ver estoque\n3. Editar produto\n4. Deletar produto\n5. Sair\n')

    if option.isnumeric(): 
      option = int(option)

    if option == 1:
      add_product()
    elif option == 2:
      get_products()
    elif option == 3:
      alter_product()
    elif option == 4:
      delete_product()
    elif option == 'sair' or option == 5:
      end_while = True 
