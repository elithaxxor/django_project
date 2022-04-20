urlpatterns = [
    path('music_controller/api', main),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('actual_blog/', include('actual_blog.urls')),
    path('ip/', include('ip.urls')),
    path('blog/', include('blog.urls')),

]
