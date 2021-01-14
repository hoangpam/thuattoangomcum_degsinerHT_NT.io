from django.shortcuts import render
from .models import *
import json
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
import kmean as km
import pandas as pd
import numpy as np

users=[]
# Create your views here.
@csrf_exempt
def login(request):
    if request.method == "GET":
        return render(request, 'student/login.html')
    usr = request.POST['usr']
    pwd = request.POST['pwd']
    try: 
        user = Nguoidung.objects.get(tendangnhap=usr, matkhau=pwd)
        users.clear()
        users.append({
            'user': usr,
            'role': user.quyennguoidung
        })
        if users[0]['role'] == 1:
            return HttpResponseRedirect(reverse("index"))
        else:
            return HttpResponseRedirect(reverse("studentview", kwargs={
                'masv': usr
            }))
    except Exception as e:
        print(e) 
        return render(request, "student/login.html", {
            'inform': "Failed"
        }) 

@csrf_exempt
def student_add(request):

    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        masv = Sinhvien.objects.get(masv=data['masv'])
        makdt = Khoadaotao.objects.get(makdt=data['makdt'])
        mamh = Ctdaotao.objects.get(mamh=data['mamh'])
        macn = Chuyennganh.objects.get(macn=data['macn'])
        print(makdt,mamh,masv,macn)
        diem = float(data['diem'])
        check = list(Diemsv2.objects.filter(masv=masv, makdt=makdt, mamh=mamh, macn=macn))
        if len(check) == 0:
            new = Diemsv2.objects.create(masv=masv, mamh=mamh, diem=diem, makdt=makdt, macn=macn)
            # new.save()
            return JsonResponse({
                "inform": "Nhập điểm thành công"
                }
            )
        else: 
            return JsonResponse({
                'inform': "Đã có thông tin"
            })


def index(request):

    khoadaotao = Khoadaotao.objects.all()
    sinhvien = list(Sinhvien.objects.all())
    sv = {}
    for i in sinhvien:
        sv.update({
            str(i.masv): i.ho + " " +i.ten
        })
    x = Chuyennganh.objects.all()
    y = [i.serialize() for i in x]
    monhoc = list(MonhocChuyennganh.objects.all())
    mh = [i.serialize() for i in monhoc]
    
    return render(request, "student/index.html", {
        'obj': y,
        'khoadaotao': khoadaotao,
        'cndata': json.dumps(y),
        'monhoc': json.dumps(mh),
        'sinhvien': json.dumps(sv)
    })

def get_mark(request):
    macn = request.GET['macn']
    # print(macn)
    mhcn = MonhocChuyennganh.objects.filter(macn=Chuyennganh.objects.get(macn=macn))
    mhcn = [x.mamh.tenmh for x in mhcn]
    if 'Giáo dục thể chất 3 (bóng chuyền)' not in mhcn:
        mhcn.append('Giáo dục thể chất 3 (bóng chuyền)')
    if 'Công nghệ WEB' not in mhcn:
        mhcn.append('Công nghệ WEB')
    mhcn = sorted(mhcn)
    diemsv = Diemsv2.objects.filter(macn=Chuyennganh.objects.get(macn=macn))
    keys = []
    arr = []
    for i in diemsv:
        i = i.serialize_mark()
        # print(i.keys())
        k = list(i.keys())[0]
        if k not in keys:
            arr.append(i)
            keys.append(k)
        else:
            index = keys.index(k)
            # arr[index][k].append(i[k][0])
            arr[index][k].update(i[k])
    
    for i in range(len(keys)):
        for j in mhcn:
            if j not in arr[i][keys[i]].keys():
                arr[i][keys[i]][j] = "---"
        arr[i][keys[i]]
    
    arr.append(mhcn)
    
    # print(arr[len(keys)-1])
    # print(len(mhcn))

    # print(len(arr[135][keys[135]]))
    # print(len(arr[1][keys[1]]))
    # print(len(arr[11][keys[11]]))
    return JsonResponse(arr, safe=False)

