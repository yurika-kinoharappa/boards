from django.urls import path

from . import views


app_name = "event"

urlpatterns = [
    # 勉強
    path("study/", views.study, name="study"),
    path("study_save1/", views.study_save1, name="study_save1"),
    path("study_save2/", views.study_save2, name="study_save2"),
    path("study_shousai/<int:event_id>",views.study_shousai, name="study_shousai"),
    path("modoru_study/", views.modoru_study, name="modoru_study"),

    # 日記
    path("diary/", views.diary, name="diary"),
    path("diary_save", views.diary_save, name="diary_save"),
    path("diary_shousai/<int:event_id>", views.diary_shousai, name="diary_shousai"),
    path("modoru_diary/", views.modoru_diary, name="modoru_diary"),

    # 夢日記
    path("dd", views.dd, name="dd"),
    path("dd_save", views.dd_save, name="dd_save"),
    path("dd_shousai/<int:event_id>", views.dd_shousai, name="dd_shousai"),
    path("modoru_dd/", views.modoru_dd, name="modoru_dd"),

    # ダイエット
    path("diet/", views.diet, name="diet"),
    path("diet_save", views.diet_save, name="diet_save"),
    path("diet_shousai/<int:event_id>", views.diet_shousai, name="diet_shousai"),
    path("modoru_diet/", views.modoru_diet, name="modoru_diet"),
    path("eat_save/", views.eat_save, name="eat_save"),
    path("eat_shousai", views.eat_shousai, name="eat_shousai"),

    # タバコ
    path("smoke/", views.smoke, name="smoke"),
    path("smoke_save", views.smoke_save, name="smoke_save"),
    path("smoke_shousai/<int:event_id>", views.smoke_shousai, name="smoke_shousai"),
    path("modoru_smoke/", views.modoru_smoke, name="modoru_smoke"),
]