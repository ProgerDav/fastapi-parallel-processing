import asyncio
import httpx

API_URL = "/sleep"


async def send(client: httpx.AsyncClient, i: int):
    print("SENDING REQUEST: ", i)
    response = await client.get(API_URL)
    print("REQUEST {} STATUSCODE {}".format(i, response.status_code))
    print("REQUEST {} RESPONSE {}".format(i, response.text))


async def run_requests():
    client = httpx.AsyncClient(base_url="http://localhost:8000", timeout=100000)
    cor = await asyncio.gather(*[send(client, i) for i in range(750)])

    await client.aclose()

    return cor


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    loop.run_until_complete(run_requests())
