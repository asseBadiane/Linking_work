from django.urls import path

from .views import home,worker, views_worker, views_workers, edit_or_delete_worker, LikeWorker
#job_views

app_name = "job"

urlpatterns = [
    path("",home,name='home'),
    path("work/",worker,name='worker'),
    path("work-detail/<int:id>",views_worker,name='worker_detail'),
    path("work/<int:work_id>",edit_or_delete_worker,name='worker_edit_and_delete'),
    path("workers-views/",views_workers,name='workers_views'),
    path('worker-like/<int:pk>', LikeWorker, name="worker_like"),

    # path("views-job/", job_views, name='views_job'),

]
