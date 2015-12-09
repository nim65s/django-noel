from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def secret_santa(request):
    return render(request, 'secret_santa.html', context={'g': [(g.group, g.gift(request.user.pk)) for g in
        [g.christmasgroup_set.first() for g in request.user.groups.all() if g.christmasgroup_set.exists()]]})
