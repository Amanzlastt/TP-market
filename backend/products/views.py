from rest_framework import veiwsets, status, filters
from rest_framework.decorators import action 
from rest_framework.response import Response
from rest_framework.permissions import  IsAuthenticated, IsAdminUser, AllowAny
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.tokens import RefreshToken 
from .models import User, Product
from .serializers import (
    UserSerializer,
    UserRegisterationSerializer,
    ProductSerializer
)


class AuthViewSet(veiwsets.Viewset):
    """
    **Objective**: Handle user authentication (login/register)
    **Key Concepts**:
    - ViewSet: Combines multiple related views in one class
    - @action decorator: Creates custom endpoints beyond CRUD
    - permissions: Control who can access each endpoint
    """

    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def register (self, request):
        """**Objective**: Register new user
        **Key Concepts**:
        - serializer.is_valid(): Validates incoming data
        - serializer.save(): Creates user in database
        - Response(): Returns JSON response with status code
        """

        serializer = UserRegisterationSerializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': UserSerializer(user).data,
                'tokens': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)

                }
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        **Objective**: Authenticate user and return JWT tokens
        **Key Concepts**:
        - authenticate(): Django's built-in authentication
        - RefreshToken.for_user(): Generate JWT tokens
        """

        email = request.data.get('email')
        password = request.data.get('password')

        user  = authenticate(email=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response ({
                'user': UserSerializer(user).data,
                'tokens':{
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }
            })
        return Response(
            {'error':"Invalid credentials"},
            status=status.HTTP_400_BAD_REQUEST
        )
    
class ProductViewset(veiwsets.ModeViewset):
    """
    **Objective**: Handle all product-related operations (CRUD)
    **Key Concepts**:
    - ModelViewSet: Provides full CRUD operations automatically
    - queryset: Defines which objects to work with
    - serializer_class: Which serializer to use
    - permission_classes: Who can access these endpoints
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type']
    search_fields = ['name']
    ordering_fields = ['price', 'created_at']


    def get_permissions(self):
        """
        **Objective**: Set different permissions for different actions
        **Key Concepts**:
        - self.action: Current action being performed (list, create, etc.)
        - IsAdminUser: Only admin users can access
        - IsAuthenticated: Any logged-in user can access
        """

        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [IsAuthenticated]
        return [permisson() for permission in permission_classes]
    

    @action(detail=False, methods=['get'])
    def filter_by_price(self, request):
        """
        **Objective**: Custom endpoint to filter products by price range
        **Key Concepts**:
        - @action: Creates custom endpoint beyond standard CRUD
        - request.query_params: Access URL query parameters
        - Q objects: Complex database queries
        """

        min_price = request.query_params.get('min_price')
        max_price = request.query_params.get('max_price')

        queryset = self.get_queryset()

        if min_price:
            queryset = queryset.filter(price__gte= min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer)
    