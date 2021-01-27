from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
app_name='blog'
urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('details/<int:id>/',views.post_details,name='post_details'),
    path('about/',views.about),
    path('share/<int:id>/',views.sharepost,name='sharepost'),
    path('comment/<int:id>/',views.add_comment,name="add_comment"),
    
						
]
if settings.DEBUG:

    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)