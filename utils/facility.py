from typing import NamedTuple
import re
from rapidfuzz.process import extract
import discord
from discord import app_commands
from data import REGIONS, ITEM_SERVICES, VEHICLE_SERVICES


class FacilityLocation(NamedTuple):
    region: str
    coordinates: str


class LocationTransformer(app_commands.Transformer):
    async def transform(self, interaction: discord.Interaction, value: str) -> FacilityLocation:
        try:
            coordinates = re.search(
                r'([A-R]\d{1,2}k\d)', value, flags=re.IGNORECASE).group(1)
        except AttributeError:
            coordinates = ''

        for region in REGIONS:
            if region in value:
                region_name = region
                break
        try:
            return FacilityLocation(region_name, coordinates)
        except UnboundLocalError:
            await interaction.response.send_message(':x: No region found', ephemeral=True)
            raise ValueError('Incorrect region passed')


    async def autocomplete(self, interaction: discord.Interaction, current) -> list[app_commands.Choice]:
        res = extract(current, list(REGIONS), limit=25)
        return [app_commands.Choice(name=choice[0], value=choice[0])
                for choice in res]


class Facility:
    """Represents a facility
    """
    def __init__(self, *, id_: int = 0, name: str, description: str = '', region: str, coordinates: str = '', marker: str = '', maintainer: str, author: int, item_services: int = 0, vehicle_services: int = 0) -> None:
        self.id_ = id_
        self.name = name
        self.description = description
        self.region = region
        self.coordinates = coordinates
        self.marker = marker
        self.maintainer = maintainer
        self.author = author
        self.item_services = item_services
        self.vehicle_services = vehicle_services
        self.initial_hash = hash((self.__class__, id_, name, description, region, coordinates, marker, maintainer, author, item_services, vehicle_services))

    def changed(self) -> bool:
        """Determine whether the facility has changed from initial instance

        Returns:
            bool: If facility has changed
        """
        return self.initial_hash != hash((self.__class__, self.id_, self.name, self.description, self.region, self.coordinates, self.marker, self.maintainer, self.author, self.item_services, self.vehicle_services))

    def embed(self) -> discord.Embed:
        """Generates a embed for viewing the facility

        Returns:
            discord.Embed: Embed filled in with current state of facility
        """
        facility_location = f'> Region: `{self.region}`\n'
        if self.marker:
            facility_location += f'> Marker: `{self.marker}`\n'
        if self.coordinates:
            facility_location += f'> Coordinates: `{self.coordinates}`\n'

        embed = discord.Embed(title=self.name,
                              description=self.description,
                              color=0x54A24A)
        embed.add_field(name='Location', value=facility_location)
        embed.add_field(name='Maintainer', value=self.maintainer)
        embed.add_field(name='Author', value=f'<@{self.author}>')

        if self.id_:
            embed.set_footer(text=f'ID: {self.id_}')

        def format_services(service_tuple: tuple, services_number: int) -> str:
            formatted_services = '```ansi\n\u001b[0;32m'
            for index, service in enumerate(service_tuple):
                if (1 << index) & services_number:
                    formatted_services += f'{service}\n'
            formatted_services += '```'
            return formatted_services
        if self.item_services:
            formatted_services = format_services(ITEM_SERVICES, self.item_services)
            embed.add_field(name='Item Services', value=formatted_services)

        if self.vehicle_services:
            formatted_services = format_services(VEHICLE_SERVICES, self.vehicle_services)
            embed.add_field(name='Vehicle Services', value=formatted_services)
        return embed

    def select_options(self, vehicle: bool = False) -> list[discord.SelectOption]:
        """Generates select options with default set for the currently selected services

        Args:
            vehicle (bool, optional): Generate vehicle select options. Defaults to False.

        Returns:
            list[discord.SelectOption]: List of select options with defaults set based on current services
        """
        if vehicle:
            return self.__generate_options(self.vehicle_services, VEHICLE_SERVICES)
        return self.__generate_options(self.item_services, ITEM_SERVICES)

    def __generate_options(self, selected_services: int, available_services: tuple):
        return [discord.SelectOption(label=service, value=service, default=bool((1 << index) & selected_services))
                for index, service in enumerate(available_services)]

    def set_services(self, services: list[str], vehicle: bool = False) -> None:
        """Set services of facility

        Args:
            services (list[str]): List of services to set
            vehicle (bool, optional): If services are vehicle. Defaults to False.
        """
        if vehicle:
            self.vehicle_services = self.__generate_service_number(services, VEHICLE_SERVICES)
        else:
            self.item_services = self.__generate_service_number(services, ITEM_SERVICES)

    def __generate_service_number(self, selected_services: list[str], available_services: tuple) -> int:
        service_var = 0
        for index, service in enumerate(available_services):
            if service in selected_services:
                service_var += (1 << index)
        return service_var
