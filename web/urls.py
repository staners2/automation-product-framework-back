"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from web.views.ChatsViewSets import ChatsViewSets
from web.views.EmployeesViewSets import EmployeesViewSets
from web.views.EventsViewSets import EventsViewSets
from web.views.EventTypesViewSets import EventTypesViewSets
from web.views.NamespacesViewSets import NamespacesViewSets
from web.views.PlansViewSets import PlansViewSets
from web.views.ProductsViewSets import ProductsViewSets, append_employee

# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


urlpatterns = [path("admin/", admin.site.urls), path("__debug__/", include("debug_toolbar.urls"))]


router = routers.SimpleRouter(trailing_slash=False)
router.register("event-types", EventTypesViewSets, basename="event-types")  # Типы событий
router.register("actions", EventsViewSets, basename="actions")  # События
router.register("products", ProductsViewSets, basename="products")  # Продукты
router.register("namespaces", NamespacesViewSets, basename="namespaces")  # Пространства в Jira
router.register("chats", ChatsViewSets, basename="chats")  # Чат
router.register("plans", PlansViewSets, basename="plans")  # Планы
router.register("employees", EmployeesViewSets, basename="employees")  # Сотрудники


urlpatterns += [path("api/", include(router.urls)), path("api/products/<int:pk>/enabled", append_employee)]

# schema_view = get_schema_view(
#     openapi.Info(
#         title="Automation product framework",
#         default_version="v1",
#         description="Продуктовый фреймворк",
#         terms_of_service="https://www.google.com/policies/terms/",
#         contact=openapi.Contact(email="dima.aratin0@gmail.com"),
#         license=openapi.License(name="BSD License"),
#     ),
#     # url=f'{settings.APP_URL}/api/v3/',
#     patterns=[
#         path("api/", include(router.urls)),
#     ],
#     public=True,
#     permission_classes=(permissions.AllowAny,),
# )
#
# urlpatterns += [
#     path(
#         "swagger/",
#         TemplateView.as_view(template_name="swagger.html", extra_context={"schema_url": "openapi-schema"}),
#         name="swagger",
#     ),
#     path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),  # new
# ]
