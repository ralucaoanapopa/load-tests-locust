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

*only if host is not set in locust file.

## Headless mode

```
locust --headless --users 1 --spawn-rate 1 -H <base_url>
```

# Results

## LibraryAPI

This is and example of Response time (ms) diagram. It was generated using locust in UI mode and generating html report.

![LibraryAPI-response_time](/LibraryAPI/response_times_(ms).png "LibraryAPI-response_time")

## ShopDemoQA

Generated using locust in UI mode, then saved a html report which contains these types of diagrams and statistics:

![ShopDemoQA-request-statistics](/ShopDemoQA/request_statistics.PNG "ShopDemoQA-request-statistics")

![ShopDemoQA-response-times](/ShopDemoQA/response_times_(ms).png "ShopDemoQA-response-times")

![ShopDemoQA-total-req-per-s](/ShopDemoQA/total_requests_per_second.png "ShopDemoQA-total-req-per-s")

## PublicSOAP-API-Countries

Generated using locust in UI mode, then saved a html report which contains these types of diagrams and statistics:

![PublicSOAP-API-request-statistics](/PublicSOAP-API-Countries/request_statistics.PNG "PublicSOAP-API-request-statistics")

![PublicSOAP-API-response-times](/PublicSOAP-API-Countries/response_times_(ms).png "PublicSOAP-API-response-times")

![PublicSOAP-API-total_requests_per_second](/PublicSOAP-API-Countries/total_requests_per_second.png "PublicSOAP-API-total_requests_per_second")

![PublicSOAP-API-number_of_users](/PublicSOAP-API-Countries/number_of_users.png "PublicSOAP-API-number_of_users")