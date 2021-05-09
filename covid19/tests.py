from django.test import TestCase
import datetime
# Create your tests here.
from .models import CovidRecord


class Covid19TestCase(TestCase):
    def setUp(self):
        """
            Student name: Van Phuc Tan Le
            Student number: 040985238

            This method sets up initially for the test:
            1/ Create the first CovidRecord object and get stored 
            in the database
            2/ Create the secobd CovidRecord object and get stored 
            in the database
        """
        CovidRecord.objects.create(uid='111', nameEN='TestEN', nameFR='TestFR',
                                   date=datetime.date.today(), num_confirmed='3',
                                   num_probable='1', num_death='1', num_total='1',
                                   num_tested='1', rate_tested='1', num_today='1',
                                   rate_total='1')

        CovidRecord.objects.create(uid='222', nameEN='TestEN', nameFR='TestFR',
                                   date=datetime.date.today(), num_confirmed='3',
                                   num_probable='2', num_death='2', num_total='2',
                                   num_tested='2', rate_tested='2', num_today='2',
                                   rate_total='2')

    def testLoadingFromDataSet(self):
        """
        ----------
        Student name: Van Phuc Tan Le
        Student number: 040985238
        ----------
        This method tests loading data from the Dataset
        1/ Number of records does not equal to zero
        2/ New object in SetUp was created successfully
        """
        self.assertNotEqual(CovidRecord.objects.all().count(), 0)
        self.assertEqual(CovidRecord.objects.get(uid='111').num_probable, '1')

    def testCreate(self):
        """
        ----------
        Student name: Van Phuc Tan Le
        Student number: 040985238
        ----------
        This method tests create new CovidRecord object
        1/ Record with uid=111 is not null
        2/ Record with uid=222 is not null
        3/ nameEN of both records does equal
        4/ Number of confirmed cases does equal
        """
        self.assertIsNotNone(CovidRecord.objects.get(uid='111'))
        self.assertIsNotNone(CovidRecord.objects.get(uid='222'))
        firstRecord = CovidRecord.objects.get(uid='111')
        secondRecord = CovidRecord.objects.get(uid='222')
        self.assertEqual(firstRecord.nameEN, secondRecord.nameEN)
        self.assertEqual(firstRecord.num_confirmed,
                         CovidRecord.objects.get(pk=2).num_confirmed)

    def testUpdate(self):
        """
        ----------
        Student name: Van Phuc Tan Le
        Student number: 040985238
        ----------
        This method tests update existing CovidRecord object
        After updating nameEN in first record and rate total in second record:
        1/ nameEN in first record does not equal to pre-update value ('TestEN')
        2/ nameEN in first record does equal to post-update value ('Test Update')
        3/ rate_total in second record does not equal to pre-update value ('2')
        4/ rate_total in second record does equal to post-update value ('999')
        """
        CovidRecord.objects.filter(uid='111').update(nameEN='Test Update')
        CovidRecord.objects.filter(uid='222').update(rate_total='999')
        self.assertNotEqual(CovidRecord.objects.get(
            uid='111').nameEN, 'TestEN')
        self.assertEqual(CovidRecord.objects.get(
            uid='111').nameEN, 'Test Update')
        self.assertNotEqual(CovidRecord.objects.get(uid='222').rate_total, '2')
        self.assertEqual(CovidRecord.objects.get(uid='222').rate_total, '999')

    def testDelete(self):
        """
        ----------
        Student name: Van Phuc Tan Le
        Student number: 040985238
        ----------
        This method tests delete existing CovidRecord object
        After deleting every records in the table:
        1/ number of records returned in count() equals zero
        Creating new record for testing delete:
        2/ number of records returned in count() equals 1
        3/ Get newly created record returns the object, is not null
        4/ nameEN of created object equals to String 'TestDelete'
        Delete the record just created:
        5/ number of records returned in count() equals 0 again.
        """
        CovidRecord.objects.all().delete()
        self.assertEqual(CovidRecord.objects.all().count(), 0)
        CovidRecord.objects.create(uid='333', nameEN='TestDelete', nameFR='TestDelete',
                                   date=datetime.date.today(), num_confirmed='3',
                                   num_probable='3', num_death='3', num_total='3',
                                   num_tested='3', rate_tested='3', num_today='3',
                                   rate_total='3')
        self.assertEqual(CovidRecord.objects.all().count(), 1)
        self.assertIsNotNone(CovidRecord.objects.get(uid='333'))
        self.assertEqual(CovidRecord.objects.get(
            uid='333').nameEN, 'TestDelete')
        CovidRecord.objects.filter(uid='333').delete()
        self.assertEqual(CovidRecord.objects.all().count(), 0)

    def tearDown(self):
        CovidRecord.objects.filter(nameEN='TestEN').delete()
