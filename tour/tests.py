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


class TourDateSlugTest(TestCase):
    def test_two_shows_same_venue_same_day_both_save(self):
        day = datetime.date(2026, 11, 7)
        matinee = TourDate.objects.create(date=day, venue="The Cambridge")
        evening = TourDate.objects.create(date=day, venue="The Cambridge")
        self.assertEqual(matinee.slug, "the-cambridge-2026-11-07")
        self.assertEqual(evening.slug, "the-cambridge-2026-11-07-2")
        self.assertEqual(self.client.get(evening.get_absolute_url()).status_code, 200)

    def test_renaming_the_venue_keeps_the_link(self):
        show = TourDate.objects.create(date=datetime.date(2026, 11, 8), venue="Old Name")
        url = show.get_absolute_url()
        show.venue = "New Name"
        show.save()
        self.assertEqual(show.get_absolute_url(), url)
        self.assertEqual(self.client.get(url).status_code, 200)