# Loc mon
def get_mark_filter(request):
    macn = request.GET['macn']
    action = request.GET['action']
    mhcn = MonhocChuyennganhLoc.objects.filter(macn=Chuyennganh.objects.get(macn=macn))
    if mhcn == None:
        return JsonResponse({
            'inform': "Noresult"
        })
    ref = [x.mamh for x in mhcn]
    # print(mhcn)
    # mhcn = sorted(mhcn)
    diemsv = Diemsv2.objects.filter(macn=Chuyennganh.objects.get(macn=macn))
    
    x = [list(diemsv.filter(mamh=x)) for x in ref]
    x = [ k for j in x for k in j]
    # print(len(x))
    mhcn = [x.mamh.tenmh for x in mhcn]

    keys = []
    arr = []
    for i in x:
        i = i.serialize_mark()
        k = list(i.keys())[0]
        if k not in keys:
            arr.append(i)
            keys.append(k)
        else:
            index = keys.index(k)
            arr[index][k].update(i[k])
    
    for i in range(len(keys)):
        for j in mhcn:
            if j not in arr[i][keys[i]].keys():
                arr[i][keys[i]][j] = "---"
        arr[i][keys[i]]
    
    arr.append(mhcn)
    print((arr))
    if (action=="modify"):
        bangdiem_kmean_loc = {}
        for i in arr:
            diem_sv = pd.DataFrame(i)
            ma_sv = diem_sv.columns[0]
            bangdiem_kmean_loc[ma_sv] = diem_sv.iloc[:,0]
        bangdiem_kmean_loc_df = pd.DataFrame(bangdiem_kmean_loc)
        bangdiem_kmean_loc_df = bangdiem_kmean_loc_df.iloc[0:8,0:-1]
        bangdiem_kmean_loc_df = bangdiem_kmean_loc_df.transpose()
        labels = bangdiem_kmean_loc_df.index
        bangdiem_kmean_loc_df.replace('---', -1, inplace = True)
        bangdiem_kmean_loc_df = bangdiem_kmean_loc_df.replace(np.nan, -1)
        bangdiem_kmean_loc_df = bangdiem_kmean_loc_df.astype(np.float32)

        #chuyển ta dạng dataframe về list để có thể chạy được thuật toán
        bangdiem_kmean_loc_last = np.array(bangdiem_kmean_loc_df)
        bangdiem_kmean_loc_last= list(bangdiem_kmean_loc_last)
        for i in range(len(bangdiem_kmean_loc_last)):
            bangdiem_kmean_loc_last[i] = list(bangdiem_kmean_loc_last[i])
        # print(bangdiem_kmean_loc_last)
        data_set = bangdiem_kmean_loc_last

        # Value of K (cái này sẽ lấy từ ô text box do giáo viên nhập)
        k_value = 2

        # Độ chính xác (làm tròn sau dấu phẩy)
        precision = 5

        #bán kính để loại nhiễu (cái này sẽ lấy từ ô text box do giáo viên nhập)
        r = 10

        # chạy thuật toán
        results = km.runner(data_set, k_value, labels, r, precision)

        """
        dữ liệu trả về sẽ dạng từ điển:
            - min_distance_centroid: khoảng cách gần nhất đến tâm 
            - outlier: danh sách các sinh viên có khoảng cách đến tâm lớn hơn hoặc bằng r => ép kiểu về pd.DataFrame
            - all_: trả về một dict chứa tất cả khoảng cách của tập sinh viên đến các cụm => ép kiểu về pd.DataFrame
            - centroid: tọa độ các cụm
        """
        all_ = pd.DataFrame(results["all"])
        min_distance = results["min_distance_centroid"]
        outliers = pd.DataFrame(results["outlier"])
        centroids = pd.DataFrame(results["centroid"])
        for i in range(all_.shape[0]):
            if all_.loc[i,"khoang cach den tam cum"] == min_distance:
                cum = all_.loc[i,"cum"]
                break
        toa_do = centroids.loc[cum,:]
        a = [str(i) for i in json.loads(toa_do.to_json()).values()]

        x = json.loads(outliers.to_json())
        x['kc tam'] = min_distance
        x['toado tam'] = "_".join(a)
        
        print(x)
        
        # print(json.loads(outliers.to_json())['cum'])
        
        # return JsonResponse(outliers.to_json(), safe=False)
        return JsonResponse(x)
    else:
        return JsonResponse(arr, safe=False)

