import asyncio

from secrets_module import xkcd_password


async def random_words(delay, total=2):
    """Can now use yield and await in the same method."""
    for i in range(total):
        yield xkcd_password(number_of_words=1)
        await asyncio.sleep(delay=delay)


async def get_words():
    async for word in random_words(delay=1, total=5):
        print(word)


async def a_comp(number_of_words):
    list_comp = [w async for w in random_words(delay=0.5, total=number_of_words)]
    print(list_comp)

loop = asyncio.get_event_loop()
loop.run_until_complete(get_words())

loop = asyncio.get_event_loop()
loop.run_until_complete(a_comp(number_of_words=3))
