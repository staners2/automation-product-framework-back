from django.utils import timezone
from rest_framework import serializers

from web.models.PlansModel import PlansModel
from web.models.ProductsModel import ProductsModel


class UpdatePlansSerializer(serializers.ModelSerializer):

    date = serializers.DateField(required=False)
    product = serializers.PrimaryKeyRelatedField(
        queryset=ProductsModel.objects.filter(deleted=None).all(),
        required=False,
        many=False,
    )

    class Meta:
        model = PlansModel
        exclude = ("updated", "deleted")

    # TODO: Валидацию на то что у одного продукта запись может быть только одна за месяц
    def validate_date(self, value):
        if (
            PlansModel.objects.exclude(id=self.instance.id)
            .filter(
                product=self.initial_data.get("product", self.instance.product.id),
                date=self.initial_data.get("date", self.instance.date),
                deleted=None,
            )
            .count()
            != 0
        ):
            raise serializers.ValidationError("План на этот месяц уже составлен")

        return value

    def update(self, instance, validated_data):
        instance.date = validated_data.get("date", instance.date)
        instance.product = validated_data.get("product", ProductsModel.objects.get(id=instance.product.id))
        instance.daily = validated_data.get("daily", instance.daily)
        instance.review_code = validated_data.get("review_code", instance.review_code)
        instance.one_to_one = validated_data.get("one_to_one", instance.one_to_one)
        instance.individual_plan = validated_data.get("individual_plan", instance.individual_plan)
        instance.meeting_on_product = validated_data.get("meeting_on_product", instance.meeting_on_product)
        instance.close_task = validated_data.get("close_task", instance.close_task)
        instance.updated = timezone.now()
        instance.save()

        return instance
