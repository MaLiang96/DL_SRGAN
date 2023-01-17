"""
This public access folder is only for the students of Technical University of Munich.
The license agreement of CelebA grants access for internal use at a single site
within the same organization.

Please proceed to the original website for other purposes.

http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html
"""
# from torchvision.datasets.utils import check_integrity, download_file_from_google_drive
from torch_utils import check_integrity, download_file_from_google_drive

import os
import zipfile

# https://drive.google.com/file/d/1U4qMpKi2zzoAKxIR7b20INBJf7oPCWxI/view?usp=sharing
file_list = [
    # File ID                         MD5 Hash                            Filename
    ("1U4qMpKi2zzoAKxIR7b20INBJf7oPCWxI", "00d2c5bc6d35e252742224ab0c1e8fcb", "img_align_celeba.zip"),
    ("1CAuKogBads5T50qlD51oygffHof_vCUP", "75e246fa4810816ffd6ee81facbd244c", "list_attr_celeba.txt"),
    ("1IK37ekqgG6E268Qou3KCVNf9pOnbGIv9", "32bd1bd63d3c78cd57e08160ec5ed1e2", "identity_CelebA.txt"),
    ("11pTBRw4vDegHi2Khrq9yF6YJbuMJC7Gj", "00566efa6fedff7a56946cd1c10f1c16", "list_bbox_celeba.txt"),
    ("10B8X-XPKAONghuhTdICXjQ-FC1XKnnsZ", "cc24ecafdb5b50baae59b03474781f8c", "list_landmarks_align_celeba.txt"),
    ("1PGNdCO6IzyQ0nDnXRNoR6nR8J2FKi0tU", "d32c9cbf5e040fd4025c592c306e6668", "list_eval_partition.txt"),
]

def download_check_integrity(root, base_folder) -> bool:
    # for (file_id, md5, filename) in file_list:
        # download_file_from_google_drive(file_id, os.path.join("./data/celeba/"), filename, md5)

    with zipfile.ZipFile(os.path.join(root, base_folder, "img_align_celeba.zip"), "r") as f:
    # with os.path.join(root, base_folder, "img_align_celeba") as f:
        print("Extracting downloaded images")
        f.extractall(os.path.join(root, base_folder))

    # for (_, md5, filename) in file_list:
    #     fpath = os.path.join(root, base_folder, filename)
    #     _, ext = os.path.splitext(filename)
    #     # Allow original archive to be deleted (zip and 7z)
    #     # Only need the extracted images
    #     if ext not in [".zip", ".7z"] and not check_integrity(fpath, md5):
    #         print("Fail")
    #         return False

    print("Success")
