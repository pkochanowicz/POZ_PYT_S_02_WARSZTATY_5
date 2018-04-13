from django.shortcuts import render
from django.views import View
from .models import Tweet
from .forms import MessageForm


class BaseView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        form = MessageForm()
        return render(request, 'homepage.html', {'title': "Homepage",
                                                 'tweets': tweets,
                                                 'form': form})

    def post(self, request):
        form = MessageForm(request.POST)
        tweets = Tweet.objects.all()
        if form.is_valid():
            content = form.cleaned_data['content']
            user = request.user
            new_tweet = Tweet.objects.create(
                content=content,
                user=user)
        return render(request, 'homepage.html', {'tweets': tweets,
                                                 'form': form})


class NewTweetView(View):
    def get(self, request):
        form = MessageForm()
        return render(request, 'new_tweet.html', {'form': form})


class UserProfileView(View):
    def get(self, request, user_id):
        tweets = Tweet.objects.filter(user=user_id)
        return render(request, 'user_profile.html', {'tweets': tweets})


class MessageInfoView(View):
    def get(self, request, message_id):
        tweet = Tweet.objects.get(id=message_id)
        return render(request, 'message_info.html', {'tweet': tweet})