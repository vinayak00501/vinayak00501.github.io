from .models import Profile
from django.conf import settings


def return_universal(request):
    
    current_user = request.user
    print("current user", current_user)
    user_profile = Profile.objects.filter(user=current_user)
    context = {
        "user" : current_user, 
        "user_profile" : user_profile   
    }
    print(context)
    # a = str(Profile.objects.all())
    
    return context
    

        