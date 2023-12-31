import os
import sys

sys.path.insert(0, './files.py')

import files

clear = lambda: os.system('cls')
users = files.get('./database/users.json')

def validate_email_and_password(email, password):
  is_valid_fields = False

  for user in users:
    if user['email'] == email and user['password'] == password:
      is_valid_fields = True
      break

  return is_valid_fields

def authenticate_user():
  end_while = False
  attempts_wrong = 0
  while(not end_while):
    email = input('Insira suas credenciais de acesso. Você tera no máximo 3 tentivas de login, caso exceda o sitema irá se fechar:\nEmail: ')
    password = input('Senha: ')

    valid_authentication = validate_email_and_password(email, password)
    if attempts_wrong == 3:
      print('Você atingiu o número máximo de tentativas.')
      end_while
      return False
    elif not valid_authentication:
      attempts_wrong += 1
    else:
      end_while
      clear()
      return True
