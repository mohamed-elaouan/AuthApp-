from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import UserAccount

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model=UserAccount
        fields=('first_name', 'last_name', 'email')
        error_class="error"
    
    
class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model=UserAccount
        fields=('first_name', 'last_name', 'email')
        error_class="error"