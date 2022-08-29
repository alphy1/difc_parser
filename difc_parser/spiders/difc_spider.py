import scrapy
from scrapy import Request
from difc_parser.items import DifcParserItem, DifcParserLoader
import difflib


class DIFCScrapy(scrapy.Spider):
    name = 'difc'

    def get_num_pages(self):
        companies = getattr(self, "companies", None)
        pages = getattr(self, "pages", None)
        num_pages = int(companies) // 10 if companies is not None else 2
        num_pages = int(pages) if pages is not None else num_pages
        return num_pages

    def start_requests(self):
        num_pages = self.get_num_pages()
        for page in range(1, num_pages + 1):
            request = Request.from_curl(
                f"""curl 'https://retailportal.difc.ae/api/v3/public-register/overviewList?page={page}&keywords 
                =&companyName=&registrationNumber=&type=&status=&latitude=0&longitude=0&sortBy=&difc_website=1
                &data_return=true &isAjax=true' -H 'authority: retailportal.difc.ae' -H 'accept: text/html, 
                */*; q=0.01' -H 'accept-language: ru-RU, ru;q=0.9,en-US;q=0.8,en;q=0.7' -H 'origin: 
                https://www.difc.ae' -H 'referer: https://www.difc.ae/' -H 'sec-ch-ua: "Chromium";v="104", 
                " Not A;Brand";v="99", "Google Chrome";v="104"' -H 'sec-ch-ua-mobile: ?0' -H 'sec-ch-ua-platform: 
                "Linux"' -H 'sec-fetch-dest: empty' -H 'sec-fetch-mode: cors' -H 'sec-fetch-site: same-site' -H 
                'user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 
                Safari/537.36' --compressed"""
            )
            yield request

    def parse(self, response, **kwargs):
        links = response.css("h4 a::attr(href)").getall()
        for link in links:
            link = link.replace("\\", "").replace('"', "")
            yield Request(url=link, callback=self.parse_companies_info)

    def get_key(self, row):
        key = row.css("p")[0].css("::text").get().split(':')[0].strip()
        possible_fields = difflib.get_close_matches(key, DifcParserItem.fields, n=1)
        if len(possible_fields) == 0:
            self.logger.warn(f"Cannot recognize key '{key}'")
            return
        return possible_fields[0]

    def get_value(self, row):
        value = None
        if len(row.css("p")) > 1:
            value = row.css("p")[1].css("::text").get()
            if value == "Not Applicable":
                value = None
        if value is not None:
            value = value.strip()
        return value

    def parse_companies_info(self, response):
        difc_loader = DifcParserLoader(item=DifcParserItem(), response=response)
        containers = response.css("div.register-detail div.container")
        for container in containers:
            for row in container.css("div.row div.row"):
                key = self.get_key(row)
                value = self.get_value(row)
                self.logger.info(f"Add key: '{key}' with value: '{value}'")
                difc_loader.add_value(key, value)

        return difc_loader.load_item()
