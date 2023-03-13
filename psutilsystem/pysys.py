from time import sleep
from dashing import HSplit, VSplit, VGauge
from psutil import virtual_memory

ui = HSplit(#ui
    VSplit( #ui.items[0]
           VGauge(title='RAM'), #ui.item[0].item[1]
           title='Memória',
           border_color=3
           
           
        
    ),
)

while True:
    # memoria
    mem = ui.items[0]
    
    #Ram
    ram = mem.items[0]
    ram.value = virtual_memory().percent
    ram.title = f'RAM {ram.value}%'
    try:
        ui.display()
        sleep(1)
        
    except KeyboardInterrupt:
        break