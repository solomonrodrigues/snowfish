import datetime
from unittest import mock

from django.test import TestCase
from django.utils import timezone

from .models import TourDate


class UpcomingDatesTest(TestCase):
    def test_last_nights_show_is_past_the_next_morning_in_sydney(self):
        TourDate.objects.create(date=datetime.date(2026, 10, 20), venue="Last Night")
        TourDate.objects.create(date=datetime.date(2026, 10, 21), venue="Tonight")
        # 9am on 21 Oct in Sydney is still 20 Oct in UTC.
        morning = datetime.datetime(2026, 10, 20, 22, 0, tzinfo=datetime.timezone.utc)
        with mock.patch.object(timezone, "now", return_value=morning):
            home = self.client.get("/")
            tour = self.client.get("/tour/")
        self.assertEqual([d.venue for d in home.context["upcoming_dates"]], ["Tonight"])
        self.assertEqual([d.venue for d in tour.context["tour_dates"]], ["Tonight"])
