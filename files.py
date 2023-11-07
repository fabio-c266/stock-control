import os
import json

def handle_system_files():
    products_path = './database/products.json'
    users_path = './database/users.json'

    if not os.path.exists(products_path):
        with open(products_path, 'w', encoding='utf') as file:
            json.dump([], file)

    if not os.path.exists(users_path):
        with open(users_path, 'w', encoding='utf') as file:
            json.dump([], file)

def get(path):
    file = open(path)
    dataJson = json.loads(file.read())

    return dataJson

def add(path, data):
    newData = get(path)
    newData.append(data)

    with open(path, 'w', encoding='utf') as file:
      json.dump(newData, file)

def update(path, index, data):
    fileData = get(path)
    fileData[index] = data

    with open(path, 'w', encoding='utf') as file:
      json.dump(fileData, file)

def remove(path, index):
    fileData = get(path)
    del fileData[index]

    with open(path, 'w', encoding='utf') as file:
      json.dump(fileData, file)

