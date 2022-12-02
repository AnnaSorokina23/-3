def delete(list_, index=None):
    if index is None:  # Условие при котором индек не задан пользователем
        return list_[:-1]  # Список без последнего элемента
    else:
        return list_[:index] + list_[index + 1:]  # Удаление элемента по индексу из списка


print(delete([0, 1, 2], index=0))  # [1, 2]
print(delete([0, 1, 2], index=1))  # [0, 2]
print(delete([0, 1, 2]))  # [0, 1]

