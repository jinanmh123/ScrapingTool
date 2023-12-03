# ScrapingTool
## This is code for a freelance project.

This script is created mainly using the scrapy python library, as requested. This `scrapy` script can be used as an alternative to `requests` library.
Sending the `POST` request asynchronously using the `httpx` library and `asyncio` library withing the `scrapy` spider named `my_spider` makes the ***script blazing fast.***
The `json` library has been used to handle json data.
These three libraries are imported with `scrapy` at the top of the script.

```
import scrapy
import json
import httpx
import asyncio
```

You can install these using-

```
pip install httpx
```
and 
```
pip install asyncio
```

***This code has been thoroughly tested, improved and optimized to give the desired output, and best coding practices and debugging techniques were used.***

The code at the bottom is used to run the spider-

```
if __name__ == '__main__':
    from scrapy import cmdline
    cmdline.execute(['python','-m','scrapy', 'runspider', 'main.py'])
```

Here, you can change 'python' to 'python3' if, 'python' does not work.

```
cmdline.execute(['python3','-m','scrapy', 'runspider', 'main.py'])
```

***You can run the script just like a normal python script. You can use `python main.py` or `python3 main.py` to run the whole script, whichever works best for you.
