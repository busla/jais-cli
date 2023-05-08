from typing import Any, List, Optional

from pydantic import BaseModel, Field, root_validator


class Language(BaseModel):
    is_: Optional[str] = Field(default=None, alias="is")
    en: Optional[str] = None


class Translation(BaseModel):
    code: Optional[str] = None
    name: Optional[Language] = None


class LocationName(BaseModel):
    nominative: Optional[str] = None
    dative: str


class Entity(Translation):
    _type: str = Field(..., alias="type")


class Address(BaseModel):
    street: Optional[LocationName] = None
    postal_code: Optional[int] = None
    town: Optional[LocationName] = None
    country: Entity
    municipality: Optional[str] = None


class InternationalAddress(BaseModel):
    street: Optional[str] = None
    place: Optional[str] = None
    country: Optional[Entity] = None


class Receiver(BaseModel):
    kennitala: Optional[str] = None
    name: str


class VskItem(BaseModel):
    vsk_number: str
    isat: Translation
    opened: str
    closed: Optional[str] = None


class SeeAlso(BaseModel):
    search: str


class Business(BaseModel):
    """Business model used for json input"""

    type: str
    kennitala: str
    full_name: str
    short_name: str
    alt_foreign_name: Optional[str] = None
    is_company: bool
    business_type: Entity
    business_activity: Optional[str] = None
    parent_company_kennitala: Optional[str] = None
    director: Optional[str] = None
    legal_address: Optional[Address] = None
    postal_address: Optional[Address] = None
    international_address: Optional[InternationalAddress] = None
    receiver: Optional[Receiver] = None
    currency: Optional[str] = None
    share_capital: Optional[int] = None
    remarks: Optional[str] = None
    banned: bool
    isat: Optional[Entity] = None
    vsk: Optional[List[VskItem]] = None
    date_bankrupt: Optional[str] = None
    date_established: Optional[str] = None
    registered_at: str
    modified_at: Optional[str] = ""
    updated_at: str
    see_also: SeeAlso

    @property
    def address_out(self) -> str | None:
        if self.postal_address and self.postal_address.street:
            return self.postal_address.street.dative

    @property
    def business_type_out(self) -> str | None:
        if self.isat and self.isat.name and self.isat.name.is_:
            return self.isat.name.is_

    @property
    def business_type_code_out(self) -> str | None:
        return self.business_type.code


# class BusinessOut(Business):
#     """Business model used for serialization."""

#     class Config:
#         json_encoders = {Decimal: lambda v: float(round(v, 2))}


class Meta(BaseModel):
    api_version: int
    first_item: int
    last_item: int
    total_items: int


class Response(BaseModel):
    items: list[Business]
    meta: Meta
