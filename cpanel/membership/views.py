from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Member
from .serializer import MemberSerializer
from django.shortcuts import get_object_or_404

class UpsertMemberAPI(APIView):
    def post(self, request):
        phone_number = request.data.get('phone_number', None)
        if not phone_number:
            return Response(
                {"error": "Phone number is required."},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Check if a member with the given phone_number exists
        try:
            member = Member.objects.get(phone_number=phone_number)
            serializer = MemberSerializer(member, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Member updated successfully.", "data": serializer.data},
                    status=status.HTTP_200_OK
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Member.DoesNotExist:
            # If the member doesn't exist, create a new one
            serializer = MemberSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Member created successfully.", "data": serializer.data},
                    status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MemberAPI(APIView):
    # GET method to retrieve all members
    def get(self, request):
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # POST method to create a new member
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class MemberByPhoneAPI(APIView):
    # GET method to retrieve a specific member by phone_number
    def get(self, request, phone_number):
        member = get_object_or_404(Member, phone_number=phone_number)
        serializer = MemberSerializer(member)
        return Response(serializer.data, status=status.HTTP_200_OK)

class DellMemberByPhoneAPI(APIView):
        # DELETE method to delete a specific member by phone_number
    def delete(self, request, phone_number):
        member = get_object_or_404(Member, phone_number=phone_number)
        member.delete()
        return Response(
            {"detail": f"Member with phone number {phone_number} has been deleted."},
            status=status.HTTP_204_NO_CONTENT
        )












