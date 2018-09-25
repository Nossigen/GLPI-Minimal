from django.urls import path

from . import views

urlpatterns = [
    # List
    path('', views.user_list, name='index'),
    path('list/', views.user_list, name = "user_list"),

    path('job/', views.user_list_by_job, name = "user_list_by_job"),
    path('list/job/', views.user_list_by_job, name = "user_list_by_job"),

    path('role/', views.user_list_by_role, name = "user_list_by_role"),
    path('list/role/', views.user_list_by_role, name = "user_list_by_role"),

    # Edit
    path('new', views.user_new, name = "user_new"),
    path('<int:user_id>/edit', views.user_edit, name = "user_edit"),
    path('job/new', views.job_new, name = "job_new"),
    path('role/new', views.role_new, name = "role_new"),
    path('job/<int:job_id>/edit', views.job_edit, name = "job_edit"),
    path('role/<int:role_id>/edit', views.role_edit, name = "role_edit"),

    # Specific
    path('<int:user_id>', views.user_info, name = "user_info"),
]
