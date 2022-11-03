from rest_framework import serializers

from work_cards.models import BrancheChoices, WorkCard


class WorkCardSerializer(serializers.ModelSerializer):

    branches = serializers.MultipleChoiceField(choices=BrancheChoices.choices, allow_empty=False)

    class Meta:
        model = WorkCard
        exclude = ('user',)

    def create(self, validated_data) -> WorkCard:
        user = self.context["request"].user
        work_card = WorkCard.objects.create(user=user, **validated_data)
        return work_card
