import numpy as np
from PIL import Image
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Exercise 2.1

# Download image
image = Image.open("Jonathan.jpg")
width = image.size[0]
length = image.size[1]
jonathancolor = np.array(image.getdata())
jonathan = jonathancolor.reshape(length, width, 3)

# find number of pixels
num_pixels = width*length
print("\nExercise 2.1:")
print("      Number of pixels: ", num_pixels)


# Exercise 2.2

# compute KMeans for k = 4, 6, 8
# store cluster centers and labels for each pixel
k_list = [4, 6, 8]
num_of_clusters = len(k_list)
cluster_centers_k = []
labels_k = []
for k in k_list:
    km_clf = KMeans(n_clusters=k)
    km_clf.fit(jonathancolor)
    cluster_centers = km_clf.cluster_centers_
    int_centers = cluster_centers.astype(int)
    data_labels = km_clf.labels_
    cluster_centers_k.append(int_centers)
    labels_k.append(data_labels)
    '''
    if k == 4:
        cluster_centers_k_4 = int_centers
        labels_k_4 = data_labels
    elif k == 6:
        cluster_centers_k_6 = int_centers
        labels_k_6 = data_labels
    else:
        cluster_centers_k_8 = int_centers
        labels_k_8 = data_labels
    '''
print("\nExercise 2.2:")
for i, k in enumerate(k_list):
    print("k = {} cluster centers:\n".format(k), cluster_centers_k[i])
'''
print("k = 4 cluster centers:\n", cluster_centers_k_4)
print("k = 6 cluster centers:\n", cluster_centers_k_6)
print("k = 8 cluster centers:\n", cluster_centers_k_8)
'''


# Exercise 2.3

# use cluster centers and labels to give each pixel a value
jonathancolor_comp_k = np.zeros((num_of_clusters, num_pixels, 3)).astype(int)
'''
jonathancolor_comp_k_4 = np.zeros((num_pixels, 3)).astype(int)
jonathancolor_comp_k_6 = np.zeros((num_pixels, 3)).astype(int)
jonathancolor_comp_k_8 = np.zeros((num_pixels, 3)).astype(int)
'''
for i in range(num_pixels):
    for j in range(num_of_clusters):
        jonathancolor_comp_k[j, i] = cluster_centers_k[j][labels_k[j][i]]
    '''
    jonathancolor_comp_k_4[i] = cluster_centers_k_4[labels_k_4[i]]
    jonathancolor_comp_k_6[i] = cluster_centers_k_6[labels_k_6[i]]
    jonathancolor_comp_k_8[i] = cluster_centers_k_8[labels_k_8[i]]
    '''

jonathan_compressed_k = []
for i in range(num_of_clusters):
    jonathan_compressed_k.append(jonathancolor_comp_k[i].reshape(length, width, 3))
'''
jonathan_compressed_k_4 = jonathancolor_comp_k_4.reshape(length, width, 3)
jonathan_compressed_k_6 = jonathancolor_comp_k_6.reshape(length, width, 3)
jonathan_compressed_k_8 = jonathancolor_comp_k_8.reshape(length, width, 3)
'''


# plot image for each k
fig = plt.figure(figsize=(10, 5))
rows = 1
columns = num_of_clusters

for i in range(0, num_of_clusters):
    fig.add_subplot(rows, columns, i+1)
    plt.imshow(jonathan_compressed_k[i])
    plt.axis('off')
    plt.title('k = {}'.format(k_list[i]))

'''
fig.add_subplot(rows, columns, 1)
plt.imshow(jonathan_compressed_k_4)
plt.axis('off')
plt.title('k = 4')

fig.add_subplot(rows, columns, 2)
plt.imshow(jonathan_compressed_k_6)
plt.axis('off')
plt.title('k = 6')

fig.add_subplot(rows, columns, 3)
plt.imshow(jonathan_compressed_k_8)
plt.axis('off')
plt.title('k = 8')
'''

plt.show()


# plt.figure(1)
# plt.clf()
# plt.axis('off')
# plt.title('compressed image (k colors)')
# plt.imshow(jonathan_compressed_k_4)
# #plt.imshow(jonathan_compressed_k_6)
# #plt.imshow(jonathan_compressed_k_8)
# plt.show()
