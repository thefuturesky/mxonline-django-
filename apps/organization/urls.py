from .views import OrgListView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView, \
    TeacherListView, TeacherDetailView
from django.urls import path

app_name = 'organization'
urlpatterns = [
    path('list/', OrgListView.as_view(), name="org_list"),
    path('add_ask/', AddUserAskView.as_view(), name="add_ask"),
    path('home/<int:org_id>', OrgHomeView.as_view(), name="org_home"),
    path('course/<int:org_id>', OrgCourseView.as_view(), name="org_course"),
    path('decs/<int:org_id>', OrgDescView.as_view(), name="org_desc"),
    path('teacher/<int:org_id>', OrgTeacherView.as_view(), name="org_teacher"),
    # 机构收藏
    path('add_fav/', AddFavView.as_view(), name="add_fav"),
    # 讲师列表页
    path('teacher/list/', TeacherListView.as_view(), name="teacher_list"),
    #讲师详情页
    path('teacher/detail/<teacher_id>', TeacherDetailView.as_view(), name="teacher_detail"),
]