# Loc mon sinh vien
def get_mark_filter_sv(request):
    makdt = request.GET['makdt']
    macns = request.GET['macn']
    macns = json.loads(macns)
    action = request.GET['action']
    masv = request.GET['masv']
    data = []
    for macn in macns:
        macn = Chuyennganh.objects.get(macn=macn)
        mhcn = MonhocChuyennganhLoc.objects.filter(macn=macn)
        if mhcn == None:
            return JsonResponse({
                'inform': "Noresult"
            })
        ref = [x.mamh for x in mhcn]
        # print(mhcn)
        # mhcn = sorted(mhcn)
        diemsv = Diemsv2.objects.filter(macn=macn, masv=Sinhvien.objects.get(masv=masv))
        
        x = [list(diemsv.filter(mamh=x)) for x in ref]
        x = [ k for j in x for k in j]
        # print(len(x))
        mhcn = [x.mamh.tenmh for x in mhcn]

        keys = []
        arr = []
        for i in x:
            i = i.serialize_mark()
            k = list(i.keys())[0]
            if k not in keys:
                arr.append(i)
                keys.append(k)
            else:
                index = keys.index(k)
                arr[index][k].update(i[k])
        
        for i in range(len(keys)):
            for j in mhcn:
                if j not in arr[i][keys[i]].keys():
                    arr[i][keys[i]][j] = "---"
            arr[i][keys[i]]
        
        arr.append(mhcn)
        data.append(arr)
    if action == "filter":
        print('here')
        return JsonResponse(data, safe=False)
    else:
        print("get to suggest")
        final_result = []
        for arr in data:
            macn = macns[data.index(arr)]
            print(arr)
            bangdiem_kmean_loc = {}
            for i in arr:
                diem_sv = pd.DataFrame(i)
                ma_sv = diem_sv.columns[0]
                if(ma_sv == 0):
                    break
                bangdiem_kmean_loc[ma_sv] = diem_sv.iloc[:,0]
            # print(bangdiem_kmean_loc)
            bangdiem_kmean_loc_df = pd.DataFrame(bangdiem_kmean_loc)
            bangdiem_kmean_loc_df = bangdiem_kmean_loc_df.iloc[0:8,0]
            bangdiem_kmean_loc_df = bangdiem_kmean_loc_df.transpose()
            labels = bangdiem_kmean_loc_df.index
            bangdiem_kmean_loc_df.replace('---', -1, inplace = True)
            bangdiem_kmean_loc_df = bangdiem_kmean_loc_df.replace(np.nan, -1)
            bangdiem_kmean_loc_df = bangdiem_kmean_loc_df.astype(np.float32)

            #chuyển ta dạng dataframe về list để có thể chạy được thuật toán
            bangdiem_kmean_loc_last = np.array(bangdiem_kmean_loc_df)
            bangdiem_kmean_loc_last= [list(bangdiem_kmean_loc_last)]
            # print(bangdiem_kmean_loc_last)
            data_set = bangdiem_kmean_loc_last

            # Value of K (cái này sẽ lấy từ ô text box do giáo viên nhập)
            k_value = 1

            # Độ chính xác (làm tròn sau dấu phẩy)
            precision = 5

            #bán kính để loại nhiễu (cái này sẽ lấy từ ô text box do giáo viên nhập)
            r = 10

            # chạy thuật toán
            results = km.runner(data_set, k_value, labels, r, precision)

            """
            dữ liệu trả về sẽ dạng từ điển:
                - min_distance_centroid: khoảng cách gần nhất đến tâm 
                - outlier: danh sách các sinh viên có khoảng cách đến tâm lớn hơn hoặc bằng r => ép kiểu về pd.DataFrame
                - all_: trả về một dict chứa tất cả khoảng cách của tập sinh viên đến các cụm => ép kiểu về pd.DataFrame
                - centroid: tọa độ các cụm
            """
            all_ = pd.DataFrame(results["all"])
            min_distance = results["min_distance_centroid"]
            outliers = pd.DataFrame(results["outlier"])
            centroids = pd.DataFrame(results["centroid"])
            # print(outliers)
            for i in range(all_.shape[0]):
                if all_.loc[i,"khoang cach den tam cum"] == min_distance:
                    cum = all_.loc[i,"cum"]
                    break
            toa_do = centroids.loc[cum,:]
            a = [i for i in json.loads(toa_do.to_json()).values()] # cái này là tham số  t1 trong hàm km.dist()
            # print(a)
            # print(macns[data.index(arr)]) # ddaya la ma cn
            b = list(Tuvan.objects.filter(macn=macns[data.index(arr)], makdt=makdt, manguoidung='admin'))
            x = b[0].toadotam.split('_')
            x.pop()
            b = [float(i) for i in x]
            kc = km.dist(a, b)
            # print(kc)
            # print(b)
            _8tdtam = [str(i) for i in json.loads(toa_do.to_json()).values()]
            tdtam = "_".join(_8tdtam)
            # x = json.loads(outliers.to_json())
            print(min_distance)
            print(tdtam)
            new = Tuvan(macn=macn, makdt=makdt,manguoidung=masv, kctam=min_distance, toadotam=tdtam)
            new.save()

            final_result.append(kc)
        x = max(final_result)
        # print(macns[final_result.index(x)])
        sugg = (Chuyennganh.objects.get(macn=macns[final_result.index(x)]))
        return JsonResponse({
            "suggest": sugg.tencn
        })
