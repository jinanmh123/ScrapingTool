# ScrapyTool

> [!NOTE]
> This code is especially written for a freelance project (contest) on freelancer.com.
> This script is created using the scrapy python library, as requested.

> [!IMPORTANT]
> You can run the script just like a normal python script. You can use `python main.py` or `python3 main.py` to run the whole script, whichever works best for you.
> The output response is not printed, but rather saved to `output.txt` file.

In the scrapy spider, the `POST` request is sent asynchronously. This makes the script ***much much faster***. `asyncio` and `httpx` has been implemented to achieve this blazing speed.

***The main structure of the scrapy spider-***

```
# create the scrapy spider class
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
            with open('output.txt', 'wb') as f:
                f.write(response.content)
    # start the request
    def start_requests(self):
        ...

    # parse
    def parse(self, response):
        print(response.body)
    
```

These two libraries are imported with `scrapy` at the top of the script.

```
import scrapy
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
    cmdline.execute(['scrapy', 'runspider', 'main.py'])
```

