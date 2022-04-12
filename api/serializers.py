from rest_framework import serializers
from costs.models import Expense


class ExpenseDetailSerializer(serializers.ModelSerializer):
    """This class serialize Expense objects"""

    author = serializers.SlugRelatedField(slug_field="username",
                                          read_only=True)

    class Meta:
        model = Expense
        fields = ('author', 'description', 'pub_date', 'status')


class ExpenseListSerializer(serializers.ModelSerializer):
    """This class serialize list of Expense objects"""

    class Meta:
        model = Expense
        fields = ('description', 'pub_date', 'status', 'pk')


class ExpenseCreateSerializer(serializers.ModelSerializer):
    """This class serialize Expense objects for creation"""

    class Meta:
        model = Expense
        exclude = ("author", 'pub_date',)
        depth = 1
