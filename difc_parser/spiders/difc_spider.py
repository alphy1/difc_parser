import scrapy
from scrapy import Request


class DIFCScrapy(scrapy.Spider):
    name = 'difc'
    num_pages = 2

    def start_requests(self):
        for page in range(1, self.num_pages + 1):
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
            self.log(f"Requested page {page}")
            yield request

    def parse(self, response, **kwargs):
        links = response.css("h4 a::attr(href)").getall()
        page = response.url.split("/")[-1].split('&')[0].split('=')[-1]
        filename = f'page-{page}.html'
        with open(filename, 'w') as f:
            for link in links:
                f.write(link+'\n')
                print(str(link))
        self.log(f'Saved file {filename}')

