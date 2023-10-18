
from django.urls import path,include
from.import views

#cbv:class based view:
urlpatterns = [
   path('',views.add,name='add'),
   #path('detalis,',views.detalis,name='detalis')
   path('delete/<int:id>/',views.delete,name="delete"),
   path('update/<int:id>/',views.update,name="update"),
   
]