# Add Tuvan
@csrf_exempt
def add_tuvan(request):
    if request.method == "POST":
        data = json.loads(request.body)
        new = Tuvan(macn=data['macn'], makdt=data['makdt'], manguoidung="admin", kctam=float(data['kc_tam']), toadotam=data['toado_tam'])
        new.save()
        return JsonResponse({
            "inform": "Nhập thành công"
        })

# Update diem
@csrf_exempt
def update(request):
    if request.method == "POST":
        # try:
            data = json.loads(request.body)
            makdt = Khoadaotao.objects.get(makdt=data['makdt'])
            print(data['macn'])
            print((data['data']))
            macn = Chuyennganh.objects.get(macn=data['macn'])
            mhcn = MonhocChuyennganhLoc.objects.filter(macn=macn)
            mhcn = [Ctdaotao.objects.get(mamh=i.mamh.mamh) for i in mhcn]
          
            for student in data['data']:
                msv = list(student.keys())[0]
                masv = Sinhvien.objects.get(masv=msv)
                for i in range(8):
                    query = Diemsv2.objects.filter(mamh=mhcn[i], macn=macn, masv=masv)
                    diem = list(query)
                    if len(diem) == 0:
                        new = Diemsv2(masv=masv, macn=macn, mamh=mhcn[i], diem=float(student[msv][i]), makdt=makdt)
                        new.save()
                    # print(diem)
                    # diem = diem[0].diem
                    else:
                        diem[0].diem = float(student[msv][i])
                        diem[0].save()
            
        # except: 
            return JsonResponse({
                "inform": "Updated"
            })
        
# Add
@csrf_exempt
def add(request):
    if request.method == "POST":
        data = json.loads(request.body)
        masv = Sinhvien.objects.get(masv=data['masv'])
        makdt = Khoadaotao.objects.get(makdt=data['makdt'])
        mamh = Ctdaotao.objects.get(mamh=data['mamh'])
        macn = Chuyennganh.objects.get(macn=data['macn'])
        print(makdt,mamh,masv,macn)
        diem = float(data['diem'])
        check = list(Diemsv2.objects.filter(masv=masv, makdt=makdt, mamh=mamh, macn=macn))
        if len(check) == 0:
            new = Diemsv2.objects.create(masv=masv, mamh=mamh, diem=diem, makdt=makdt, macn=macn)
            # new.save()
            return JsonResponse({
                "inform": "Nhập điểm thành công"
                }
            )
        else: 
            return JsonResponse({
                'inform': "Đã có thông tin"
            })
            
# Hocsinh index
def student_view(request, masv):
    # ------------------------------------------
    khoadaotao = Khoadaotao.objects.all()
    monhoc = list(MonhocChuyennganh.objects.all())
    mh = [i.serialize() for i in monhoc]
    x = Chuyennganh.objects.all()
    y = [i.serialize() for i in x]
    monhoc = list(MonhocChuyennganh.objects.all())
    mh = [i.serialize() for i in monhoc]
    # ------------------------------
    sinhvien = Sinhvien.objects.get(masv=masv)
    diem = list(Diemsv2.objects.filter(masv=sinhvien))
    makdt = list(set([x.makdt.makdt for x in diem]))
    data = {}
    chuyennganh = list(Chuyennganh.objects.all())
    chuyennganh = [x.serialize() for x in chuyennganh]
    chuyennganh = [{x["macn"]: x["tencn"]} for x in chuyennganh]
    x = {}
    for i in chuyennganh:
        x.update(i)
    for i in makdt:
        data.update({
            str(i): set()
        })
    # print(data, makdt)
    for i in diem:
        for j in makdt:
            if i.makdt.makdt == j:
                data[j].add(i.macn.macn)
    for i in makdt:
        data[str(i)] = list(data[str(i)])
    for i in makdt:
        data[str(i)] = [{str(j): x[j] } for j in data[str(i)]]

    return render(request, 'student/student.html', {
        'name': sinhvien.ho + " " + sinhvien.ten,
        'masv': sinhvien.masv,
        'data': json.dumps(data), #data for nav bar
        # --------------
        'khoadaotao': khoadaotao,
        'cndata': json.dumps(y),
        'monhoc': json.dumps(mh),

    })

