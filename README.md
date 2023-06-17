# python-rrta

Python wrapper for the RRTA (MyStop) REST API.

## Usage

```python
import aiohttp
import asyncio
from rrta import RRTAClient

async def main():
    session = aiohttp.ClientSession()
    client = RRTAClient(session=session)

    routes = await client.get_all_routes()

    for route in routes:
        vehicles = await client.get_vehicles(route_ids=[route.RouteId])

        print(f"Route {route.RouteId}: {len(vehicles)} Vehicles")

        for v in vehicles:
            print(f"\t{v.VehicleId} currently en-route to {v.Destination} at {v.Speed} MPH")

if __name__ == "__main__":
    asyncio.run(main())

```

## Installation

    pip install rrta

## Known Issues

* Dataclasses are not pythonic at the moment and contain a bunch of member variables that RRTA doesn't seem to use despite being part of the MyStop spec