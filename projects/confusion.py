import itertools

import numpy as np
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import matplotlib

_PATCH_SIZE = [9, 17, 25, 41, 57]

# confusion matrix 그리는 함수 
def plot_confusion_matrix(con_mats, labels, title='', file_name = "" ,cmap=plt.cm.get_cmap('Blues'), normalize=False):
    fig, axes = plt.subplots(figsize=(15, 3),
                           nrows=1,
                           ncols=5,)
    plt.title(title)
    # plt.colorbar()
    font = {'size'   : 13}
    matplotlib.rc('font', **font)   
    for idx_con, con_mat in enumerate(con_mats):
        img = axes[idx_con].imshow(con_mat, interpolation='nearest', cmap=cmap)
        img.set_clim([0, 0.7])
        marks = np.arange(len(labels))
        nlabels = []
        for k in range(len(con_mat)):
            n = sum(con_mat[k])
            # nlabel = '{0}(n={1})'.format(labels[k],n)
            nlabel = '{0}'.format(labels[k])
            nlabels.append(nlabel)
        axes[idx_con].set_xticks(marks)
        axes[idx_con].set_yticks(marks)
        # axes[idx_con].set_xticklabels(['start', 'middel', 'end'], fontsize=12)
        # axes[idx_con].set_yticklabels(['low', 'zero', 'high'], fontsize=12)
        print(n)
        thresh = con_mat.max() / 2.
        if normalize:
            for i, j in itertools.product(range(con_mat.shape[0]), range(con_mat.shape[1])):
                axes[idx_con].text(j, i, '{0:0.2f}%'.format(con_mat[i, j] * 100), horizontalalignment="center", color="white" if con_mat[i, j] > thresh else "black")
        else:
            for i, j in itertools.product(range(con_mat.shape[0]), range(con_mat.shape[1])):
                axes[idx_con].text(j, i, con_mat[i, j], horizontalalignment="center", color="white" if con_mat[i, j] > thresh else "black")
        
        axes[idx_con].set_ylabel('True label')
        axes[idx_con].set_xlabel('Predicted label')
        axes[idx_con].set_title(f"Patch size {_PATCH_SIZE[idx_con]}", fontsize=16) 
    plt.tight_layout()
    plt.savefig(f'tmp_{file_name}.png')
    plt.close()

# array[patch][fold]
# (TN, FP, FN, TP)
confusion_AD = [
    [
        [79, 8, 8, 64], 
        [80, 7, 12, 60],
        [74, 12, 14, 58],
        [71, 15, 10, 61],
        [82, 5, 8, 64],
    ],
    [
        [79, 8, 7, 65],
        [78, 9, 10, 62],
        [73, 13, 15, 57],
        [78, 8, 12, 59],
        [81, 6, 8, 64],
    ],
    [
        [80, 7, 12, 60],
        [78, 9, 9, 63],
        [73, 13, 16, 56],
        [80, 6, 12, 59],
        [82, 5, 7, 65],
    ],
    [
        [76, 11, 8, 64],
        [79, 8, 8, 64],
        [77, 9, 17, 55],
        [78, 8, 10, 61],
        [82, 5, 6, 66],
    ],
    [
        [81, 6, 10, 62],
        [81, 6, 10, 62],
        [75, 11, 17, 55],
        [77, 9, 11, 60],
        [83, 4, 9, 63],
    ]
]
confusion_MCI = [
    [
        [66, 34, 12, 38],
        [69, 30, 15, 35],
        [68, 31, 14, 36],
        [73, 26, 12, 38],
        [65, 35, 15, 36],
    ],
    [
        [71, 29, 20, 30],
        [78, 21, 23, 27],
        [68, 31, 18, 32],
        [68, 31, 8, 42],
        [65, 35, 13, 38],
    ],
    [
        [72, 28, 14, 36],
        [65, 34, 16, 34],
        [66, 33, 11, 39],
        [76, 23, 15, 35],
        [72, 28, 19, 32],
    ],
    [
        [67, 33, 13, 37],
        [73, 26, 19, 31],
        [67, 32, 15, 35],
        [77, 22, 14, 36],
        [66, 34, 10, 41],
    ],
    [
        [58, 44, 9, 41],
        [71, 28, 16, 34],
        [69, 30, 18, 32],
        [72, 27, 6, 44],
        [68, 32, 11, 40],
    ],
]
confusion_AD_AIBL = [
    [
        [405, 71, 8, 71],
        [410, 66, 11, 68],
        [422, 54, 12, 67],
        [396, 80, 11, 68],
        [406, 70, 8, 71]
    ],
    [
        [380, 96, 7, 72],
        [402, 74, 14, 65],
        [361, 115, 9, 70],
        [406, 70, 9, 70],
        [412, 64, 7, 72]
    ],
    [
        [404, 72, 11, 68],
        [372, 104, 10, 69],
        [344, 132, 9, 70],
        [410, 66, 9, 70],
        [403, 73, 7, 72]
    ],
    [
        [363, 113, 7, 72],
        [387, 89, 13, 66],
        [395, 81, 10, 69],
        [409, 67, 9, 70],
        [391, 85, 6, 73]
    ],
    [
        [409, 67, 9, 70],
        [396, 80, 12, 67],
        [397, 79, 11, 68],
        [390, 86, 9, 70],
        [399, 77, 12, 67]
    ],
]

