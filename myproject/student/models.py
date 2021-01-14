# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Chuyennganh(models.Model):
    macn = models.TextField(db_column='MaCN', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    tencn = models.TextField(db_column='TenCN', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    tenbang = models.TextField(db_column='TenBang', blank=True, null=True)  # Field name made lowercase.

    def serialize(self):

        return({
            'macn': self.macn,
            'tencn': self.tencn,
            'makdt': self.makdt,
            'tenbang': self.tenbang
        })
    class Meta:
        # managed = False
        db_table = 'CHUYENNGANH'



class Ctdaotao(models.Model):
    mamh = models.TextField(db_column='MaMH', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    sttmh = models.IntegerField(db_column='SttMH', blank=True, null=True)  # Field name made lowercase.
    tenmh = models.TextField(db_column='TenMH', blank=True, null=True)  # Field name made lowercase.
    tinchi = models.TextField(db_column='TinCHI', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'CTDAOTAO'

    def serialize(self):
        return({
            'mamh': self.mamh,
            'sttmh': self.sttmh,
            'tenmh': self.tenmh,
            'tinchi': self.tinchi,
            'makdt': self.makdt
        })
    def serialize_student(self):
        return({
            'mamh': self.mamh,
            'tenmh': self.tenmh,
            'makdt': self.makdt
        })

class Diemsv2(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    # masv = models.TextField(db_column='MaSV', blank=True, null=True)  # Field name made lowercase.

    masv = models.ForeignKey("Sinhvien", on_delete=models.CASCADE, db_column='MaSV', blank=True, null=True)  # Field name made lowercase.

    mamh = models.ForeignKey("Ctdaotao", on_delete=models.CASCADE, db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    makdt = models.ForeignKey("Khoadaotao", on_delete=models.CASCADE, db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    macn = models.ForeignKey("Chuyennganh", on_delete=models.CASCADE, db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    diem = models.FloatField(db_column='Diem', blank=True, null=True)  # Field name made lowercase.

    def serialize(self):
        sv = self.masv.serialize()
        # return ({
        #     str(sv['masv']): {
        #         "ho": sv["ho"],
        #         'ten': sv['ten'],
        #         'mark': [
        #             {
        #                 'sj': self.mamh.serialize(),
        #                 'kdt': self.makdt.serialize(),
        #                 'diem': self.diem 
        #             }
        #         ]
        #     }
        # })
        return ({
            'id': self.id,
            'sv': self.masv.serialize(),
            'sj': self.mamh.serialize(),
            'kdt': self.makdt.serialize(),
            'diem': self.diem
        })
    
    def serialize_mark(self):
        return({
            str(self.masv.masv): {
                str(self.mamh.tenmh): self.diem
            },
            "sv": {
                "masv": self.masv.masv,
                'ho': self.masv.ho,
                'ten': self.masv.ten
            }
        })
    
    def serialize_student(self):
        return({
            "kdt": self.makdt.makdt,
            "macn": {}
        })


    class Meta:
        managed = True
        db_table = 'DIEMSV2'


class Khoadaotao(models.Model):
    makdt = models.TextField(primary_key=True, db_column='MaKDT', blank=True, null=False)  # Field name made lowercase.
    tenkdt = models.TextField(db_column='TenKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'KHOADAOTAO'
    def serialize(self):
        return({
            'makdt': self.makdt,
            'tenkdt': self.tenkdt
        })


class MonhocChuyennganh(models.Model):
    id = models.AutoField(blank=True, null=False, primary_key=True)
    sttmh = models.IntegerField(db_column='SttMH', blank=True, null=True)  # Field name made lowercase.
    mamh = models.ForeignKey("Ctdaotao", on_delete=models.CASCADE, db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    macn = models.ForeignKey("Chuyennganh", on_delete=models.CASCADE, db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'MONHOC_CHUYENNGANH'

    def serialize(self):
        return({
            'mamh': self.mamh.mamh,
            "tenmh": self.mamh.tenmh,
            'macn': self.macn.macn,
            'makdt': self.makdt
        })
class MonhocChuyennganhLoc(models.Model):
    id = models.AutoField(blank=True, null=False, primary_key=True)
    mamh = models.ForeignKey("Ctdaotao", on_delete=models.CASCADE, db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    macn = models.ForeignKey("Chuyennganh", on_delete=models.CASCADE, db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    makdt = models.ForeignKey("Khoadaotao", on_delete=models.CASCADE, db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'MONHOC_CHUYENNGANH_LOC'


class Nguoidung(models.Model):
    manguoidung = models.AutoField(db_column='MaNguoiDung', primary_key=True, blank=True, null=False)  # Field name made lowercase.
    tennguoidung = models.TextField(db_column='TenNguoiDung', blank=True, null=True)  # Field name made lowercase.
    quyennguoidung = models.IntegerField(db_column='QuyenNguoiDung', blank=True, null=True)  # Field name made lowercase.
    tendangnhap = models.TextField(db_column='TenDangNhap', blank=True, null=True)  # Field name made lowercase.
    matkhau = models.TextField(db_column='MatKhau', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'NGUOIDUNG'


class Sinhvien(models.Model):
    masv = models.TextField(db_column='MaSV', blank=True, null=False, primary_key=True)  # Field name made lowercase.
    ho = models.TextField(db_column='Ho', blank=True, null=True)  # Field name made lowercase.
    ten = models.TextField(db_column='Ten', blank=True, null=True)  # Field name made lowercase.

    def serialize(self):
        return({
            'masv': self.masv,
            'ho': self.ho,
            'ten': self.ten
        })
    class Meta:
        # managed = False
        db_table = 'SINHVIEN'

class Tuvan(models.Model):
    matv = models.AutoField(db_column='MaTV', primary_key=True, blank=True)  # Field name made lowercase.
    kctam = models.FloatField(db_column='KCTAM', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    toadotam = models.TextField(db_column='ToadoTAM', blank=True, null=True)  # Field name made lowercase.
    manguoidung = models.TextField(db_column='MaNguoiDung', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TUVAN'