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

class TaskSet(SequentialTaskSet):

    @task
    def list_of_countries_by_name(self):
        response = self.client.post(url = "",
                        data=XML_BODY,
                        headers = HEADERS)

        json_resp = xmltodict.parse(response.text)
        list_countries = json_resp['soap:Envelope']['soap:Body']['m:ListOfCountryNamesByNameResponse']['m:ListOfCountryNamesByNameResult']['m:tCountryCodeAndName']

        assert len(list_countries) == 246

class AllOperationsUser(HttpUser):
    """Locust class that sets the Tasks Set(User Behaviour)
    """

    tasks = [TaskSet]
    host = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"