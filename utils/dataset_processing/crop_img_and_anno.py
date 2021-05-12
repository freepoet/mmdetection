# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Project Name: mmdetection
File Name: crop_img_and_anno.py
Author: ningmq_cv@foxmail.com
Create Date: 2021/5/12
-------------------------------------------------
"""
from __future__ import division
import os
from PIL import Image
import xml.dom.minidom as xmldom
import numpy as np
import xml.etree.ElementTree as ET

ImgPath = '../../data/SSDD/VOC2007/JPEGImages/'
AnnoPath = '../../data/SSDD/VOC2007/Annotations/'
modified_anno_path='../../data/SSDD/VOC2007/Annotations_croped/'
ProcessedPath = '../../data/SSDD/VOC2007/JPEGImages_croped/'
prefix_str ='''
<annotation verified="no">
    <folder>JPEGImages</folder>
    <filename>{}</filename>
    <path>/home/ljw/FRCN_ROOT/data/VOCdevkit2007/VOC2007/JPEGImages/000001.jpg</path>
    <source>
        <database>Unknown</database>
    </source>
    <size>
        <width>416</width>
        <height>323</height>
        <depth>1</depth>
    </size>
    <segmented>0</segmented> 
    '''
suffix = '</annotation>'
new_head = '''	
    <object>
        <name>ship</name>
        <pose>Unspecified</pose>
        <truncated>0</truncated>
        <difficult>0</difficult>
		<bndbox>
			<xmin>{}</xmin>
			<ymin>{}</ymin>
			<xmax>{}</xmax>
			<ymax>{}</ymax>
		</bndbox>
	</object>
	'''


imagelist = os.listdir(ImgPath)
for image in imagelist:
    image_pre, ext = os.path.splitext(image)
    imgfile = ImgPath + image
    xmlfile = AnnoPath + image_pre + '.xml'

    DomTree = xmldom.parse(xmlfile)  # 打开xml文档
    annotation = DomTree.documentElement  # 得到xml文档对象

    # tree = ET.parse(xmlfile)
    # annotation = tree.getroot()

    filenamelist = annotation.getElementsByTagName('filename')  # [<DOM Element: filename at 0x381f788>]
    filename = filenamelist[0].childNodes[0].data  # 获取XML节点值
    namelist = annotation.getElementsByTagName('name')
    objectname = namelist[0].childNodes[0].data
    savepath = ProcessedPath + objectname
    if not os.path.exists(savepath):
        os.makedirs(savepath)

    bndbox = annotation.getElementsByTagName('bndbox')
    b = bndbox[0]
    print(b.nodeName)
    i = 1
    a = [0, 200, 0, 200]
    b = [0, 0, 200, 200]
    h = 200
    cropboxes = []


    def select(m, n):
        bbox = []
        for index in range(0, len(bndbox)):
            x1_list = bndbox[index].getElementsByTagName('xmin')  # 寻找有着给定标签名的所有的元素
            x1 = int(x1_list[0].childNodes[0].data)
            y1_list = bndbox[index].getElementsByTagName('ymin')
            y1 = int(y1_list[0].childNodes[0].data)
            x2_list = bndbox[index].getElementsByTagName('xmax')
            x2 = int(x2_list[0].childNodes[0].data)
            y2_list = bndbox[index].getElementsByTagName('ymax')
            y2 = int(y2_list[0].childNodes[0].data)
            print("the number of the box is", index)
            print("the xy", x1, y1, x2, y2)
            if x1 >= m and x2 <= m + h and y1 >= n and y2 <= n + h:
                print(x1, y1, x2, y2)
                a1 = x1 - m
                b1 = y1 - n
                a2 = x2 - m
                b2 = y2 - n
                bbox.append([a1, b1, a2, b2])  # 更新后的标记框
        if bbox is not None:
            return bbox
        else:
            return 0


    cropboxes = np.array(
        [[a[0], b[0], a[0] + h, b[0] + h], [a[1], b[1], a[1] + h, b[1] + h], [a[2], b[2], a[2] + h, b[2] + h],
         [a[3], b[3], a[3] + h, b[3] + h]])
    img = Image.open(imgfile)
    for j in range(0, len(cropboxes)):
        print("the img number is :", j)
        Bboxes = select(a[j], b[j])
        if Bboxes is not 0:
            head_str = ''
            for Bbox in Bboxes:
                head_str = head_str + new_head.format(Bbox[0], Bbox[1], Bbox[2], Bbox[3])
        cropedimg = img.crop(cropboxes[j])
        xml = prefix_str.format(image) + head_str + suffix
        cropedimg.save(savepath + '/' + image_pre + '_' + str(j) + '.jpg')
        open(modified_anno_path+image_pre+'_'+'{}th_patch.xml'.format(j), 'w').write(xml)

