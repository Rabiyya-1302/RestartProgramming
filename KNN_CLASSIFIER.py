# Full dataset — 30 points [weight_grams, sweetness_1to10]
import math
dataset = [
    {"features": [152, 7], "label": "apple"},
    {"features": [168, 6], "label": "apple"},
    {"features": [143, 8], "label": "apple"},
    {"features": [158, 5], "label": "apple"},
    {"features": [172, 7], "label": "apple"},
    {"features": [139, 9], "label": "apple"},
    {"features": [161, 6], "label": "apple"},
    {"features": [155, 8], "label": "apple"},
    {"features": [148, 7], "label": "apple"},
    {"features": [165, 5], "label": "apple"},

    {"features": [190, 9], "label": "orange"},
    {"features": [205, 8], "label": "orange"},
    {"features": [183, 9], "label": "orange"},
    {"features": [212, 7], "label": "orange"},
    {"features": [197, 8], "label": "orange"},
    {"features": [178, 9], "label": "orange"},
    {"features": [220, 7], "label": "orange"},
    {"features": [195, 8], "label": "orange"},
    {"features": [188, 9], "label": "orange"},
    {"features": [201, 8], "label": "orange"},

    {"features": [118, 9], "label": "banana"},
    {"features": [132, 8], "label": "banana"},
    {"features": [109, 9], "label": "banana"},
    {"features": [125, 8], "label": "banana"},
    {"features": [137, 9], "label": "banana"},
    {"features": [112, 8], "label": "banana"},
    {"features": [128, 9], "label": "banana"},
    {"features": [121, 8], "label": "banana"},
    {"features": [135, 9], "label": "banana"},
    {"features": [115, 8], "label": "banana"},
]

# Split — first 24 for training (80%), last 6 for testing (20%)
# 8 apples, 8 oranges, 8 bananas → train
# 2 apples, 2 oranges, 2 bananas → test
train_data = dataset[:8] + dataset[10:18] + dataset[20:28]
test_data  = dataset[8:10] + dataset[18:20] + dataset[28:30]
def euclidean(point1,point2):
    total=0
    for i in range(len(point1)):
        total+=(point2[i]-point1[i])**2
def knn_predict(test):
    for i in range(len(dataset)):
        x=euclidean(test["features"],dataset[i]["features"])
        distance=[]
        distance.append(x)
    distance.sort()
    k=distance[0]
        
    
