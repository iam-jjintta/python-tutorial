
import asyncio


def native_coroutine():
    print('네이티브 코루틴 호출')


loop = asyncio.get_event_loop()
loop.run_until_complete(native_coroutine())
loop.close()
