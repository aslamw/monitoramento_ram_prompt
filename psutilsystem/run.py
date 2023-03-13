from psutil import virtual_memory, swap_memory


def bytes_to_gigas(value):
    return f'{value/1024/1024/1024: .2f}GB'

print(bytes_to_gigas(virtual_memory().used))
print('ram in disc (swap)' + bytes_to_gigas(swap_memory().used))