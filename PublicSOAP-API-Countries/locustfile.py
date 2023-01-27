from locust import HttpUser, SequentialTaskSet, task
import xmltodict

HEADERS = {
    "Content-Type": "text/xml; charset=utf-8",
}

XML_BODY = """<?xml version="1.0" encoding="utf-8"?>
<soap12:Envelope xmlns:soap12="http://www.w3.org/2003/05/soap-envelope">
  <soap12:Body>
    <ListOfCountryNamesByName xmlns="http://www.oorsprong.org/websamples.countryinfo">
    </ListOfCountryNamesByName>
  </soap12:Body>
</soap12:Envelope>
"""

XML_COUNTRY_BODY = """<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <CapitalCity xmlns="http://www.oorsprong.org/websamples.countryinfo">
      <sCountryISOCode>AF</sCountryISOCode>
    </CapitalCity>
  </soap:Body>
</soap:Envelope>
"""

class TaskSet(SequentialTaskSet):

    @task
    def list_of_countries_by_name(self):
      with self.client.post(url = "",
                      data = XML_BODY,
                      headers = HEADERS,
                      name = "list_of_countries_by_name") as response:
        json_resp = xmltodict.parse(response.text)
        list_countries = json_resp['soap:Envelope']['soap:Body']['m:ListOfCountryNamesByNameResponse']['m:ListOfCountryNamesByNameResult']['m:tCountryCodeAndName']

        if response.status_code != 200:
          response.failure("Got wrong status code")
          
        assert len(list_countries) == 246

    @task
    def get_capital_city_for_country_by_iso_code(self):
      with self.client.post(url = "",
                      data = XML_COUNTRY_BODY,
                      headers = HEADERS,
                      name = "get_capital_city_for_country_by_iso_code") as response:
        json_resp = xmltodict.parse(response.text)
        capital = json_resp['soap:Envelope']['soap:Body']['m:CapitalCityResponse']['m:CapitalCityResult']
        assert capital == 'Kabul'

class AllOperationsUser(HttpUser):
    """Locust class that sets the Tasks Set(User Behaviour)
    """

    tasks = [TaskSet]
    host = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"