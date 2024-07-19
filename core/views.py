from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from .models import Video 

@login_required(redirect_field_name="account_login")
def home(request):
    videos = Video.objects.all()

    context = {
        'videos': videos
    }
    return render(request, 'core/home.html', context)


@login_required(redirect_field_name="account_login")
def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    next_video = Video.objects.filter(pk__gt=pk).order_by('pk').first()
    previous_video = Video.objects.filter(pk__lt=pk).order_by('-pk').first()
    return render(request, 'video_detail.html', {
        'video': video,
        'next_video': next_video,
        'previous_video': previous_video,
    })

