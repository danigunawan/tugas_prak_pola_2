import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
from dotenv import load_dotenv
load_dotenv()

dataset_path = os.getenv("DATASET_PATH")
data_csv_path = os.path.join(dataset_path, "Data.csv")
data = pd.read_csv(data_csv_path, sep=";")
print(data)

data_txt_path = os.path.join(dataset_path, "Data.txt")
print("\nRead text data with tab delimiter")
with open(data_txt_path) as data_file:
    print(data_file.read())

traffic_data_path = os.path.join(dataset_path, "web_traffic.tsv")
traffic = np.genfromtxt(traffic_data_path, delimiter='\t')

print("First 10 rows of traffic data:")
print(traffic[:10])
print(f"Traffic data shape: {traffic.shape}")

x = traffic[:, 0]
y = traffic[:, 1]
x = x[~np.isnan(y)]
y = y[~np.isnan(y)]

plt.figure(figsize=(8, 5))
plt.scatter(x, y)
plt.title("Web Traffic Last Month")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w * 7 * 24 for w in range(10)], [f'Week {w}' for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show(block=False) 

print("\nOperasi Image dengan OpenCV\n")

image_ipb_path = os.path.join(dataset_path, "ipb.png")
image = cv2.imread(image_ipb_path)

print(f"Shape image: {image.shape}")
print(f"Size image: {image.size}")

plt.figure(figsize=(5, 5))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 
plt.axis("off")
plt.title("Original IPB Image")
plt.show(block=False)

babon_dataset_path = os.path.join(dataset_path, "5.png")
babon = cv2.imread(babon_dataset_path)
babon_gray = cv2.cvtColor(babon, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(babon, cv2.COLOR_BGR2RGB)) 
plt.title("Original Babon Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(babon_gray, cmap="gray")
plt.title("Grayscale Babon Image")
plt.axis("off")

plt.show(block=False)
plt.show()
