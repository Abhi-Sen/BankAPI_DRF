from rest_framework.test import APITestCase
from banks_api.models import Bank, Branch


class BankAPITestCase(APITestCase):
    def setUp(self):
        self.headers = {
            'Content-Type': 'application/json'
        }
        self.bank = Bank.objects.create(name='Test Bank')
        self.branch = Branch.objects.create(
            bank=self.bank,
            ifsc='TEST_IFSC',
            branch='Test Branch',
            address='Test Address',
            city='Test City',
            district='Test District',
            state='Test State'
        )

    def test_bank_list(self):
        bank_list = self.client.get("/api/banks_api/bank/", self.headers)
        self.assertEqual(200, bank_list.status_code)
        self.assertEqual(1, bank_list.json()[0]["id"])

    def test_bank_retrieve(self):
        bank_list = self.client.get("/api/banks_api/bank/", self.headers)
        bank_id = bank_list.json()[0]["id"]
        bank_retrieve = self.client.get(f"/api/banks_api/bank/{bank_id}/", self.headers)
        self.assertEqual(200, bank_retrieve.status_code)
        self.assertEqual(self.bank.id, bank_retrieve.json()["id"])

    def test_bank_retrieve_failed(self):
        bank_list = self.client.get("/api/banks_api/bank/", self.headers)
        bank_id = bank_list.json()[0]["id"]
        bank_retrieve = self.client.get(f"/api/banks_api/bank/{int(bank_id) + 1}/", headers=self.headers)
        self.assertEqual(404, bank_retrieve.status_code)

    def test_branch_list(self):
        bank_list = self.client.get("/api/banks_api/bank/", self.headers)
        bank_id = bank_list.json()[0]["id"]
        branch_list = self.client.get(f"/api/banks_api/bank/{bank_id}/branch/", headers=self.headers)
        self.assertEqual(200, branch_list.status_code)
        self.assertEqual(self.branch.ifsc, branch_list.json()[0]["ifsc"])

    def test_branch_retrieve(self):
        bank_list = self.client.get("/api/banks_api/bank/", self.headers)
        bank_id = bank_list.json()[0]["id"]
        branch_list = self.client.get(f"/api/banks_api/bank/{bank_id}/branch/", headers=self.headers)
        ifsc = branch_list.json()[0]["ifsc"]
        branch_retrieve = self.client.get(f"/api/banks_api/bank/{bank_id}/branch/{ifsc}/", headers=self.headers)
        self.assertEqual(200, branch_retrieve.status_code)
        self.assertEqual(self.branch.ifsc, branch_retrieve.json()["ifsc"])

    def test_branch_retrieve_failed(self):
        bank_list = self.client.get("/api/banks_api/bank/", self.headers)
        bank_id = bank_list.json()[0]["id"]
        ifsc = "failed_ifsc"
        branch_retrieve = self.client.get(f"/api/banks_api/bank/{bank_id}/branch/{ifsc}/", headers=self.headers)
        self.assertEqual(404, branch_retrieve.status_code)
