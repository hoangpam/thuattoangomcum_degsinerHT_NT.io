import pandas as pd
import numpy as np
import random
import time

def get_outlier(dict_kmean, r):
    df_phan_cum_sv = pd.DataFrame(dict_kmean)
    df_phan_cum_sv = df_phan_cum_sv[df_phan_cum_sv["khoang cach den tam cum"] >= r]
    return dict(df_phan_cum_sv)

def get_min_distance(dict_kmean):
    df_phan_cum_sv = pd.DataFrame(dict_kmean)
    return min(df_phan_cum_sv["khoang cach den tam cum"])


def calc_time_taken(method):
    """Phương thức tính thời gian"""
    def wrapper(*args):
        # Start clock
        start = time.time()
        # Run the method
        method(*args)
        # Stop clock
        end = time.time()
        # Time taken
        print("Time taken: " + str(end-start) + " s")
    return wrapper

def distance(cluster, centroid):
    distances = []
    for point in cluster:
        dis = dist(point, centroid)
        distances.append(dis)
    return distances

def dist(p1, p2):
    """Phương thức trả về khoảng cách euclid giữa hai điểm"""
    return np.linalg.norm(np.array(p1)-np.array(p2))


def cal_centroids(_, precision):
    """Phương thức trả về tọa độ các centroid"""
    centroids = []
    for item in _:
        ele = len(item[0])
        c_item = []
        for i in range(ele):
            c_item.append(round(np.mean([li[i] for li in item]), precision))
        centroids.append(c_item)
    return centroids


def compare_lists(list_1, list_2):
    """Phương thức trả về true khi hai list giống nhau và ngược lại"""
    flag = True
    for item in list_1:
        if item not in list_2:
            flag = False
        break
    if flag:
        return True
    else:
        return False


def runner(data, k, labels, r, prec=5):
    """Runner method for K-Means Clustering"""
    # khởi tạo ngẫu nhiên tạo độ các centroid ban đầu
    indices = random.sample(range(len(data)), k)
    centroids = []
    for index in indices:
        centroids.append(data[index])
    
    # Initialization of counter value to count no of iterations needed
    counter = 0
    # Loop that does the iterative calculations
    while True:
        # In giá trị số lần lặp hiện tại
#         print("Lần lặp thứ ",counter)
        
        # Updates the counter value
        counter += 1
        # Khởi tạo list clusters để lưu danh sách các nhóm
        clusters = []
        clusters_label = []
        for i in range(k):
            clusters.append([])
            clusters_label.append([])
        # Tính toán khoảng cách Euclide giữa mỗi điểm trong tập dữ liệu và centroid
        for i,point in enumerate(data):
            distances = []
            for centroid in centroids:
                distances.append(dist(point, centroid))
            # Việc phân cụm từng điểm xảy ra trong bước này
            clusters[distances.index(min(distances))].append(point)
            clusters_label[distances.index(min(distances))].append(labels[i])
            
        # tính các điểm tạo độ mới của các centroid
        new_centroids = cal_centroids(clusters, prec)
        
        # in thử giá trị tọa dộ cũ và mới của các centroids
        #print("===== Tọa độ cũ các centroids: ",centroids)
        #print("===== Tọa độ mới các centroids: ",new_centroids,"\n\n")
        
        # khi các giá trị mới và cũ của tất cả các centroid không thay đổi thì dừng thuật toán
        if compare_lists(centroids, new_centroids):
            break
        
        # Cập nhật các centroid mới cho lần lặp tiếp theo
        centroids = new_centroids
        
        
    
    # In tọa độ các centroids khi đã chạy xong thuật toán
    #print("Giá trị tọa độ cuối cùng của các centorid: ",centroids,"\n\n")
    dict_kmean = {}
    dict_kmean["cum"] = []
    dict_kmean["ma SV"] = []
    dict_kmean["khoang cach den tam cum"] = []
    for i, cluster in enumerate(clusters):
        #print("\nKhoảng cách từ các điểm trong cụm đến tâm cụm ",i,":\n",distance(cluster, centroids[i]))
        #print("Các điểm thuộc cụm ",i,":",clusters_label[i])
        if(len(dict_kmean["ma SV"]) == 0):
            cums = np.ones(len(clusters_label[i]),)
            cums = cums*i
            dict_kmean["cum"] = cums
            dict_kmean["ma SV"] = clusters_label[i]
            dict_kmean["khoang cach den tam cum"] = distance(cluster, centroids[i])
        else:
            cums = np.ones(len(clusters_label[i]),)
            cums = cums*i
            dict_kmean["cum"] = np.concatenate((dict_kmean["cum"], cums))
            dict_kmean["ma SV"] = dict_kmean["ma SV"] + clusters_label[i]
            dict_kmean["khoang cach den tam cum"] = dict_kmean["khoang cach den tam cum"] + distance(cluster, centroids[i])
    """
    dữ liệu trả về sẽ dạng từ điển:
        - min_distance_centroid: khoảng cách gần nhất đến tâm
        - outlier: danh sách các sinh viên có khoảng cách đến tâm lớn hơn hoặc bằng r    
        - all: trả về một dict chứa tất cả khoảng cách của tập sinh viên đến các cụm
    """
    outliers = get_outlier(dict_kmean, r)
    min_distance = get_min_distance(dict_kmean)
    
    results = {}
    results["all"] = dict_kmean
    results["min_distance_centroid"] = min_distance
    results["outlier"] = outliers
    results["centroid"] = centroids
    
    return results




 