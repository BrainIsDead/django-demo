import random

import factory
from django.contrib.auth import get_user_model
from faker import Faker

from work_cards.models import BrancheChoices, ContractTypeChoices, EducationLevelChoices, WorkCard

fake = Faker()


class UserFactory(factory.django.DjangoModelFactory):
    """
    User model factory
    """
    class Meta:
        model = get_user_model()


class WorkCardFactory(factory.django.DjangoModelFactory):
    """
    WorkCard model factory
    """
    available_from = fake.future_date()
    hours_per_week = random.randrange(1, 40)
    branches = random.sample([choice[0] for choice in BrancheChoices.choices], random.randrange(1, len(BrancheChoices.choices)))
    contract_type = random.choice([choice[0] for choice in ContractTypeChoices.choices])
    minimal_education_level = random.choice([choice[0] for choice in EducationLevelChoices.choices])
    current_client = fake.company()
    looking_for = fake.sentence()
    key_skills = fake.sentence()
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = WorkCard
