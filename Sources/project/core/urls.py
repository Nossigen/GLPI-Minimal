from django.urls        import path

from .                  import views

import uuid

app_name='core'
urlpatterns = [

    #########
    # Admin #
    #########

    path('admin/', views.admin, name='admin'),

    ###############
    # UserManager #
    ###############

    # User

    path('user/', views.user_list,
        name = 'user_list'),
    path('user/job', views.user_list_job,
        name = 'user_list'),
    path('user/new', views.user_new,
        name = 'user_new'),
    path('user/edit/<int:user_id>', views.user_edit,
        name = 'user_edit'),
    path('user/<int:user_id>', views.user_info,
        name = "user_info"),
    path('user/delete/<int:user_id>', views.user_delete,
        name = 'user_delete'),
    path('user/job/new', views.job_new,
        name = 'job_new'),

    #################
    # ObjectManager #
    #################

    path('object/', views.object_list,
         name = "object_list"),
    path('object/stock', views.object_stock_list,
         name = "object_stock_list"),
    path('object/new/', views.object_new,
         name = "object_new"),
    path('object/new/type', views.object_type_new,
         name = "object_type_new"),
    path('object/new/get_type_form', views.get_type_form,
        name = "get_type_form"),
    path('object/<uuid:object_id>', views.object_info,
        name = "object_info"),

    ##################
    # HistoryManager #
    ##################

    path('object/change/<uuid:object_id>', views.object_to_stock,
        name = 'object_to_stock'),
    path('object/stock/change/<uuid:object_id>', views.object_to_user,
        name = 'object_to_user'),
    path('object/state/new', views.object_state_new,
        name = 'object_state_new'),

    ##################
    # CommandManager #
    ##################

    path('command/', views.command_list,
        name = 'command_list'),
    path('command/new', views.command_new,
        name = 'command_new'),
    path('command/<uuid:command_id>', views.command_info,
        name = 'command_info'),

    #################
    # VendorManager #
    #################

    path('vendor/', views.vendor_list,
        name = 'vendor_list'),
    path('vendor/new', views.vendor_new,
        name = 'vendor_new'),
    path('vendor/<int:vendor_id>', views.vendor_info,
        name = 'vendor_info'),

    path('login/', views.login, name='login'),
    path('', views.user_list, name='user_list')
]
