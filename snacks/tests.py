from django.test import TestCase
from django.urls import reverse

import snacks.views


class SnacksTests(TestCase):
    def test_list_page_status_code(self):
        url = reverse("snack_list")
        res = self.client.get(url)
        self.assertEqual(res.status_code, 200)

    def test_list_page_template(self):
        url = reverse("snack_list")
        res = self.client.get(url)
        self.assertTemplateUsed(res, "snack_list.html")
        self.assertTemplateUsed(res, "base.html")

    # def test_detail_page_status_code(self):
    #     url = reverse("snack_detail", args=arr.pk)
    #     res = self.client.get(url)
    #     self.assertEqual(res.status_code, 200)

    # def test_detail_page_template(self):
    #     url = reverse("snack_detail", args=[1, 2, 3, 4])
    #     res = self.client.get(url)
    #     self.assertTemplateUsed(res, "snack_detail.html")
    #     self.assertTemplateUsed(res, "base.html")


