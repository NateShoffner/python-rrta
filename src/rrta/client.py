import aiohttp
import logging
from typing import Dict
from rrta import models
from .adapter import RestAdapter
from .exceptions import MyStopApiException

class RRTAClient:
    def __init__(
        self, session: aiohttp.ClientSession, logger: logging.Logger = None
    ) -> None:
        self._logger = logger or logging.getLogger(__name__)
        self.session = session
        self.adapter = RestAdapter(
            self.session, hostname="busfinder.redrosetransit.com", base="InfoPoint/rest"
        )

    async def get_public_messages(self) -> list[models.messages.Message]:
        url = f"PublicMessages/GetCurrentMessages"
        return await self.__get_collection(endpoint=url, model=models.messages.Message)

    async def get_all_vehicles(self) -> list[models.vehicles.Vehicle]:
        """Get the routes from the server"""
        url = f"Vehicles/GetAllVehicles"
        return await self.__get_collection(endpoint=url, model=models.vehicles.Vehicle)

    async def get_vehicles(self, route_ids: list[int]) -> list[models.vehicles.Vehicle]:
        """Get the routes from the server"""
        url = (
            f'Vehicles/GetAllVehiclesForRoutes?routeIDs={",".join(map(str, route_ids))}'
        )
        return await self.__get_collection(endpoint=url, model=models.vehicles.Vehicle)

    async def get_all_routes(self) -> list[models.route.Route]:
        """Get all visible routes"""
        url = f"Routes/GetVisibleRoutes"
        return await self.__get_collection(endpoint=url, model=models.route.Route)

    async def get_route(self, id: int) -> models.route.Route:
        """Get a route by ID"""
        url = f"Routes/Get/{id}"
        return await self.__get_singular(endpoint=url, model=models.route.Route)

    async def get_all_route_details(self) -> list[models.routedetails.RouteDetails]:
        """Gets route details"""
        url = f"RouteDetails/GetAllRouteDetails"
        return await self.__get_collection(
            endpoint=url, model=models.routedetails.RouteDetails
        )

    async def get_route_details(self, id: int) -> models.routedetails.RouteDetails:
        """Gets route details for a specific route"""
        url = f"RouteDetails/Get/{id}"
        return await self.__get_singular(
            endpoint=url, model=models.routedetails.RouteDetails
        )

    async def get_all_stops(self) -> list[models.stops.Stop]:
        """Gets all stops"""
        url = f"Stops/GetAllStops"
        return await self.__get_collection(endpoint=url, model=models.stops.Stop)

    async def get_stop(self, id: int) -> models.stops.Stop:
        """Gets a stop by ID"""
        url = f"Stops/Get/{id}"
        return await self.__get_singular(endpoint=url, model=models.stops.Stop)

    async def get_stop_departures(
        self, id: int
    ) -> list[models.stopdepartures.StopDeparture]:
        """Gets the departures for a stop"""
        url = f"Stops/GetDepartures/{id}"
        return await self.__get_collection(
            endpoint=url, model=models.stopdepartures.StopDeparture
        )

    # Helper methods

    async def __get_singular(
        self, endpoint: str, model: type, ep_params: Dict = None
    ) -> object:
        """Generic method for getting a single object from the server"""
        try:
            result = await self.adapter.get(endpoint=endpoint, ep_params=ep_params)
        except MyStopApiException as e:
            return None

        # TODO - might want something more graceful to handle empty data
        if isinstance(result.data, list) and len(result.data) == 0:
            return None
        return model(**result.data)

    async def __get_collection(
        self, endpoint: str, model: type, ep_params: Dict = None
    ) -> list[object]:
        """Generic method for getting a collection of objects from the server"""
        collection = []
        try:
            result = await self.adapter.get(endpoint=endpoint, ep_params=ep_params)
        except MyStopApiException as e:
            return collection

        # TODO - might want something more graceful to handle empty data
        if isinstance(result.data, list) and len(result.data) == 0:
            return collection

        for item in result.data:
            collection.append(model(**item))
        return collection
