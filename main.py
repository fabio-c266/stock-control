import sys
sys.path.insert(0, './login.py')
sys.path.insert(0, './stock.py')
sys.path.insert(0, './files.py')

import login
import stock
import files

files.handle_system_files()

authentication = login.authenticate_user()

if authentication:
  stock.initialize_system()