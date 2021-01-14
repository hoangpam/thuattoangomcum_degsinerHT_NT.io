from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("getmark", views.get_mark, name="getmark"),
    path("student/add", views.student_add, name="student_add"),

    path("getmark/filter", views.get_mark_filter, name="getmark_filter"),
    path("update", views.update, name="update"),
    path('', views.login, name="login"),
    path('add', views.add, name="adminadd"),
    path('student/<str:masv>', views.student_view, name="studentview"),
    path("filter/student>", views.get_mark_filter_sv, name="getmark_filter_sv"),
    path('getmark/student', views.mark_student, name="mark_student"),
    path('ctdaotao', views.ctdaotao, name="ctdaotao"),
    path('getctdaotao', views.getctdaotao, name="getctdaotao"),
    path("delctdaotao", views.delctdaotao, name="delctdaotao"),
    path("modifyctdaotao", views.modifyctdaotao, name="modifyctdaotao"),
    path("createctdaotao", views.createctdaotao, name="createctdaotao"),
    path('chuyennganh', views.chuyennganh, name="chuyennganh"),
    path('getchuyennganh', views.getchuyennganh, name="getchuyennganh"),
    path('delchuyennganh', views.delchuyennganh, name="delchuyennganh"),
    path("modifychuyennganh", views.modifychuyennganh, name="modifychuyennganh"),
    path("createchuyennganh", views.createchuyennganh, name="createchuyennganh"),
    path('khoadaotao', views.khoadaotao, name="khoadaotao"),
    path('delkhoadaotao', views.delkhoadaotao, name="delkhoadaotao"),
    path("modifykhoadaotao", views.modifykhoadaotao, name="modifykhoadaotao"),
    path('createkhoadaotao', views.createkhoadaotao, name="createkhoadaotao"),
    path('addtuvan', views.add_tuvan, name="addtuvan"),
    path('nguoidung', views.nguoidung, name="nguoidung"),
    path('delnguoidung', views.delnguoidung, name="delnguoidung"),
    path("modifynguoidung", views.modifynguoidung, name="modifynguoidung"),
    path("createnguoidung", views.createnguoidung, name="createnguoidung"),
    path("tuvan", views.tuvan, name="tuvan"),
    path("deltuvan", views.deltuvan, name="deltuvan"),
    path("modifytuvan", views.modifytuvan, name="modifytuvan"),
    path("createtuvan", views.createtuvan, name="createtuvan"),





]