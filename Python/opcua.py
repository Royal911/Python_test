import asyncio
from asyncua import Client, Node, ua

async def main():
    url = "opc.tcp://UMTM14CUJ2501:4840"
    async with Client(url=url) as client:
        var = client.get_node("ns=4;s=DOPAC.CU_INF_Manual_Mode_L")
        print("My variable", var, await var.read_value())
if __name__ == '__main__':
    asyncio.run(main())