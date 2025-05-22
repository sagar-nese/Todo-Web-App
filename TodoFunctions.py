def file_write(mytodolist):
    with open("TodoList.txt", 'w') as file_local:
        file_local.writelines(mytodolist)


def file_read():
    with open("TodoList.txt", 'r') as file_local:
        mytodolist = file_local.readlines()
    return mytodolist