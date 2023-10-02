import sys
sys.path.insert(0, './login.py')
sys.path.insert(0, './stock.py')

import login
import stock

authentication = login.authenticate_user()

if authentication:
  stock.initialize_system()