# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field
from typing import Optional
from itemloaders.processors import MapCompose, TakeFirst
from scrapy.loader import ItemLoader


# ref: https://stackoverflow.com/questions/52259779/scrapy-spider-converts-float-int-to-string
def process_float_or_int(value):
    try:
        return eval(value)
    except:
        return value


class DifcParserLoader(ItemLoader):
    default_output_processor = TakeFirst()


class DifcParserItem(scrapy.Item):
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
        self.fields["Directors"]: Optional[str] = Field(default=None)
        self.fields["Shareholders"]: Optional[str] = Field(default=None)
        self.fields["Company Secretary"]: Optional[str] = Field(default=None)
        self.fields["DNFBP"]: Optional[str] = Field(default=None)
        self.fields["Financial Year End"]: Optional[str] = Field(default=None)
        self.fields["Share Capital"]: Optional[str] = Field(default=None)
        self.fields["Business activities"]: Optional[str] = Field(default=None)
        self.fields["Registered Number"]: Optional[int] = \
            Field(default=None, input_processor=MapCompose(lambda x: process_float_or_int(x)))
        self.fields["Registered offices"]: Optional[str] = Field(default=None)
        self.fields["Data Protection Officer Appointed"]: Optional[str] = Field(default=None)
        self.fields["Personal Data Processing Operations"]: Optional[str] = Field(default=None)
        self.fields["Transfer of Personal Data from the DIFC"]: Optional[str] = Field(default=None)
        self.fields["Processing of Special Categories of Personal Data"]: Optional[str] = Field(default=None)
