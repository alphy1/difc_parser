# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from typing import Optional


class CompanyInformation(scrapy.Item):

    def __init__(self):
        super().__init__()
        self.fields["Name"]: Optional[str] = Field(default=None)
        self.fields["Trading Name"]: Optional[str] = Field(default=None)
        self.fields["Status of Registration"]: Optional[str] = Field(default=None)
        self.fields["Type of License"]: Optional[str] = Field(default=None)
        self.fields["Type of Entity"]: Optional[str] = Field(default=None)
        self.fields["Legal Structure"]: Optional[str] = Field(default=None)
        self.fields["Date of Incorporation"]: Optional[str] = Field(default=None)
        self.fields["Commercial License Validity Date"]: Optional[str] = Field(default=None)
        self.fields["Directors"]: Optional[list] = Field(default=None)
        self.fields["Shareholders"]: Optional[list] = Field(default=None)
        self.fields["dnfbp"]: Optional[str] = Field(default=None)
        self.fields["Financial Year End"]: Optional[str] = Field(default=None)
        self.fields["Share Capital"]: Optional[str] = Field(default=None)


class DataProtection(scrapy.Item):
    def __init__(self):
        super().__init__()
        self.fields["Data Protection Officer Appointed"]: Optional[str] = Field(default=None)
        self.fields["Personal Data Processing Operations"]: Optional[str] = Field(default=None)
        self.fields["Transfer of Personal Data from the DIFC"]: Optional[str] = Field(default=None)
        self.fields["Processing of Special Categories of Personal Data"]: Optional[str] = Field(default=None)


class DifcParserItem(scrapy.Item):
    def __init__(self):
        super().__init__()
        self.fields["company_name"]: Optional[str] = Field(default=None)
        self.fields["Status of registration"]: Optional[str] = Field(default=None)
        self.fields["Business activities"]: Optional[list] = Field(default=None)
        self.fields["Registered Number"]: Optional[int] = Field(default=None)
        self.fields["Registered Offices"]: Optional[list] = Field(default=None)
        self.fields["company_information"]: Optional[CompanyInformation] = Field(default=None)
        self.fields["data_protection"]: Optional[DataProtection] = Field(default=None)
