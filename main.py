import pandas as pd
import numpy as np

# Filtrelenmiş Excel dosyasını oku
file_path = r"C:\Users\yasar\Downloads\aylik_yagis_verileri_filtered.xlsx"
df = pd.read_excel(file_path)

# Yılları ve aylık yağış değerlerini al
years = df["Year_Month"].values
monthly_rainfall = df["Value"].values.reshape(-1, 12)  # Her yıl için 12 ay olmalı

# SPI Hesaplama Fonksiyonu
def calculate_spi(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return (data - mean) / std_dev if std_dev != 0 else np.zeros(len(data))

# Kuraklık Durumu Belirleme Fonksiyonu
def determine_drought_level(spi_value):
    if spi_value >= 1.5:
        return "Çok Nemli"
    elif 1.0 <= spi_value < 1.5:
        return "Nemli"
    elif 0 <= spi_value < 1.0:
        return "Hafif Nemli"
    elif -1.0 < spi_value < 0:
        return "Hafif Kurak"
    elif -1.5 < spi_value <= -1.0:
        return "Orta Kurak"
    else:
        return "Şiddetli Kurak"

# 1 Aylık Periyot SPI Hesaplama
one_month_spi = []
for month in range(12):
    monthly_values = monthly_rainfall[:, month]
    spi = calculate_spi(monthly_values)
    one_month_spi.extend(spi)
# 1 Aylık verileri kaydet
df_one_month = pd.DataFrame({
    'Year': years[:len(one_month_spi)],
    'SPI Value': one_month_spi,
    'Drought Level': [determine_drought_level(spi) for spi in one_month_spi]
})
df_one_month.to_excel("1_Aylik_Periyot_SPI.xlsx", index=False)

# 3 Aylık Periyot SPI Hesaplama
three_month_spi = []
three_month_groups = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]]
for group in three_month_groups:
    group_values = []
    for year in range(len(years)):
        if group == [0, 1, 2] and year == len(years) - 1:
            continue
        if year < len(monthly_rainfall):
            group_data = np.sum(monthly_rainfall[year, group])
            group_values.append(group_data)
    spi = calculate_spi(np.array(group_values))
    three_month_spi.extend(spi)
# 3 Aylık verileri kaydet
df_three_month = pd.DataFrame({
    'Year': years[:len(three_month_spi)],
    'SPI Value': three_month_spi,
    'Drought Level': [determine_drought_level(spi) for spi in three_month_spi]
})
df_three_month.to_excel("3_Aylik_Periyot_SPI.xlsx", index=False)

# 6 Aylık Periyot SPI Hesaplama
six_month_spi = []
six_month_groups = [[9, 10, 11, 0, 1, 2], [3, 4, 5, 6, 7, 8]]
for group in six_month_groups:
    group_values = []
    for year in range(len(years) - (1 if group[0] == 0 else 0)):
        if year < len(monthly_rainfall):
            group_data = np.sum(monthly_rainfall[year, group])
            group_values.append(group_data)
    spi = calculate_spi(np.array(group_values))
    six_month_spi.extend(spi)
# 6 Aylık verileri kaydet
df_six_month = pd.DataFrame({
    'Year': years[:len(six_month_spi)],
    'SPI Value': six_month_spi,
    'Drought Level': [determine_drought_level(spi) for spi in six_month_spi]
})
df_six_month.to_excel("6_Aylik_Periyot_SPI.xlsx", index=False)

# 8 Aylık Periyot SPI Hesaplama (Eylül - Nisan)
eight_month_spi = []
eight_month_groups = [[0, 1, 2, 3,8,9,10,11]]
for group in eight_month_groups:
    group_values = []
    for year in range(len(years) - (1 if group[0] == 0 else 0)):
        if year < len(monthly_rainfall):
            group_data = np.sum(monthly_rainfall[year, group])
            group_values.append(group_data)
    spi = calculate_spi(np.array(group_values))
    eight_month_spi.extend(spi)
# 8 Aylık verileri kaydet
df_eight_month = pd.DataFrame({
    'Year': years[:len(eight_month_spi)],
    'SPI Value': eight_month_spi,
    'Drought Level': [determine_drought_level(spi) for spi in eight_month_spi]
})
df_eight_month.to_excel("8_Aylik_Periyot_SPI.xlsx", index=False)

# 10 Aylık Periyot SPI Hesaplama
ten_month_spi = []
ten_month_groups = [[0, 1, 2, 3, 4,5, 8,9,10,11]]
for group in ten_month_groups:
    group_values = []
    for year in range(len(years) - (1 if group[0] == 0 else 0)):
        if year < len(monthly_rainfall):
            group_data = np.sum(monthly_rainfall[year, group])
            group_values.append(group_data)
    spi = calculate_spi(np.array(group_values))
    ten_month_spi.extend(spi)
# 10 Aylık verileri kaydet
df_ten_month = pd.DataFrame({
    'Year': years[:len(ten_month_spi)],
    'SPI Value': ten_month_spi,
    'Drought Level': [determine_drought_level(spi) for spi in ten_month_spi]
})
df_ten_month.to_excel("10_Aylik_Periyot_SPI.xlsx", index=False)

# 12 Aylık Periyot SPI Hesaplama
twelve_month_spi = []
twelve_month_groups = [[0, 1, 2, 3, 4,5, 6 ,7, 8,9,10,11]]
for group in twelve_month_groups:
    group_values = []
    for year in range(len(years) - (1 if group[0] == 0 else 0)):
        if year < len(monthly_rainfall):
            group_data = np.sum(monthly_rainfall[year, group])
            group_values.append(group_data)
    spi = calculate_spi(np.array(group_values))
    twelve_month_spi.extend(spi)
# 12 Aylık verileri kaydet
df_twelve_month = pd.DataFrame({
    'Year': years[:len(twelve_month_spi)],
    'SPI Value': twelve_month_spi,
    'Drought Level': [determine_drought_level(spi) for spi in twelve_month_spi]
})
df_twelve_month.to_excel("12_Aylik_Periyot_SPI.xlsx", index=False)

print("Tüm periyotlar başarıyla kaydedildi.")
