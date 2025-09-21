from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # Существующие маршруты
    path("", views.show_menu, name="main"),
    path("docs/<str:workshop_name>", views.show_docs),
    path("orders/<str:workshop_name>", views.show_orders, name="orders"),
    path("docs/", views.show_all_docs, name='show_doc'),
    path("orders/", views.show_all_orders, name="all_orders"),
    path("docs/info/<int:id>", views.doc_show_info, name="doc_show_info"),
    path("create_doc", views.create_doc, name="create_doc"),
    path("create_order", views.create_order, name="create_order"),
    path("success/", views.success, name="success"),
    path("docs/order/<int:id>/", views.order_detail, name="order_detail"),
    path("doc/<int:doc_id>/add_process/", views.add_process, name="add_process"),
    path('report/', views.report, name='page_report'),
    path(
        "doc/<int:doc_id>/add_process_order/",
        views.add_process_order,
        name="add_process_order",
    ),
    path("doc/<int:doc_id>/add_order/", views.add_order, name="add_order"),
    path(
        "acquaint/<int:employee_id>/<int:doc_id>/",
        views.acquaint_employee,
        name="acquaint_employee",
    ),
    path(
        "unacquaint/<int:employee_id>/<int:doc_id>/",
        views.unacquaint_employee,
        name="unacquaint_employee",
    ),
    path("acquaint_all/<int:doc_id>/", views.acquaint_all, name="acquaint_all"),
    path("unacquaint_all/<int:doc_id>/", views.unacquaint_all, name="unacquaint_all"),
    path(
        "delete_process/<int:process_id>/", views.delete_process, name="delete_process"
    ),
    path(
        "update_process_status/<int:process_id>/",
        views.update_process_status,
        name="update_process_status",
    ),
    path(
        "acquaint_order/<int:employee_id>/<int:order_id>/",
        views.acquaint_employee_order,
        name="acquaint_employee_order",
    ),
    path(
        "unacquaint_order/<int:employee_id>/<int:order_id>/",
        views.unacquaint_employee_order,
        name="unacquaint_employee_order",
    ),
    path(
        "acquaint_all_order/<int:order_id>/",
        views.acquaint_all_order,
        name="acquaint_all_order",
    ),
    path(
        "unacquaint_all_order/<int:order_id>/",
        views.unacquaint_all_order,
        name="unacquaint_all_order",
    ),
    path('doc/<int:id>/edit/', views.edit_doc, name='edit_doc'),
    path('order/<int:id>/edit/', views.edit_order, name='edit_order'),
    path('get_employees_by_filters/', views.get_employees_by_filters, name='get_employees_by_filters'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)