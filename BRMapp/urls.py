
from django.conf.urls import url,include
from BRMapp import views

urlpatterns=[
url('view-books',views.viewBooks),
url('edit-book',views.editBook),
url('search-books',views.searchBook),
url('delete-book',views.deleteBook),
url('new-book',views.newBook),
url('add',views.Add),
url('search',views.search),
url('edit',views.edit),

]
