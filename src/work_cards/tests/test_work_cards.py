import random

from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase

from work_cards.models import BrancheChoices, ContractTypeChoices, EducationLevelChoices, WorkCard
from work_cards.tests.factories import UserFactory, WorkCardFactory

fake = Faker()


class WorkCardsAPITestCase(APITestCase):

    def setUp(self) -> None:
        self.user = UserFactory()
        self.work_card = WorkCardFactory(user=self.user)
        self.client.force_authenticate(user=self.user)

    def generate_work_card_data(self):
        return {
            'available_from': fake.future_date(),
            'hours_per_week': random.randrange(1, 40),
            'branches': random.sample([choice[0] for choice in BrancheChoices.choices], random.randrange(1, len(BrancheChoices.choices))),
            'contract_type': random.choice([choice[0] for choice in ContractTypeChoices.choices]),
            'minimal_education_level': random.choice([choice[0] for choice in EducationLevelChoices.choices]),
            'current_client': fake.company(),
            'looking_for': fake.sentence(),
            'key_skills': fake.sentence(),
        }

    def test_work_card_list(self):
        response = self.client.get(reverse("work_cads-list"))
        self.assertIsNotNone(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_work_card_detail(self):
        response = self.client.get(reverse("work_cads-detail", kwargs={'pk': self.work_card.id}))
        self.assertIsNotNone(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_work_card_partial_update(self):
        data = self.generate_work_card_data()
        response = self.client.patch(reverse("work_cads-detail", kwargs={'pk': self.work_card.id}), data=data, format='json')
        work_card = WorkCard.objects.get(id=self.work_card.id)
        self.assertIsNotNone(response.content)
        self.assertEqual(data['available_from'], work_card.available_from)
        self.assertEqual(data['hours_per_week'], work_card.hours_per_week)
        for branch in data['branches']:
            self.assertIn(branch, work_card.branches)
        self.assertEqual(data['contract_type'], work_card.contract_type)
        self.assertEqual(data['minimal_education_level'], work_card.minimal_education_level)
        self.assertEqual(data['current_client'], work_card.current_client)
        self.assertEqual(data['looking_for'], work_card.looking_for)
        self.assertEqual(data['key_skills'], work_card.key_skills)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_work_card_update(self):
        data = self.generate_work_card_data()
        response = self.client.put(reverse("work_cads-detail", kwargs={'pk': self.work_card.id}), data=data, format='multipart')
        work_card = WorkCard.objects.get(id=self.work_card.id)
        self.assertIsNotNone(response.content)
        self.assertEqual(data['available_from'], work_card.available_from)
        self.assertEqual(data['hours_per_week'], work_card.hours_per_week)
        for branch in data['branches']:
            self.assertIn(branch, work_card.branches)
        self.assertEqual(data['contract_type'], work_card.contract_type)
        self.assertEqual(data['minimal_education_level'], work_card.minimal_education_level)
        self.assertEqual(data['current_client'], work_card.current_client)
        self.assertEqual(data['looking_for'], work_card.looking_for)
        self.assertEqual(data['key_skills'], work_card.key_skills)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_work_card_create(self):
        data = self.generate_work_card_data()
        response = self.client.post(reverse("work_cads-list"), data=data, format='multipart')
        self.assertIsNotNone(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_work_card_unauthorized(self):
        self.client.logout()
        response = self.client.get(reverse("work_cads-list"))
        self.assertIsNotNone(response.content)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_other_user_work_card(self):
        password = fake.password()
        username = fake.first_name()
        user_2 = UserFactory(username=username, password=password)
        self.client.force_authenticate(user=user_2)
        response = self.client.get(reverse("work_cads-detail", kwargs={'pk': self.work_card.id}))
        self.assertIsNotNone(response.content)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
