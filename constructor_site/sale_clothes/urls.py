from django.urls import path
from . import views

app_name = 'clothes'
urlpatterns = [
    path('',views.ClientIndexView.as_view(), name ='index'),
    path('good/list/<int:category>/',views.GoodListView.as_view(), name ='good_list'),
    path('good/list/<int:category>/<int:subcategory>',views.GoodListView.as_view(), name ='good_list'),
    path('detail/<int:good>',views.DetailView.as_view(), name ='detail'),
    path('add/bag/<int:good>',views.AddBagView.as_view(), name ='add_bag'),
    path('creat/index',views.ConstructIndexView.as_view(), name ='creat_index'),
    path('creat/good/list/<int:category>',views.CreatGoodListView.as_view(), name ='creat_good_list'),
    path('creat/category',views.CategoryCreateView.as_view(), name ='creat_category'),
    path('creat/good',views.GoodCreateView.as_view(), name ='creat_good'),
    path('creat/subcategory/<int:category>',views.SubcategoryCreateView.as_view(), name ='creat_subcategory'),
    path('update/title/good',views.UpdateTitleGoodView.as_view(), name ='update_title'),
    path('update/additional/data',views.UpdateOrCreateAdditionalDataView.as_view(), name ='update_additional_data'),
    path('update/category',views.UpdateCategoryView.as_view(), name ='update_category'),
    path('delete/category',views.DeleteCategoryView.as_view(), name ='delete_category'),
    path('delete/good',views.DeleteGoodView.as_view(), name ='delete_good'),

] 