cm_list = []
for idx_patch, i_patch in enumerate(confusion_AD):
    tmp = [0, 0, 0, 0]
    for i_fold in i_patch:
        for idx, i_pred in enumerate(i_fold):
            tmp[idx] += i_pred
    print(tmp)

    pred = []  # 0, 1, 0, 1 
    annot = []  # 0, 0, 1, 1
    for idx, i_pred in enumerate(tmp):
        pred.append(np.ones(i_pred) * (idx % 2))
        annot.append(np.ones(i_pred) * (idx // 2))

    pred = np.hstack(pred)
    annot = np.hstack(annot)
    cm = confusion_matrix(annot, pred, labels=None, sample_weight=None, normalize='all')    
    cm_list.append(cm)

labels = ["Positive", "Negative"]
plot_confusion_matrix(cm_list, labels=labels, file_name='AD', normalize=True)

cm_list = []
for idx_patch, i_patch in enumerate(confusion_MCI):
    tmp = [0, 0, 0, 0]
    for i_fold in i_patch:
        for idx, i_pred in enumerate(i_fold):
            tmp[idx] += i_pred
    print(tmp)

    pred = []  # 0, 1, 0, 1 
    annot = []  # 0, 0, 1, 1
    for idx, i_pred in enumerate(tmp):
        pred.append(np.ones(i_pred) * (idx % 2))
        annot.append(np.ones(i_pred) * (idx // 2))

    pred = np.hstack(pred)
    annot = np.hstack(annot)
    cm = confusion_matrix(annot, pred, labels=None, sample_weight=None, normalize='all')    
    cm_list.append(cm)

labels = ["Positive", "Negative"]
plot_confusion_matrix(cm_list, labels=labels, file_name='MCI', normalize=True)


cm_list = []
for idx_patch, i_patch in enumerate(confusion_AD_AIBL):
    tmp = [0, 0, 0, 0]
    for i_fold in i_patch:
        for idx, i_pred in enumerate(i_fold):
            tmp[idx] += i_pred
    print(tmp)

    pred = []  # 0, 1, 0, 1 
    annot = []  # 0, 0, 1, 1
    for idx, i_pred in enumerate(tmp):
        pred.append(np.ones(i_pred) * (idx % 2))
        annot.append(np.ones(i_pred) * (idx // 2))

    pred = np.hstack(pred)
    annot = np.hstack(annot)
    cm = confusion_matrix(annot, pred, labels=None, sample_weight=None, normalize='all')    
    cm_list.append(cm)

labels = ["Positive", "Negative"]
plot_confusion_matrix(cm_list, labels=labels, file_name='AD_AIBL', normalize=True)
