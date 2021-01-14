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


class Cnpm08(models.Model):
    mã_sinh_viên = models.TextField(db_column='Mã sinh viên', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    họ_đệm = models.TextField(db_column='Họ đệm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tên = models.TextField(db_column='Tên', blank=True, null=True)  # Field name made lowercase.
    lớp_học = models.TextField(db_column='Lớp học', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đối_chiếu_bằng_tốt_nghiệp_thpt_tccn_hoặc_cđ = models.TextField(db_column='Đối chiếu bằng tốt nghiệp THPT, TCCN, hoặc CĐ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_1 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_1 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_năng_ứng_dụng_công_nghệ_thông_tin = models.TextField(db_column='Kỹ năng ứng dụng Công nghệ Thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a1 = models.TextField(db_column='Anh văn A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_2 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_3_ab = models.TextField(db_column='Giáo dục quốc phòng - an ninh 3 AB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_1_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kiến_trúc_máy_tính = models.TextField(db_column='Kiến trúc máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_hướng_đối_tượng = models.TextField(db_column='Lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nhập_môn_lập_trình = models.TextField(db_column='Nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_nhập_môn_lập_trình = models.TextField(db_column='Thực hành nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_2 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pháp_luật_đại_cương = models.TextField(db_column='Pháp luật đại cương', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_lập_trình_hướng_đối_tượng = models.TextField(db_column='Thực hành lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_cao_cấp_a1 = models.TextField(db_column='Toán cao cấp A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_rời_rạc = models.TextField(db_column='Toán rời rạc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xác_suất_thống_kê = models.TextField(db_column='Xác suất thống kê', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lý_thuyết_thông_tin = models.TextField(db_column='Lý thuyết thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cơ_sở_dữ_liệu = models.TextField(db_column='Cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_2_bơi_field = models.TextField(db_column='Giáo dục thể chất 2 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 3 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hệ_điều_hành = models.TextField(db_column='Hệ điều hành', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Thực hành cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tư_tưởng_hồ_chí_minh = models.TextField(db_column='Tư tưởng Hồ Chí Minh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a2 = models.TextField(db_column='Anh văn A2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b1 = models.TextField(db_column='Anh văn B1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đại_số_tuyến_tính = models.TextField(db_column='Đại số Tuyến tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cơ_sở_dữ_liệu = models.TextField(db_column='Thực hành cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_java = models.TextField(db_column='Công Nghệ Java', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_web = models.TextField(db_column='Lập trình Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mạng_máy_tính = models.TextField(db_column='Mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_mạng_máy_tính = models.TextField(db_column='Thực hành mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trí_tuệ_nhân_tạo = models.TextField(db_column='Trí tuệ nhân tạo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b2 = models.TextField(db_column='Anh văn B2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_web = models.TextField(db_column='Công nghệ WEB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_họa_máy_tính = models.TextField(db_column='Đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khai_thác_dữ_liệu = models.TextField(db_column='Khai thác dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_thuật_lập_trình = models.TextField(db_column='Kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_trị_mạng = models.TextField(db_column='Quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_đồ_họa_máy_tính = models.TextField(db_column='Thực hành đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Thực hành hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_kỹ_thuật_lập_trình = models.TextField(db_column='Thực hành kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_ảnh = models.TextField(db_column='Xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_quản_trị_mạng = models.TextField(db_column='Thực hành quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_và_tính_toán_song_song = models.TextField(db_column='Xử lý và tính toán song song', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_net = models.TextField(db_column='Công nghệ .NET', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ảo_hóa_và_điện_toán_đám_mây = models.TextField(db_column='Ảo hóa và điện toán đám mây', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_xử_lý_ảnh = models.TextField(db_column='Thực hành xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Thực hành phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_án_chuyên_ngành_công_nghệ_phần_mềm = models.TextField(db_column='Đồ án chuyên ngành công nghệ phần mềm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khoá_luận_tốt_nghiệp = models.TextField(db_column='Khoá luận tốt nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_tập_nghề_nghiệp = models.TextField(db_column='Thực tập nghề nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_án_tốt_nghiệp = models.TextField(db_column='Đồ án tốt nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    học_lực = models.TextField(db_column='Học lực', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hạnh_kiểm = models.TextField(db_column='Hạnh kiểm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chuyên_ngành = models.TextField(db_column='chuyên ngành', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'CNPM08'


class Cnpm09(models.Model):
    mã_sinh_viên = models.TextField(db_column='Mã sinh viên', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    họ_đệm = models.TextField(db_column='Họ đệm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tên = models.TextField(db_column='Tên', blank=True, null=True)  # Field name made lowercase.
    lớp_học = models.TextField(db_column='Lớp học', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a1 = models.TextField(db_column='Anh văn A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nhập_môn_lập_trình = models.TextField(db_column='Nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_nhập_môn_lập_trình = models.TextField(db_column='Thực hành nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_1 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_cao_cấp_a1 = models.TextField(db_column='Toán cao cấp A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xác_suất_thống_kê = models.TextField(db_column='Xác suất thống kê', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_năng_ứng_dụng_công_nghệ_thông_tin = models.TextField(db_column='Kỹ năng ứng dụng Công nghệ Thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_1 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_2 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_1_thể_hình_field = models.TextField(db_column='Giáo dục thể chất 1(Thể hình)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_thể_hình_field = models.TextField(db_column='Giáo dục thể chất 2(Thể hình)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 1 (võ thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bơi_field = models.TextField(db_column='Giáo dục thể chất 1 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 1 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bơi_field = models.TextField(db_column='Giáo dục thể chất 2 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 2 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 2 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 2 (võ thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 2 (bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kiến_trúc_máy_tính = models.TextField(db_column='Kiến trúc máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_hướng_đối_tượng = models.TextField(db_column='Lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_2 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pháp_luật_đại_cương = models.TextField(db_column='Pháp luật đại cương', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_lập_trình_hướng_đối_tượng = models.TextField(db_column='Thực hành lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_rời_rạc = models.TextField(db_column='Toán rời rạc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a2 = models.TextField(db_column='Anh văn A2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lý_thuyết_thông_tin = models.TextField(db_column='Lý thuyết thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cơ_sở_dữ_liệu = models.TextField(db_column='Cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_3_ab = models.TextField(db_column='Giáo dục quốc phòng - an ninh 3 AB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_3_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 3(bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 3 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bơi_field = models.TextField(db_column='Giáo dục thể chất 3 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 3 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 3 (võ Thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hệ_điều_hành = models.TextField(db_column='Hệ điều hành', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Thực hành cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tư_tưởng_hồ_chí_minh = models.TextField(db_column='Tư tưởng Hồ Chí Minh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b1 = models.TextField(db_column='Anh văn B1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đại_số_tuyến_tính = models.TextField(db_column='Đại số Tuyến tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cơ_sở_dữ_liệu = models.TextField(db_column='Thực hành cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_java = models.TextField(db_column='Công Nghệ Java', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_web = models.TextField(db_column='Lập trình Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mạng_máy_tính = models.TextField(db_column='Mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_mạng_máy_tính = models.TextField(db_column='Thực hành mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trí_tuệ_nhân_tạo = models.TextField(db_column='Trí tuệ nhân tạo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b2 = models.TextField(db_column='Anh văn B2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_web = models.TextField(db_column='Công nghệ Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_họa_máy_tính = models.TextField(db_column='Đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khai_thác_dữ_liệu = models.TextField(db_column='Khai thác dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_thuật_lập_trình = models.TextField(db_column='Kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_trị_mạng = models.TextField(db_column='Quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_đồ_họa_máy_tính = models.TextField(db_column='Thực hành đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Thực hành hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_kỹ_thuật_lập_trình = models.TextField(db_column='Thực hành kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_ảnh = models.TextField(db_column='Xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_quản_trị_mạng = models.TextField(db_column='Thực hành quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_và_tính_toán_song_song = models.TextField(db_column='Xử lý và tính toán song song', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_net = models.TextField(db_column='Công nghệ .NET', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ảo_hóa_và_điện_toán_đám_mây = models.TextField(db_column='Ảo hóa và điện toán đám mây', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_xử_lý_ảnh = models.TextField(db_column='Thực hành xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Thực hành phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    học_lực = models.TextField(db_column='Học lực', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hạnh_kiểm = models.TextField(db_column='Hạnh kiểm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chuyên_ngành = models.TextField(db_column='chuyên ngành', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'CNPM09'


class Ctdaotao(models.Model):
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    sttmh = models.IntegerField(db_column='SttMH', blank=True, null=True)  # Field name made lowercase.
    tenmh = models.TextField(db_column='TenMH', blank=True, null=True)  # Field name made lowercase.
    tinchi = models.TextField(db_column='TinCHI', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CTDAOTAO'


class Diemsv(models.Model):
    madiem = models.AutoField(db_column='MaDIEM', blank=True, null=True)  # Field name made lowercase.
    masv = models.TextField(db_column='MaSV', blank=True, null=True)  # Field name made lowercase.
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    diem = models.FloatField(db_column='Diem', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIEMSV'


class Diemsv2(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    masv = models.TextField(db_column='MaSV', blank=True, null=True)  # Field name made lowercase.
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    diem = models.FloatField(db_column='Diem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIEMSV2'


class Diemtuvan(models.Model):
    madiem = models.AutoField(db_column='MaDIEM', blank=True, null=True)  # Field name made lowercase.
    masv = models.TextField(db_column='MaSV', blank=True, null=True)  # Field name made lowercase.
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    diem = models.FloatField(db_column='Diem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DIEMTUVAN'


class Httt08(models.Model):
    mã_sinh_viên = models.TextField(db_column='Mã sinh viên', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    họ_đệm = models.TextField(db_column='Họ đệm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tên = models.TextField(db_column='Tên', blank=True, null=True)  # Field name made lowercase.
    lớp_học = models.TextField(db_column='Lớp học', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đối_chiếu_bằng_tốt_nghiệp_thpt_tccn_hoặc_cđ = models.TextField(db_column='Đối chiếu bằng tốt nghiệp THPT, TCCN, hoặc CĐ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_1 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_1 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_năng_ứng_dụng_công_nghệ_thông_tin = models.TextField(db_column='Kỹ năng ứng dụng Công nghệ Thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a1 = models.TextField(db_column='Anh văn A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_2 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_3_ab = models.TextField(db_column='Giáo dục quốc phòng - an ninh 3 AB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_1_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kiến_trúc_máy_tính = models.TextField(db_column='Kiến trúc máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_hướng_đối_tượng = models.TextField(db_column='Lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nhập_môn_lập_trình = models.TextField(db_column='Nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_nhập_môn_lập_trình = models.TextField(db_column='Thực hành nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_2 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pháp_luật_đại_cương = models.TextField(db_column='Pháp luật đại cương', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_lập_trình_hướng_đối_tượng = models.TextField(db_column='Thực hành lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_cao_cấp_a1 = models.TextField(db_column='Toán cao cấp A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_rời_rạc = models.TextField(db_column='Toán rời rạc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xác_suất_thống_kê = models.TextField(db_column='Xác suất thống kê', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lý_thuyết_thông_tin = models.TextField(db_column='Lý thuyết thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cơ_sở_dữ_liệu = models.TextField(db_column='Cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_2_bơi_field = models.TextField(db_column='Giáo dục thể chất 2 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 3 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hệ_điều_hành = models.TextField(db_column='Hệ điều hành', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Thực hành cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tư_tưởng_hồ_chí_minh = models.TextField(db_column='Tư tưởng Hồ Chí Minh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a2 = models.TextField(db_column='Anh văn A2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b1 = models.TextField(db_column='Anh văn B1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đại_số_tuyến_tính = models.TextField(db_column='Đại số Tuyến tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cơ_sở_dữ_liệu = models.TextField(db_column='Thực hành cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_java = models.TextField(db_column='Công Nghệ Java', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_web = models.TextField(db_column='Lập trình Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mạng_máy_tính = models.TextField(db_column='Mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_mạng_máy_tính = models.TextField(db_column='Thực hành mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trí_tuệ_nhân_tạo = models.TextField(db_column='Trí tuệ nhân tạo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b2 = models.TextField(db_column='Anh văn B2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_web = models.TextField(db_column='Công nghệ WEB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_họa_máy_tính = models.TextField(db_column='Đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khai_thác_dữ_liệu = models.TextField(db_column='Khai thác dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_thuật_lập_trình = models.TextField(db_column='Kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_trị_mạng = models.TextField(db_column='Quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_đồ_họa_máy_tính = models.TextField(db_column='Thực hành đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Thực hành hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_kỹ_thuật_lập_trình = models.TextField(db_column='Thực hành kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_ảnh = models.TextField(db_column='Xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_quản_trị_mạng = models.TextField(db_column='Thực hành quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_và_tính_toán_song_song = models.TextField(db_column='Xử lý và tính toán song song', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_net = models.TextField(db_column='Công nghệ .NET', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ảo_hóa_và_điện_toán_đám_mây = models.TextField(db_column='Ảo hóa và điện toán đám mây', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_xử_lý_ảnh = models.TextField(db_column='Thực hành xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Thực hành phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_án_chuyên_ngành_hệ_thống_thông_tin = models.TextField(db_column='Đồ án chuyên ngành Hệ thống thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khoá_luận_tốt_nghiệp = models.TextField(db_column='Khoá luận tốt nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_tập_nghề_nghiệp = models.TextField(db_column='Thực tập nghề nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_án_tốt_nghiệp = models.TextField(db_column='Đồ án tốt nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    học_lực = models.TextField(db_column='Học lực', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hạnh_kiểm = models.TextField(db_column='Hạnh kiểm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chuyên_ngành = models.TextField(db_column='chuyên ngành', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'HTTT08'


class Httt09(models.Model):
    mã_sinh_viên = models.TextField(db_column='Mã sinh viên', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    họ_đệm = models.TextField(db_column='Họ đệm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tên = models.TextField(db_column='Tên', blank=True, null=True)  # Field name made lowercase.
    lớp_học = models.TextField(db_column='Lớp học', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a1 = models.TextField(db_column='Anh văn A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nhập_môn_lập_trình = models.TextField(db_column='Nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_nhập_môn_lập_trình = models.TextField(db_column='Thực hành nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_1 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_cao_cấp_a1 = models.TextField(db_column='Toán cao cấp A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xác_suất_thống_kê = models.TextField(db_column='Xác suất thống kê', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_năng_ứng_dụng_công_nghệ_thông_tin = models.TextField(db_column='Kỹ năng ứng dụng Công nghệ Thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_1 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_2 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_1_thể_hình_field = models.TextField(db_column='Giáo dục thể chất 1(Thể hình)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_thể_hình_field = models.TextField(db_column='Giáo dục thể chất 2(Thể hình)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 1 (võ thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bơi_field = models.TextField(db_column='Giáo dục thể chất 1 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 1 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bơi_field = models.TextField(db_column='Giáo dục thể chất 2 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 2 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 2 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 2 (võ thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 2 (bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kiến_trúc_máy_tính = models.TextField(db_column='Kiến trúc máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_hướng_đối_tượng = models.TextField(db_column='Lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_2 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pháp_luật_đại_cương = models.TextField(db_column='Pháp luật đại cương', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_lập_trình_hướng_đối_tượng = models.TextField(db_column='Thực hành lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_rời_rạc = models.TextField(db_column='Toán rời rạc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a2 = models.TextField(db_column='Anh văn A2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lý_thuyết_thông_tin = models.TextField(db_column='Lý thuyết thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cơ_sở_dữ_liệu = models.TextField(db_column='Cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_3_ab = models.TextField(db_column='Giáo dục quốc phòng - an ninh 3 AB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_3_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 3(bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 3 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bơi_field = models.TextField(db_column='Giáo dục thể chất 3 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 3 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 3 (võ Thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hệ_điều_hành = models.TextField(db_column='Hệ điều hành', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Thực hành cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tư_tưởng_hồ_chí_minh = models.TextField(db_column='Tư tưởng Hồ Chí Minh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b1 = models.TextField(db_column='Anh văn B1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đại_số_tuyến_tính = models.TextField(db_column='Đại số Tuyến tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cơ_sở_dữ_liệu = models.TextField(db_column='Thực hành cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_java = models.TextField(db_column='Công Nghệ Java', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_web = models.TextField(db_column='Lập trình Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mạng_máy_tính = models.TextField(db_column='Mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_mạng_máy_tính = models.TextField(db_column='Thực hành mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trí_tuệ_nhân_tạo = models.TextField(db_column='Trí tuệ nhân tạo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b2 = models.TextField(db_column='Anh văn B2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_web = models.TextField(db_column='Công nghệ Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_họa_máy_tính = models.TextField(db_column='Đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khai_thác_dữ_liệu = models.TextField(db_column='Khai thác dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_thuật_lập_trình = models.TextField(db_column='Kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_trị_mạng = models.TextField(db_column='Quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_đồ_họa_máy_tính = models.TextField(db_column='Thực hành đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Thực hành hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_kỹ_thuật_lập_trình = models.TextField(db_column='Thực hành kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_ảnh = models.TextField(db_column='Xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_quản_trị_mạng = models.TextField(db_column='Thực hành quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_và_tính_toán_song_song = models.TextField(db_column='Xử lý và tính toán song song', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_net = models.TextField(db_column='Công nghệ .NET', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ảo_hóa_và_điện_toán_đám_mây = models.TextField(db_column='Ảo hóa và điện toán đám mây', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_xử_lý_ảnh = models.TextField(db_column='Thực hành xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Thực hành phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    học_lực = models.TextField(db_column='Học lực', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hạnh_kiểm = models.TextField(db_column='Hạnh kiểm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chuyên_ngành = models.TextField(db_column='chuyên ngành', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'HTTT09'


class Khoadaotao(models.Model):
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.
    tenkdt = models.TextField(db_column='TenKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'KHOADAOTAO'


class Khptdl09(models.Model):
    mã_sinh_viên = models.TextField(db_column='Mã sinh viên', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    họ_đệm = models.TextField(db_column='Họ đệm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tên = models.TextField(db_column='Tên', blank=True, null=True)  # Field name made lowercase.
    lớp_học = models.TextField(db_column='Lớp học', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a1 = models.TextField(db_column='Anh văn A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nhập_môn_lập_trình = models.TextField(db_column='Nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_nhập_môn_lập_trình = models.TextField(db_column='Thực hành nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_1 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_cao_cấp_a1 = models.TextField(db_column='Toán cao cấp A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xác_suất_thống_kê = models.TextField(db_column='Xác suất thống kê', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_năng_ứng_dụng_công_nghệ_thông_tin = models.TextField(db_column='Kỹ năng ứng dụng Công nghệ Thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_1 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_2 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_1_thể_hình_field = models.TextField(db_column='Giáo dục thể chất 1(Thể hình)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_thể_hình_field = models.TextField(db_column='Giáo dục thể chất 2(Thể hình)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 1 (võ thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bơi_field = models.TextField(db_column='Giáo dục thể chất 1 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 1 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bơi_field = models.TextField(db_column='Giáo dục thể chất 2 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 2 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 2 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 2 (võ thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 2 (bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kiến_trúc_máy_tính = models.TextField(db_column='Kiến trúc máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_hướng_đối_tượng = models.TextField(db_column='Lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_2 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pháp_luật_đại_cương = models.TextField(db_column='Pháp luật đại cương', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_lập_trình_hướng_đối_tượng = models.TextField(db_column='Thực hành lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_rời_rạc = models.TextField(db_column='Toán rời rạc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a2 = models.TextField(db_column='Anh văn A2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lý_thuyết_thông_tin = models.TextField(db_column='Lý thuyết thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cơ_sở_dữ_liệu = models.TextField(db_column='Cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_3_ab = models.TextField(db_column='Giáo dục quốc phòng - an ninh 3 AB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_3_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 3(bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 3 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bơi_field = models.TextField(db_column='Giáo dục thể chất 3 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 3 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 3 (võ Thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hệ_điều_hành = models.TextField(db_column='Hệ điều hành', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Thực hành cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tư_tưởng_hồ_chí_minh = models.TextField(db_column='Tư tưởng Hồ Chí Minh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b1 = models.TextField(db_column='Anh văn B1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đại_số_tuyến_tính = models.TextField(db_column='Đại số Tuyến tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cơ_sở_dữ_liệu = models.TextField(db_column='Thực hành cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_java = models.TextField(db_column='Công Nghệ Java', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_web = models.TextField(db_column='Lập trình Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mạng_máy_tính = models.TextField(db_column='Mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_mạng_máy_tính = models.TextField(db_column='Thực hành mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trí_tuệ_nhân_tạo = models.TextField(db_column='Trí tuệ nhân tạo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b2 = models.TextField(db_column='Anh văn B2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chuyên_đề_seminar = models.TextField(db_column='Chuyên đề seminar', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_họa_máy_tính = models.TextField(db_column='Đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khai_thác_dữ_liệu = models.TextField(db_column='Khai thác dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_thuật_lập_trình = models.TextField(db_column='Kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_trị_mạng = models.TextField(db_column='Quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_đồ_họa_máy_tính = models.TextField(db_column='Thực hành đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Thực hành hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_kỹ_thuật_lập_trình = models.TextField(db_column='Thực hành kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_ảnh = models.TextField(db_column='Xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_quản_trị_mạng = models.TextField(db_column='Thực hành quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_và_tính_toán_song_song = models.TextField(db_column='Xử lý và tính toán song song', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_net = models.TextField(db_column='Công nghệ .NET', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ảo_hóa_và_điện_toán_đám_mây = models.TextField(db_column='Ảo hóa và điện toán đám mây', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_xử_lý_ảnh = models.TextField(db_column='Thực hành xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Thực hành phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    học_lực = models.TextField(db_column='Học lực', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hạnh_kiểm = models.TextField(db_column='Hạnh kiểm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chuyên_ngành = models.TextField(db_column='chuyên ngành', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'KHPTDL09'


class Mmt08(models.Model):
    mã_sinh_viên = models.TextField(db_column='Mã sinh viên', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    họ_đệm = models.TextField(db_column='Họ đệm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tên = models.TextField(db_column='Tên', blank=True, null=True)  # Field name made lowercase.
    lớp_học = models.TextField(db_column='Lớp học', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đối_chiếu_bằng_tốt_nghiệp_thpt_tccn_hoặc_cđ = models.TextField(db_column='Đối chiếu bằng tốt nghiệp THPT, TCCN, hoặc CĐ', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_1 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_1 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_năng_ứng_dụng_công_nghệ_thông_tin = models.TextField(db_column='Kỹ năng ứng dụng Công nghệ Thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a1 = models.TextField(db_column='Anh văn A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_2 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_3_ab = models.TextField(db_column='Giáo dục quốc phòng - an ninh 3 AB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_1_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kiến_trúc_máy_tính = models.TextField(db_column='Kiến trúc máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_hướng_đối_tượng = models.TextField(db_column='Lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nhập_môn_lập_trình = models.TextField(db_column='Nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_nhập_môn_lập_trình = models.TextField(db_column='Thực hành nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_2 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pháp_luật_đại_cương = models.TextField(db_column='Pháp luật đại cương', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_lập_trình_hướng_đối_tượng = models.TextField(db_column='Thực hành lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_cao_cấp_a1 = models.TextField(db_column='Toán cao cấp A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_rời_rạc = models.TextField(db_column='Toán rời rạc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xác_suất_thống_kê = models.TextField(db_column='Xác suất thống kê', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lý_thuyết_thông_tin = models.TextField(db_column='Lý thuyết thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cơ_sở_dữ_liệu = models.TextField(db_column='Cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_2_bơi_field = models.TextField(db_column='Giáo dục thể chất 2 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bơi_field = models.TextField(db_column='Giáo dục thể chất 3 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hệ_điều_hành = models.TextField(db_column='Hệ điều hành', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Thực hành cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tư_tưởng_hồ_chí_minh = models.TextField(db_column='Tư tưởng Hồ Chí Minh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a2 = models.TextField(db_column='Anh văn A2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b1 = models.TextField(db_column='Anh văn B1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đại_số_tuyến_tính = models.TextField(db_column='Đại số Tuyến tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cơ_sở_dữ_liệu = models.TextField(db_column='Thực hành cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_java = models.TextField(db_column='Công Nghệ Java', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_web = models.TextField(db_column='Lập trình Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mạng_máy_tính = models.TextField(db_column='Mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_mạng_máy_tính = models.TextField(db_column='Thực hành mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trí_tuệ_nhân_tạo = models.TextField(db_column='Trí tuệ nhân tạo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b2 = models.TextField(db_column='Anh văn B2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_họa_máy_tính = models.TextField(db_column='Đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khai_thác_dữ_liệu = models.TextField(db_column='Khai thác dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_thuật_lập_trình = models.TextField(db_column='Kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_lý_dự_án_công_nghệ_thông_tin = models.TextField(db_column='Quản lý dự án Công nghệ thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_trị_mạng = models.TextField(db_column='Quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_đồ_họa_máy_tính = models.TextField(db_column='Thực hành đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Thực hành hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_kỹ_thuật_lập_trình = models.TextField(db_column='Thực hành kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_ảnh = models.TextField(db_column='Xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_quản_trị_mạng = models.TextField(db_column='Thực hành quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_và_tính_toán_song_song = models.TextField(db_column='Xử lý và tính toán song song', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_net = models.TextField(db_column='Công nghệ .NET', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ảo_hóa_và_điện_toán_đám_mây = models.TextField(db_column='Ảo hóa và điện toán đám mây', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_xử_lý_ảnh = models.TextField(db_column='Thực hành xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Thực hành phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_án_chuyên_ngành_mạng_máy_tính = models.TextField(db_column='Đồ án chuyên ngành mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khoá_luận_tốt_nghiệp = models.TextField(db_column='Khoá luận tốt nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_tập_nghề_nghiệp = models.TextField(db_column='Thực tập nghề nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_án_tốt_nghiệp = models.TextField(db_column='Đồ án tốt nghiệp', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    học_lực = models.TextField(db_column='Học lực', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hạnh_kiểm = models.TextField(db_column='Hạnh kiểm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chuyên_ngành = models.TextField(db_column='chuyên ngành', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'MMT08'


class Mmt09(models.Model):
    mã_sinh_viên = models.TextField(db_column='Mã sinh viên', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    họ_đệm = models.TextField(db_column='Họ đệm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tên = models.TextField(db_column='Tên', blank=True, null=True)  # Field name made lowercase.
    lớp_học = models.TextField(db_column='Lớp học', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a1 = models.TextField(db_column='Anh văn A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nhập_môn_lập_trình = models.TextField(db_column='Nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_nhập_môn_lập_trình = models.TextField(db_column='Thực hành nhập môn lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_1 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_cao_cấp_a1 = models.TextField(db_column='Toán cao cấp A1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xác_suất_thống_kê = models.TextField(db_column='Xác suất thống kê', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_năng_ứng_dụng_công_nghệ_thông_tin = models.TextField(db_column='Kỹ năng ứng dụng Công nghệ Thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_1 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_2 = models.TextField(db_column='Giáo dục quốc phòng - an ninh 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_1_thể_hình_field = models.TextField(db_column='Giáo dục thể chất 1(Thể hình)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_thể_hình_field = models.TextField(db_column='Giáo dục thể chất 2(Thể hình)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 1 (võ thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 1 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_bơi_field = models.TextField(db_column='Giáo dục thể chất 1 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_1_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 1 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bơi_field = models.TextField(db_column='Giáo dục thể chất 2 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 2 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 2 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 2 (võ thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_2_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 2 (bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    kiến_trúc_máy_tính = models.TextField(db_column='Kiến trúc máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_hướng_đối_tượng = models.TextField(db_column='Lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    những_nguyên_lý_cơ_bản_của_chủ_nghĩa_mác_lênin_2 = models.TextField(db_column='Những nguyên lý cơ bản của chủ nghĩa Mác-Lênin 2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    pháp_luật_đại_cương = models.TextField(db_column='Pháp luật đại cương', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_lập_trình_hướng_đối_tượng = models.TextField(db_column='Thực hành lập trình hướng đối tượng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    toán_rời_rạc = models.TextField(db_column='Toán rời rạc', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_a2 = models.TextField(db_column='Anh văn A2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lý_thuyết_thông_tin = models.TextField(db_column='Lý thuyết thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cơ_sở_dữ_liệu = models.TextField(db_column='Cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_quốc_phòng_an_ninh_3_ab = models.TextField(db_column='Giáo dục quốc phòng - an ninh 3 AB', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    giáo_dục_thể_chất_3_bóng_đá_field = models.TextField(db_column='Giáo dục thể chất 3(bóng đá)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bóng_chuyền_field = models.TextField(db_column='Giáo dục thể chất 3 (bóng chuyền)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_bơi_field = models.TextField(db_column='Giáo dục thể chất 3 (bơi)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_cầu_lông_field = models.TextField(db_column='Giáo dục thể chất 3 (cầu lông)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    giáo_dục_thể_chất_3_võ_thuật_field = models.TextField(db_column='Giáo dục thể chất 3 (võ Thuật)', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it ended with '_'.
    hệ_điều_hành = models.TextField(db_column='Hệ điều hành', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cấu_trúc_dữ_liệu_và_giải_thuật = models.TextField(db_column='Thực hành cấu trúc dữ liệu và giải thuật', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tư_tưởng_hồ_chí_minh = models.TextField(db_column='Tư tưởng Hồ Chí Minh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b1 = models.TextField(db_column='Anh văn B1', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đại_số_tuyến_tính = models.TextField(db_column='Đại số Tuyến tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_cơ_sở_dữ_liệu = models.TextField(db_column='Thực hành cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_java = models.TextField(db_column='Công Nghệ Java', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    lập_trình_web = models.TextField(db_column='Lập trình Web', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    mạng_máy_tính = models.TextField(db_column='Mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_mạng_máy_tính = models.TextField(db_column='Thực hành mạng máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    trí_tuệ_nhân_tạo = models.TextField(db_column='Trí tuệ nhân tạo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    anh_văn_b2 = models.TextField(db_column='Anh văn B2', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    đồ_họa_máy_tính = models.TextField(db_column='Đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    khai_thác_dữ_liệu = models.TextField(db_column='Khai thác dữ liệu', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kỹ_thuật_lập_trình = models.TextField(db_column='Kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_lý_dự_án_công_nghệ_thông_tin = models.TextField(db_column='Quản lý dự án Công nghệ thông tin', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    quản_trị_mạng = models.TextField(db_column='Quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_đồ_họa_máy_tính = models.TextField(db_column='Thực hành đồ họa máy tính', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_hệ_quản_trị_cơ_sở_dữ_liệu_oracle = models.TextField(db_column='Thực hành hệ quản trị cơ sở dữ liệu Oracle', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_kỹ_thuật_lập_trình = models.TextField(db_column='Thực hành kỹ thuật lập trình', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_ảnh = models.TextField(db_column='Xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_quản_trị_mạng = models.TextField(db_column='Thực hành quản trị mạng', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    xử_lý_và_tính_toán_song_song = models.TextField(db_column='Xử lý và tính toán song song', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    công_nghệ_net = models.TextField(db_column='Công nghệ .NET', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    ảo_hóa_và_điện_toán_đám_mây = models.TextField(db_column='Ảo hóa và điện toán đám mây', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_xử_lý_ảnh = models.TextField(db_column='Thực hành xử lý ảnh', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    thực_hành_phân_tích_dữ_liệu_và_dự_báo = models.TextField(db_column='Thực hành phân tích dữ liệu và dự báo', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    học_lực = models.TextField(db_column='Học lực', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hạnh_kiểm = models.TextField(db_column='Hạnh kiểm', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    chuyên_ngành = models.TextField(db_column='chuyên ngành', blank=True, null=True)  # Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'MMT09'


class MonhocChuyennganh(models.Model):
    id = models.AutoField(blank=True, null=True)
    sttmh = models.IntegerField(db_column='SttMH', blank=True, null=True)  # Field name made lowercase.
    mamh = models.TextField(db_column='MaMH', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MONHOC_CHUYENNGANH'


class MonhocChuyennganhLoc(models.Model):
    id = models.AutoField(blank=True, null=True)
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


class Tuvan(models.Model):
    matv = models.AutoField(db_column='MaTV', primary_key=True, blank=True, null=True)  # Field name made lowercase.
    kctam = models.FloatField(db_column='KCTAM', blank=True, null=True)  # Field name made lowercase.
    macn = models.TextField(db_column='MaCN', blank=True, null=True)  # Field name made lowercase.
    toadotam = models.TextField(db_column='ToadoTAM', blank=True, null=True)  # Field name made lowercase.
    manguoidung = models.TextField(db_column='MaNguoiDung', blank=True, null=True)  # Field name made lowercase.
    makdt = models.TextField(db_column='MaKDT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TUVAN'
