from django.urls import path
from .views import CourseListView, CourseDetailView, CourseInfoView, CourseCommentView, AddCommentView


app_name = 'courses'
urlpatterns = [
    path('list/',CourseListView.as_view(),name="course_list"),#课程列表
    path('detail/<int:course_id>',CourseDetailView.as_view(),name="course_detail"),#课程详情
    path('info/<int:course_id>',CourseInfoView.as_view(),name="course_info"),#课程章节
    path('comment/<int:course_id>',CourseCommentView.as_view(),name="course_Comment"),#课程评论
    path('add_comment/',AddCommentView.as_view(),name="add_Comment"),#课程评论
]