n = int(input())
queue = []

for i in range(n):
    operation = input()
    operation_parts = operation.split(' ')

    if operation_parts[0] == '1':
        queue.append(operation_parts[1])
    elif operation_parts[0] == '2':
        queue.pop(0)
    else:
        print(queue[0])
