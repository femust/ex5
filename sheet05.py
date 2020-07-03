import numpy as np
import cv2 as cv
import cv2.xfeatures2d as features
import os
import yaml

def create_lable_vector():

    label_vector = [
    'shampoo',
    'medicin',
    'milkBIO',
    'juiceAPPLE',
    'juiceORANGE',
    'juiceHAPPY',
    'waterVITTEL',
    'dressing',
    'candida',
    'chips',
    'toilettePaper',
    'beer',
    'clock',
    'candidaLEMON',
    'drummer',
    'cat',
    'apple',
    'monstertruck',
    'plane',
    'mic',
    'paper',
    'zebra',
    'tom',
    'hairdryer',
    'basket',
    'shoe',
    'walkman',
    'camera',
    'Total',
    'muiltisocket',
    'babyShampoo',
    'thaiRice',
    'teaCup',
    'babyPhone',
    'cup',
    'planeWithPilot',
    'babySoundThing',
    'coockingPot',
    'trumpet',
    'weirdGuy',
    'shoeRed',
    'fruits',
    'mocca',
    'littelAngelRice',
    'polizei',
    'nescafe',
    'miniDisk',
    'videoTape',
    'bookReterieval',
    'cupGoofi',
    'schneider',
    'fireWire',
    'oracle8'
    ]

    return label_vector


def generate_bow_response_hist(vocabulary_path, image_path, img_num, bag_num, feat_type='SIFT'):
    voc_file_path = os.path.join(vocabulary_path, 'vocabulary.yaml')

    # for i in np.arange(2):
    #     img = cv.imread(image_path + )


    print(voc_file_path)
    print(image_path)
    print(img_num)
    print(bag_num)
    if os.path.isfile(voc_file_path):
        print("Load vocabulary from %s" % voc_file_path)
        # _________________ ToDo _________________
    else:
        print("Generating vocabulary")
        bow = cv.BOWKMeansTrainer(bag_num)

        descriptors = []
        # _________________ ToDO _________________
        print("DONE")

        print("Writing vocabulary to %s" % voc_file_path )
        # _________________ ToDO _________________


    # _________________ ToDO _________________

    for i_idx in range(img_num):
        bow_responce_hist_path = os.path.join(vocabulary_path, "BOW_response_hist_%d.yaml" % i_idx)
        file_path = os.path.join(image_path, "{:03d}.jpg".format(i_idx))
        print(file_path)
        img = cv.imread(file_path)
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        sift = cv.xfeatures2d.SURF_create()
        #sift = features.SURF_create()
        kp = sift.detect(gray, None)
        img = cv.drawKeypoints(gray, kp)
        cv.imshow(img)

        # _________________ ToDO _________________
    response_hists = []
    return response_hists,response_hists



def l2_mat_distance(X):

    # _________________ ToDO _________________

     return l2


def mahalanobis_disstance(X, M):

    # _________________ ToDO _________________

    return distances


def knn_classification(knn, img_num, distances):
    print("Classify with knn = %d" % knn)
    final_distances = []
    final_labels = []

    # iterate over all testing images
    for i_idx in range(img_num):
        pass

        # _________________ ToDO _________________

    #print("FINAL ALL", all)
    #print("FINAL WRONG", wrong)
    #print("WRONG/ALL", wrong / all)

def task_1(image_path, vocabulary_path, img_num, bag_num):
    response_hists_surf = generate_bow_response_hist(vocabulary_path,
                                                image_path,
                                                img_num,
                                                bag_num, 'SURF')

    # response_hists_sift = generate_bow_response_hist(vocabulary_path,
    #                                             image_path,
    #                                             img_num,
    #                                             bag_num)
    # return response_hists_surf, response_hists_sift

def task_2(response_hists, img_num):
    pass
    # # __________ Your Part Here __________

    # knn_classification(1, img_num, distances)
    # print("----------------")
    # knn_classification(3, img_num, distances)


def task_3(response_hists, img_num):
    pass

    # _______ Your Part Here _________

    # knn_classification(1, img_num, distances)
    # print("----------------")
    # knn_classification(3, img_num, distances)


def main():

    img_num = 265
    bag_num = 55

    vocabulary_path = "./offline/{:04d}".format(bag_num)
    image_path = "./images/"

    print("TASK 1")
    task_1(image_path, vocabulary_path, img_num, bag_num)
    #response_hists_surf, response_hists_sift = task_1(image_path, vocabulary_path, img_num, bag_num)
    # print("TASK 2")
    # task_2(response_hists_surf, img_num)
    # print("TASK 3")
    # task_3(response_hists_sift, img_num)


if __name__ == '__main__':
    print(cv.__version__)
    print("hello!")
    main()
