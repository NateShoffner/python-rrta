import aiohttp
import asyncio
from src.rrta.client import RRTAClient


async def main():
    session = aiohttp.ClientSession()
    client = RRTAClient(session=session)

    routes = await client.get_all_routes()

    for route in routes:
        vehicles = await client.get_vehicles(route_ids=[route.RouteId])

        print(f"Route {route.RouteId}: {len(vehicles)} Vehicles")

        if len(vehicles) == 0:
            continue

        for v in vehicles:
            print(
                f"\t{v.VehicleId} currently en-route to {v.Destination} at {v.Speed} MPH"
            )


if __name__ == "__main__":
    asyncio.run(main())
