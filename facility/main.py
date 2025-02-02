from typing import Optional
import discord
from data import ITEM_SERVICES, VEHICLE_SERVICES


class Facility:
    """Represents a facility

    Args:
        id_ (int, optional): ID
        name (str): Name
        description (str, optional): Description
        region (str): Region
        coordinates (str, optional): Coordinates within region
        marker (str): Location in region
        maintainer (str): Maintainer
        author (int): Author ID
        item_services (int, optional): Item services
        vehicle_services (int, optional): Vehicle services
        creation_time (int, optional): Creation time of facility
        guild_id (int): Guild facility was created in
    """

    def __init__(
        self,
        *,
        name: str,
        region: str,
        marker: str,
        maintainer: str,
        author: int,
        guild_id: int,
        **options,
    ) -> None:
        self.id_: Optional[int] = options.pop("id_", None)
        self.name: str = name
        self.description: Optional[str] = options.pop("description", None)
        self.region: str = region
        self.coordinates: Optional[str] = options.pop("coordinates", None)
        self.marker: str = marker
        self.maintainer: str = maintainer
        self.author: int = author
        self.item_services: Optional[int] = options.pop("item_services", 0)
        self.vehicle_services: Optional[int] = options.pop("vehicle_services", 0)
        self.creation_time: Optional[int] = options.pop("creation_time", None)
        self.guild_id: int = guild_id
        self.initial_hash: int = self.__current_hash()

    def __current_hash(self) -> int:
        return hash(
            (
                self.__class__,
                self.id_,
                self.name,
                self.description,
                self.region,
                self.coordinates,
                self.marker,
                self.maintainer,
                self.author,
                self.item_services,
                self.vehicle_services,
            )
        )

    def changed(self) -> bool:
        """Determine whether the facility has changed from initial instance

        Returns:
            bool: If facility has changed
        """
        return self.initial_hash != self.__current_hash()

    def embed(self) -> discord.Embed:
        """Generates a embed for viewing the facility

        Returns:
            discord.Embed: Embed filled in with current state of facility
        """
        facility_location = f"> Region : {self.region}\n> Marker : {self.marker}\n"
        if self.coordinates:
            facility_location += f"> Coordinates : {self.coordinates}\n"

        creation_info = f"> Author : <@{self.author}>\n> Guild ID : {self.guild_id}\n"
        if self.creation_time:
            creation_info += f"> Created : <t:{self.creation_time}:R>\n"
        if self.id_:
            creation_info += f"> ID : {self.id_}\n"

        embed = discord.Embed(
            title=self.name, description=self.description, color=0x54A24A
        )
        embed.add_field(name="Location:", value=facility_location)
        embed.add_field(name="Maintainer:", value=self.maintainer)
        embed.add_field(name="Creation Info:", value=creation_info)

        embed.set_footer(text="Source Code: https://github.com/thecuz1/FacilityLocator")

        def format_services(service_tuple: tuple, services_number: int) -> str:
            formatted_services = "```ansi\n\u001b[0;32m"
            for index, service in enumerate(service_tuple):
                if (1 << index) & services_number:
                    formatted_services += f"{service}\n"
            formatted_services += "```"
            return formatted_services

        if self.item_services:
            formatted_services = format_services(ITEM_SERVICES, self.item_services)
            embed.add_field(name="Item Services:", value=formatted_services)

        if self.vehicle_services:
            formatted_services = format_services(
                VEHICLE_SERVICES, self.vehicle_services
            )
            embed.add_field(name="Vehicle Services:", value=formatted_services)
        return embed

    def select_options(self, vehicle: bool = False) -> list[discord.SelectOption]:
        """Generates select options with defaults set for the currently selected services

        Args:
            vehicle (bool, optional): Generate vehicle select options. Defaults to False.

        Returns:
            list[discord.SelectOption]: List of select options with defaults set based on current services
        """
        if vehicle:
            return self.__generate_options(self.vehicle_services, VEHICLE_SERVICES)
        return self.__generate_options(self.item_services, ITEM_SERVICES)

    def __generate_options(
        self, selected_services: int | None, available_services: tuple
    ):
        try:
            return [
                discord.SelectOption(
                    label=service,
                    value=service,
                    default=bool((1 << index) & selected_services),
                )
                for index, service in enumerate(available_services)
            ]
        except TypeError:
            return [
                discord.SelectOption(label=service, value=service)
                for service in available_services
            ]

    def set_services(self, services: list[str], vehicle: bool = False) -> None:
        """Set services of facility

        Args:
            services (list[str]): List of services to set
            vehicle (bool, optional): If services are vehicle. Defaults to False.
        """
        if vehicle:
            self.vehicle_services = self.__generate_service_number(
                services, VEHICLE_SERVICES
            )
        else:
            self.item_services = self.__generate_service_number(services, ITEM_SERVICES)

    def __generate_service_number(
        self, selected_services: list[str], available_services: tuple
    ) -> int | None:
        service_var = 0
        for index, available_service in enumerate(available_services):
            if available_service in selected_services:
                service_var += 1 << index
        return service_var

    def can_modify(self, interaction: discord.Interaction) -> bool:
        """Returns true if the passed interaction has the ability to modify the facility

        Args:
            interaction (discord.Interaction): The interaction to check

        Returns:
            bool: Whether the facility can be modified
        """
        if self.author == interaction.user.id:
            return True
        if (
            interaction.guild_id == self.guild_id
            and interaction.permissions.manage_guild
        ):
            return True
        return False
