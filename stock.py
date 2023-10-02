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

def delete_product():
  if (len(products) == 0):
    print('Não possui nenhum produto cadastrado')
  else:
    avaliable_products = ''
    for index, product in enumerate(products):
      avaliable_products += f".{index} {product['name']}\n"

    product_to_delete = input(f"Digite o número produto que você deseja deletar:\n{avaliable_products}")
    if product_to_delete.isnumeric(): product_to_delete = int(product_to_delete)

    if not isinstance(product_to_delete, int) or product_to_delete > len(products):
      print('Valor inserido errado.')
    else:
      del products[product_to_delete]
      clear()

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
      print('Editar produto')
    elif option == 4:
      delete_product()
    elif option == 'sair' or option == 5:
      end_while = True 
