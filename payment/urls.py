from django.urls import path

from payment.views import CancelView, SuccessView, CreateCheckoutSessionView, BlogPage, Blogs

urlpatterns = [
    path('cancel/', CancelView.as_view(), name='cancel'),
    path('success/', SuccessView.as_view(), name='success'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('blog_page/', BlogPage.as_view(), name='blog page')

]
