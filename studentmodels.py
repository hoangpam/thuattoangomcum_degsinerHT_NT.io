# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chuyennganh(models.Model):
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    tencn = models.TextField(db_column='TenCN', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    tenbang = models.TextField(db_column='TenBang', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHUYENNGANH'



class Ctdaotao(models.Model):
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    sttmh = models.IntegerField(db_column='SttMH', blank=True, null=True)  # Field name made lowercase.
    tenmh = models.TextField(db_column='TenMH', blank=True, null=True)  # Field name made lowercase.
    tinchi = models.TextField(db_column='TinCHI', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTDAOTAO'


class Diemsv2(models.Model):
    e_id = models.IntegerField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    masv = models.TextField(db_column='MaSV', blank=True, null=True)  # Field name made lowercase.
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    diem = models.FloatField(db_column='Diem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIEMSV2'


class Khoadaotao(models.Model):
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    tenkdt = models.TextField(db_column='TenKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KHOADAOTAO'


class MonhocChuyennganh(models.Model):
    e_id = models.IntegerField(blank=True, null=True)
    sttmh = models.IntegerField(db_column='SttMH', blank=True, null=True)  # Field name made lowercase.
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MONHOC_CHUYENNGANH'


class MonhocChuyennganhLoc(models.Model):
    e_id = models.IntegerField(blank=True, null=True)
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MONHOC_CHUYENNGANH_LOC'


class Nguoidung(models.Model):
    manguoidung = models.AutoField(db_column='MaNguoiDung', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    tennguoidung = models.TextField(db_column='TenNguoiDung', blank=True, null=True)  # Field name made lowercase.
    quyennguoidung = models.IntegerField(db_column='QuyenNguoiDung', blank=True, null=True)  # Field name made lowercase.
    tendangnhap = models.TextField(db_column='TenDangNhap', blank=True, null=True)  # Field name made lowercase.
    matkhau = models.TextField(db_column='MatKhau', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'NGUOIDUNG'


class Sinhvien(models.Model):
    masv = models.TextField(db_column='MaSV', blank=True, null=True)  # Field name made lowercase.
    ho = models.TextField(db_column='Ho', blank=True, null=True)  # Field name made lowercase.
    ten = models.TextField(db_column='Ten', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SINHVIEN'

