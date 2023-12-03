# ScrapingTool

> [!NOTE]
> This code is especially written for a freelance project (contest) on freelancer.com.
> This script is created using the scrapy python library, as requested.

> [!IMPORTANT]
> You can run the script just like a normal python script. You can use `python main.py` or `python3 main.py` to run the whole script, whichever works best for you.
> The output response is not printed, but rather saved to `output.json`

This `scrapy` script can be used as an alternative to `requests` library.
Sending the `POST` request asynchronously using the `httpx` library and `asyncio` library within the `scrapy` spider named `my_spider` makes the ***script blazing fast.***

***The main structure of the scrapy spider-***

```
class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_url = 'https://fooddelivery.mykeeta.com/api/v1/homePage/homePageInfo'

    headers = {
        ...
    }

    form_data = {
        ...
    }

    # make the post request asynchronously to increase speed
    async def make_request(self):
        async with httpx.AsyncClient() as client:
                ...
            )

            # Save the response to output.js file
            with open('output.json', 'wb') as f:
                f.write(response.content)
    # start the request
    def start_requests(self):
        ...

    # mainly prints out log data necessary for debugging, such as when the spider was run, when it was closed, how many websites crawled or scraped etc.
    def parse(self, response):
        print(response.body)

    
```

The `json` library has been used to handle json data.
These three libraries are imported with `scrapy` at the top of the script.

```
import scrapy
import json
import httpx
import asyncio
```

You can install these dependencies using-

```
pip install httpx
```
and 
```
pip install asyncio
```

and if you don't have scrapy installed, you can run-

```
pip install scrapy
```

***This code has been thoroughly tested, improved and optimized to give the desired output, and best coding practices and debugging techniques were used.***

The code at the bottom is used to run the spider-

```
if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(['python','-m','scrapy', 'runspider', 'main.py'])
```

Here, you can change 'python' to 'python3' if you need to-.

```
cmdline.execute(['python3','-m','scrapy', 'runspider', 'main.py'])
```

