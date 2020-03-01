import asyncio
import random
import websockets

async def sentence(websocket, path):
    nouns = ("billie", "justin", "rob", "julia", "sarah")
    verbs = ("runs", "hits", "jumps", "drives", "barfs","sings","stabs","cries","pokes","stalks")
    adv = ("crazily.", "drunkenly.", "foolishly.", "merrily.", "occasionally.")
    while True:
        num1 = random.randrange(0,len(nouns))
        num2 = random.randrange(0,len(verbs))
        num3 = random.randrange(0,len(adv))
        now = nouns[num1] + ' ' + verbs[num2] + ' ' + adv[num3]
        await websocket.send(now)
        await asyncio.sleep(random.random() * 5)

start_server = websockets.serve(sentence, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
