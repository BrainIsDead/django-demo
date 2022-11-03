from django.contrib.auth import get_user_model
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

from base.models import UUIDModel
from work_cards.validators import FileSizeValidator

User = get_user_model()


class ContractTypeChoices(models.TextChoices):
    """
    Contract type enum
    """
    FREELANCE = 'Freelance', _('Freelance')
    REGULAR = 'Regular', _('Regular')
    BOTH = 'Both', _('Both')
    OTHER = 'other', _('other')


class EducationLevelChoices(models.TextChoices):
    """
    Education level enum
    """
    NO_FURTHER = 'No further education', _('No further education')
    VOCATIONAL = 'Vocational education', _('Vocational education')
    COMMUNITY_COLLEGE_LOWER_SECONDARY = 'Community College/Lower secondary education', _('Community College/Lower secondary education')
    HIGH_SCHOOL = 'High school', _('High school')
    GED = 'GED (General Education Diploma)', _('GED (General Education Diploma)')
    HIGH_SCHOOL_PRE_UNIVERSITY = 'High school/Pre-University education', _('High school/Pre-University education')
    GYMNASIUM = 'Gymnasium', _('Gymnasium')
    ASSOCIATE = 'Associate', _('Associate')
    BACHELOR = 'Bachelor', _('Bachelor')
    MASTER = 'Master', _('Master')
    PHD = 'Phd', _('Phd')


class BrancheChoices(models.TextChoices):
    """
    Branches enum
    """
    AGRICULTURE = 'Agriculture', _('Agriculture')
    BANKING = 'Banking', _('Banking')
    BIOTECHNOLOGY = 'Biotechnology', _('Biotechnology')
    CHEMICALS = 'Chemicals', _('Chemicals')
    COMMUNICATIONS = 'Communications', _('Communications')
    CONSTRUCTION = 'Construction', _('Construction')
    CONSULTING = 'Consulting', _('Consulting')
    EDUCATION = 'Education', _('Education')
    ELECTRONICS = 'Electronics', _('Electronics')
    ENERGY = 'Energy', _('Energy')
    ENGINEERING = 'Engineering', _('Engineering')
    ENTERTAINMENT = 'Entertainment', _('Entertainment')
    ENVIRONMENTAL = 'Environmental', _('Environmental')
    FINANCE = 'Finance', _('Finance')
    FOOD_AND_BEVERAGE = 'Food & Beverage', _('Food & Beverage')
    GOVERNMENT = 'Government', _('Government')
    HEALTHCARE = 'Healthcare', _('Healthcare')
    HOSPITALITY = 'Hospitality', _('Hospitality')
    INSURANCE = 'Insurance', _('Insurance')
    MACHINERY = 'Machinery', _('Machinery')
    MANUFACTURING = 'Manufacturing', _('Manufacturing')
    MEDIA = 'Media', _('Media')
    NOT_FOR_PROFIT = 'Not for Profit', _('Not for Profit')
    RECREATION = 'Recreation', _('Recreation')
    RETAIL = 'Retail', _('Retail')
    SHIPPING = 'Shipping', _('Shipping')
    TECHNOLOGY = 'Technology', _('Technology')
    TELECOMMUNICATIONS = 'Telecommunications', _('Telecommunications')
    TRANSPORTATION = 'Transportation', _('Transportation')
    UTILITIES = 'Utilities', _('Utilities')
    OTHER = 'Other', _('Other')


class WorkCard(UUIDModel):
    """
    Defines a constructor for work card
    """
    resume_nl = models.FileField(
        help_text=_('Resume in Dutch'),
        upload_to='resumes_nl',
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf"]),
            FileSizeValidator(max_size=5*1024*1024)
        ])
    resume_uk = models.FileField(
        help_text=_('Resume in English'),
        upload_to='resumes_uk',
        null=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf"]),
            FileSizeValidator(max_size=5*1024*1024)
        ])
    contract_type = models.CharField(
        help_text=_('Contract Type'),
        choices=ContractTypeChoices.choices,
        default=ContractTypeChoices.FREELANCE,
        max_length=300
    )
    available_from = models.DateField(validators=[MinValueValidator(timezone.now().date())])
    minimal_education_level = models.CharField(
        help_text=_('Minimum Education Level'),
        choices=EducationLevelChoices.choices,
        max_length=300
    )
    hours_per_week = models.PositiveIntegerField(
        help_text=_('Hours per Week'),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(40)
        ]
    )
    branches = MultiSelectField(help_text=_('Work Branches'), choices=BrancheChoices.choices, max_length=300)
    abroad = models.BooleanField(help_text=_("Work Abroad"), default=False)
    current_client = models.CharField(help_text=_("Current client"), max_length=300)
    looking_for = models.CharField(help_text=_("Looking for"), max_length=300)
    key_skills = models.CharField(help_text=_("Key skills"), max_length=300)
    user = models.ForeignKey(User, related_name='work_cards', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}__work_card({self.id})'
