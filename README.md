# Setup

1. Download and install [Python 3.x](https://www.python.org/downloads/windows/)
- If it is already installed, check in terminal:

```
python --version
```

2. Make sure to have the [latest pip version](https://pip.pypa.io/en/stable/installation/) installed

```
python.exe -m pip install --upgrade pip
```

3. Install [locust](http://docs.locust.io/en/stable/installation.html)

```
pip3 install locust
```

# Run load tests

Locust files from this repository use the following domains:

 locust file | base URL  
 --- | --- 
 BookCartAPI | https://bookcart.azurewebsites.net/api 
 LibraryAPI | https://postman-library-api.glitch.me
 ShopDemoQA | https://shop.demoqa.com

## Headful / UI mode
1. Start locust
```
locust -f <path>/locustfile.py
```

2. Access http://localhost:8089/ and set:
- number of users
- spawn rate
- base URL*

* only if host is not set in locust file.

## Headless mode

```
locust --headless --users 1 --spawn-rate 1 -H <base_url>
```

# Results

## LibraryAPI

This is and example of Response time (ms) diagram. It was generated using locust in UI mode and generating html report.

![LibraryAPI-response_time](/LibraryAPI/response_times_(ms).png "LibraryAPI-response_time")