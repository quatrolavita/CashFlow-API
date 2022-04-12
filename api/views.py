from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from costs.models import Expense
from clients.permissions import IsAuthorOrAdmin
from .serializers import (ExpenseDetailSerializer, ExpenseListSerializer,
                          ExpenseCreateSerializer)


class ExpenseViewSet(viewsets.ViewSet):

    @action(detail=False, permission_classes=[IsAuthorOrAdmin])
    def list(self, request):
        queryset = Expense.objects.all().filter(author=request.user)
        serializer = ExpenseListSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, permission_classes=[IsAuthorOrAdmin])
    def retrive(self, request, pk=None):
        queryset = Expense.objects.all()
        expense = get_object_or_404(queryset, pk=pk)
        serializer = ExpenseDetailSerializer(expense)
        return Response(serializer.data)

    @action(detail=False, permission_classes=[permissions.IsAuthenticated])
    def create(self, request):
        new_expense = Expense(author=request.user)
        serializer = ExpenseCreateSerializer(new_expense, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthorOrAdmin])
    def update(self, request, pk=None):
        queryset = Expense.objects.all()
        expense = get_object_or_404(queryset, pk=pk)
        serializer = ExpenseCreateSerializer(expense, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=False, permission_classes=[IsAuthorOrAdmin])
    def destroy(self, request, pk=None):
        queryset = Expense.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
