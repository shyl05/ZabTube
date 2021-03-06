from django.urls import path

from core.views import ChannelView, CreateChannelView, HomeView, VideoView, CommentView, NewVideo, VideoFileView

app_name = 'core'

urlpatterns = [
    path('<user>/channel/', ChannelView.as_view(), name='channel'),
    path('create-channel/', CreateChannelView.as_view(), name='create_channel'),
    path('', HomeView.as_view(), name='index'),
    path('video/<int:id>', VideoView.as_view(), name='video'),
    path('comment', CommentView.as_view(), name='comment'),
    path('new_video', NewVideo.as_view(), name='new_video'),
    path('get_video/<file_name>', VideoFileView.as_view()),
]