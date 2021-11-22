from datetime import datetime

async def loop1():
    for _ in range(1000):
        pass
    print('Loop 1')
async def loop2():
    for _ in range(1000):
        pass
    print('Loop 2')
async def loop3():
    for _ in range(1000):
        pass
    print('Loop 3')
async def loop4():
    for _ in range(1000):
        pass
    print('Loop 4')
async def loop5():
    for _ in range(1000):
        pass
    print('Loop 5')

print('##### Start Async Functions #####')
start_time = datetime.now()
loop1()
loop2()
loop3()
loop4()
loop5()
print(str(datetime.now() - start_time))
print('##### Done Async Functions #####')
