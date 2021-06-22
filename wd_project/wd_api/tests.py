
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient

# Using the standard RequestFactory API to create a form POST request

class TestAPI(TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        self.client = APIClient()
    
    def test_zone_list(self):
        # test zone list, DB has been reset so should be empty
        response = self.client.get('/zones/',content_type='application/json')
        zones=response.json()
        print(f"List status={response.status_code}")
        self.assertEqual(len(zones),0)

    def test_zone_creation(self):
        # test zone creation, create one and get list
        response = self.client.post('/zones/create', {'name': 'SomeZone','geometry':{}},format='json',content_type='application/json')
        self.assertEqual(response.status_code,201)
        zone=response.json()
        print(f"Create status={response.status_code} zone={zone}")
        
        response = self.client.get('/zones/',content_type='application/json')
        self.assertEqual(response.reason_phrase,'OK')
        zones=response.json()
        print(f"List status={response.status_code} zones={zones}")
        self.assertEqual(len(zones),1)

    def test_reports_creation(self):
        # test zone creation, create one and get list
        response = self.client.post('/reports/create', {'waste_type':'JK','location':{},'reported_by':'someone@somemail.com'},format='json',content_type='application/json')
        self.assertEqual(response.status_code,201)
        report=response.json()
        print(f"Create status={response.status_code} report={report}")

        response = self.client.get('/reports/',content_type='application/json')
        self.assertEqual(response.reason_phrase,'OK')
        reports=response.json()
        print(f"List status={response.status_code} reports={reports}")
        self.assertEqual(len(reports),1)

        response = self.client.delete(f"/reports/{reports[0].id}")
        self.assertEqual(response.reason_phrase,'OK')
        print(f"Delete status={response.status_code}")

# factory = APIRequestFactory()
# request = factory.post('/zones/', {'name': 'SomeZone','geometry':{}})

