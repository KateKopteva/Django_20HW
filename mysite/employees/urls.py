import addpage as addpage
import delete as delete
from django.urls import path, re_path
from django.utils import archive

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('addnewpage/', addnewpage, name='add_new_page'),
    path('addpage/<int:post_id>/', addpage, name='addpage'),
    path('delete_e/<int:post_id>/', delete_e, name='delete_e'),
    ]