def mark_student(request):
    makdt = request.GET['makdt']
    macn = request.GET['macn']
    masv = request.GET['masv']
    print(makdt, masv, masv)
    makdt = Khoadaotao.objects.get(makdt=makdt)
    macn = Chuyennganh.objects.get(macn=macn)
    masv = Sinhvien.objects.get(masv=masv)
    
    diem = list(Diemsv2.objects.filter(makdt=makdt, masv=masv, macn=macn))
    diem = [{"tenmon": i.mamh.tenmh, "diem": i.diem} for i in diem]
    return JsonResponse(diem, safe=False)

def ctdaotao(request):
    kdt = list(Khoadaotao.objects.all())
    # kdt = [{'ten': i.tenkdt, 'kdt': i.makdt} for i in kdt]

    return render(request, 'student/khoadaotao.html', {
        'khoadaotao': kdt
    })
def getctdaotao(request):
    makdt = request.GET['makdt']
    ctdaotao = Ctdaotao.objects.filter(makdt=makdt)
    ctdaotao = [{"mamh": i.mamh, 'ten': i.tenmh, 'tinchi': i.tinchi, 'stt': i.sttmh} for i in ctdaotao]
    return JsonResponse(ctdaotao,safe=False)

@csrf_exempt
def delctdaotao(request):
    data = json.loads(request.body)
    for i in data:
        row = Ctdaotao.objects.get(mamh=i).delete()

    return JsonResponse({
        "inform": "Successfully delete"
    })
@csrf_exempt
def modifyctdaotao(request):
    data = json.loads(request.body)
    for i in data:
        if i[1] != i[2]:
            try:
                row = Ctdaotao.objects.get(mamh=i[2])
                return JsonResponse({
                    "inform": "Cannot change to an existing MaMH"
                })
            except:
                pass
        else:
            row = Ctdaotao.objects.get(mamh=i[1])
            row.sttmh = i[0]
            row.mamh = i[2]
            row.tenmh = i[3]
            row.tinchi = i[4]
            row.save()
    return JsonResponse({
                "inform": "Successfully change"
            })

@csrf_exempt
def createctdaotao(request):
    i = json.loads(request.body)
    try:
        x = Ctdaotao.objects.get(mamh=i[1])
        return JsonResponse({
            "inform": "Fail"
        })
    except:
        print(i[4])
        new = Ctdaotao(sttmh=i[0], mamh=i[1], tenmh=i[2], tinchi=i[3], 
        makdt=i[4])
        new.save()
        return JsonResponse({
            "inform": "Success!"
        })

def chuyennganh(request):
    kdt = list(Khoadaotao.objects.all())
    # kdt = [{'ten': i.tenkdt, 'kdt': i.makdt} for i in kdt]

    return render(request, 'student/chuyennganh.html', {
        'khoadaotao': kdt
    })

def getchuyennganh(request):
    makdt = request.GET['makdt']
    chuyennganh = Chuyennganh.objects.filter(makdt=makdt)
    chuyennganh = [{"macn": i.macn, 'ten': i.tencn, 'makdt': i.makdt, 'tenbang': i.tenbang} for i in chuyennganh]
    return JsonResponse(chuyennganh,safe=False)

@csrf_exempt
def delchuyennganh(request):
    data = json.loads(request.body)
    for i in data:
        row = Chuyennganh.objects.get(macn=i).delete()

    return JsonResponse({
        "inform": "Successfully delete"
    })

@csrf_exempt
def modifychuyennganh(request):
    data = json.loads(request.body)
    for i in data:
        if i[1] != i[0]:
            try:
                row = Chuyennganh.objects.get(macn=i[0])
                return JsonResponse({
                    "inform": "Cannot change to an existing MaCN"
                })
            except:
                pass
        else:
            row = Chuyennganh.objects.get(macn=i[1])
            row.macn = i[0]
            row.tencn = i[2]
            row.makdt = i[3]
            row.tenbang = i[4]
            row.save()
    return JsonResponse({
                "inform": "Successfully change"
            })

