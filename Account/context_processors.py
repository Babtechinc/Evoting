from django.contrib.auth.decorators import login_required
from Account.models import UserAccount
from Election.models import ElectionPosition



def add_variable_to_context(request):
    user=0
    if UserAccount.objects.filter(UserID=request.user.id):
        user = UserAccount.objects.get(UserID=request.user.id)
    Position = ElectionPosition.objects.all()

    return {
    'voter':user,
    'Position':Position
    }