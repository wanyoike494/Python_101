import asyncio

#define a function that simulates a time-consumeing task
async def fetch_data(delay):
    print('fetching data')
    await asyncio.sleep(delay) #simulates an io operation with a sleep
    print('data fetched')
    return {'data': 'some data'}

#define another coroutine that calls the first coroutine
async def main():
    print('start of main coroutine')
    task = fetch_data(2)
    #await the fetch_data coroutine, pausing execution of main unti fetch_data completes
    result = await task
    print(f'received result {result}')
    print ('end of main coroutine')

#run the main coroutine
asyncio.run(main())