@csrf_exempt
def createchuyennganh(request):
    i = json.loads(request.body)
    try:
        x = Chuyennganh.objects.get(macn=i[1])
        return JsonResponse({
            "inform": "Fail"
        })
    except:
        new = Chuyennganh(macn=i[0], tencn=i[1], makdt=i[2], tenbang=i[3])
        new.save()
        return JsonResponse({
            "inform": "Success!"
        })

def khoadaotao(request):
    kdt = list(Khoadaotao.objects.all())
    # kdt = [{'ten': i.tenkdt, 'kdt': i.makdt} for i in kdt]

    return render(request, 'student/khoadaotao1.html', {
        'khoadaotao': kdt
    })

@csrf_exempt
def delkhoadaotao(request):
    data = json.loads(request.body)
    for i in data:
        row = Khoadaotao.objects.get(makdt=i).delete()

    return JsonResponse({
        "inform": "Successfully delete"
    })
@csrf_exempt
def modifykhoadaotao(request):
    data = json.loads(request.body)
    for i in data:
        if i[1] != i[0]:
            try:
                row = Khoadaotao.objects.get(makdt=i[0])
                return JsonResponse({
                    "inform": "Cannot change to an existing MaCN"
                })
            except:
                pass
        else:
            row = Khoadaotao.objects.get(makdt=i[1])
            row.makdt = i[0]
            row.tenkdt = i[2]
            row.save()
    return JsonResponse({
                "inform": "Successfully change"
            })

@csrf_exempt
def createkhoadaotao(request):
    i = json.loads(request.body)
    try:
        x = khoadaotao.objects.get(makdt=i[1])
        return JsonResponse({
            "inform": "Fail"
        })
    except:
        new = Khoadaotao(makdt=i[0], tenkdt=i[1])
        new.save()
        return JsonResponse({
            "inform": "Success!",
        })

def nguoidung(request):
    nguoidung = list(Nguoidung.objects.all())
    return render(request, 'student/user.html', {
            'nguoidung': nguoidung
        })
@csrf_exempt
def delnguoidung(request):
    data = json.loads(request.body)
    for i in data:
        row = Nguoidung.objects.get(manguoidung=i).delete()

    return JsonResponse({
        "inform": "Successfully delete"
    })
@csrf_exempt
def modifynguoidung(request):
    data = json.loads(request.body)

    for i in data:
        print(i[1])
        row = Nguoidung.objects.get(manguoidung=i[1])
        row.tennguoidung= i[0]
        row.tendangnhap = i[2]
        row.matkhau = i[3]
        row.quyennguoidung = int(i[4])
        row.save()
    return JsonResponse({
                "inform": "Successfully change"
            })

@csrf_exempt
def createnguoidung(request):
    i = json.loads(request.body)
    try:
        x = Nguoidung.objects.get(tendangnhap=i[1])
        return JsonResponse({
            "inform": "Tên đăng nhập đã tồn tại"
        })
    except:
        new = Nguoidung(tennguoidung=i[0], tendangnhap=i[1], matkhau=i[2], quyennguoidung=i[3])
        new.save()
        return JsonResponse({
            "inform": "Success!",
        })

def tuvan(request):
    tuvan = list(Tuvan.objects.all())
    return render(request, 'student/tuvan.html', {
            'tuvan': tuvan
        })

@csrf_exempt
def deltuvan(request):
    data = json.loads(request.body)
    for i in data:
        row = Tuvan.objects.get(matv=i).delete()

    return JsonResponse({
        "inform": "Successfully delete"
    })

@csrf_exempt
def modifytuvan(request):
    data = json.loads(request.body)

    for i in data:
        row = Tuvan.objects.get(matv=int(i[1]))
        row.kctam= float(i[0])
        row.macn = i[2]
        row.toadotam = (i[3])
        row.manguoidung = i[4]
        row.makdt = i[5]
        row.save()
    return JsonResponse({
                "inform": "Successfully change"
            })
@csrf_exempt
def createtuvan(request):
    i = json.loads(request.body)
    try:
        x = Tuvan.objects.get(tendangnhap=i[1])
        return JsonResponse({
            "inform": "Tên đăng nhập đã tồn tại"
        })
    except:
        new = Tuvan(kctam=float(i[0]), macn=i[1], toadotam=i[2], manguoidung=i[3], makdt=i[4])
        new.save()
        return JsonResponse({
            "inform": "Success!",
        })