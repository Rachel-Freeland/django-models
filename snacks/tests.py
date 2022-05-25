from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack


class SnacksTests(TestCase):

    def setUp(self):
        user = get_user_model().objects.create(username="tester", password="tester")
        Snack.objects.create(name="Doritos", purchaser=user, description="cheesy goodness")

    def test_list_page_status_code(self):
        url = reverse("snack_list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        res = self.client.get(url)
        self.assertTemplateUsed(res, "snack_list.html")
        self.assertTemplateUsed(res, "base.html")

    def test_detail_page_status_code(self):
        url = reverse("snack_detail", args=[1])
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_detail_page_template(self):
        url = reverse("snack_detail", args=[1])
        res = self.client.get(url)
        self.assertTemplateUsed(res, "snack_detail.html")
        self.assertTemplateUsed(res, "base.html")


