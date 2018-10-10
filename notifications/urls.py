from django.conf.urls import url
from notifications import views

# urlpatterns = [
#     url(r'^email/$',
#         views.email,
#         name='email'
#         ),
#     url(r'^thanks/$',
#         views.thanks,
#         name='thanks'
#         ),
# ]

urlpatterns = [
    url(r'^email/', views.email, name='email'),
    url(r'^whatsapp/', views.whatsapp, name='whatsapp'),
    url(r'^thanks/', views.thanks, name='thanks'),
]