from datetime import datetime, timedelta
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Transaction
from .serializers import TransactionSerializer, CheckoutSerializer
from books.models import Book
from users.models import User

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.user.is_staff:
            queryset = queryset.filter(user=self.request.user)
        return queryset

    @action(detail=False, methods=['post'])
    def checkout(self, request):
        serializer = CheckoutSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        book = get_object_or_404(Book, pk=serializer.validated_data['book_id'])
        user = get_object_or_404(User, pk=serializer.validated_data['user_id'])

        #requesting user = transaction user
        if user != request.user and not request.user.is_staff:
            raise PermissionDenied("Cannot checkout books for other users")

        # validations
        if book.copies_available <= 0:
            return Response(
                {'error': 'No copies available'}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        if Transaction.objects.filter(user=user, book=book, is_returned=False).exists():
            return Response(
                {'error': 'Book already checked out'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create transaction
        transaction = Transaction.objects.create(
            user=user,
            book=book,
            due_date=datetime.now() + timedelta(days=14),
            is_returned=False
        )

        # Update inventory
        book.copies_available -= 1
        book.save()

        return Response(
            TransactionSerializer(transaction).data,
            status=status.HTTP_201_CREATED
        )

    @action(detail=True, methods=['post'])
    def return_book(self, request, pk=None):
        transaction = get_object_or_404(Transaction, pk=pk)

        # Verification
        if transaction.user != request.user and not request.user.is_staff:
            raise PermissionDenied("Cannot return books for other users")

        if transaction.is_returned:
            return Response(
                {'error': 'Book already returned'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Process return
        transaction.is_returned = True
        transaction.return_date = datetime.now()
        transaction.save()

        # Update inventory
        transaction.book.copies_available += 1
        transaction.book.save()

        return Response(
            TransactionSerializer(transaction).data,
            status=status.HTTP_200_OK
        )

    def perform_create(self, serializer):
        raise PermissionDenied()
    