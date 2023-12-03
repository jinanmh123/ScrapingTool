import scrapy
import httpx
import asyncio

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_url = 'https://fooddelivery.mykeeta.com/api/v1/homePage/homePageInfo'

    # The Headers (same as the given 'requests' library script)
    headers = {
        'deviceType': 'sdk_gphone64_arm64',
        'Accept-Language': 'en',
        'appVersion': '1.1.10',
        'retrofit_exec_time': '1700590724587',
        'timeZone': 'GMT+08:00',
        'M-SHARK-TRACEID': '5171f71126b2d4544b38a98a4ff0e4cd66d7a16999806706990672227d03c17005907245875e1c22',
        'cityId': '810001',
        'locale': 'en',
        'uuid': '00000000000007024EEFCC47C49358643C0AE382C498BA169998067154711603',
        'platform': '4',
        'clientType': 'c_android',
        'districtId': '8100019',
        'osVersion': '33_13',
        'partner': '85204',
        'seq_id': '13',
        'region': 'HK',
        'request_id': '28BAC42F-6E16-4DFD-B978-EE48F2BEA1AF',
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    # The body/main data (same as in the given 'requests' library script)
    json_data = {
        'location': {
            'latitude': '22.31924733900611',
            'longitude': '114.1692228242755'
        }
    }

    # make the post request asynchronously to increase speed
    async def make_request(self):
        async with httpx.AsyncClient() as client:
            response = await client.post(
                'https://fooddelivery.mykeeta.com/api/v1/homePage/homePageInfo',
                headers=self.headers,
                json=self.json_data,
                follow_redirects=True  # Enable automatic redirects
            )
            response.raise_for_status()  # Raise an HTTPError for bad responses
            # print the status code (for debugging purposes)
            print(response.status_code)

            # Save the response to output.js file
            with open('output.txt', 'wb') as f:
                f.write(response.content)

    # start the request
    def start_requests(self):
        loop = asyncio.get_event_loop()
        yield from loop.run_until_complete(self.make_request())


    def parse(self, response):
        print(response.body)


# run the spider using scrapy cmdline
if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(['scrapy', 'runspider', 'main.py'])
