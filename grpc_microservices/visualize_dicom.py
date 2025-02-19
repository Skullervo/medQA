import pydicom
import matplotlib.pyplot as plt

# 🔹 Luetaan DICOM-tiedosto
dicom_file = "test.dcm"
dataset = pydicom.dcmread(dicom_file)

# 🔍 Tulostetaan DICOM-metatiedot
print("\n📄 DICOM Metadata:\n")
print(dataset)

# 🔍 Näytetään kuva, jos siinä on pikselitietoa
if "PixelData" in dataset:
    image_array = dataset.pixel_array  # Muutetaan numpy-taulukoksi
    
    # 📊 Näytetään kuva
    plt.figure(figsize=(8, 8))
    plt.imshow(image_array, cmap="gray")
    plt.title("DICOM Image")
    plt.axis("off")
    plt.show()
else:
    print("❌ Tämä DICOM-tiedosto ei sisällä kuvaa!")
