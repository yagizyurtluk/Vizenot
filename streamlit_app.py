import streamlit as st
import pandas as pd

# Öğrenci Sınıfı
def calculate_average(vize, final):
    return round((vize * 0.4) + (final * 0.6), 2)

class Ogrenci:
    def __init__(self, id, adi, soyadi, sinifi, vizenot, finalnot):
        self.id = id
        self.adi = adi
        self.soyadi = soyadi
        self.sinifi = sinifi
        self.vizenot = vizenot
        self.finalnot = finalnot
        self.ortalama = calculate_average(vizenot, finalnot)

    def to_dict(self):
        return {
            "id": self.id,
            "adı": self.adi,
            "soyadı": self.soyadi,
            "sınıfı": self.sinifi,
            "vizenot": self.vizenot,
            "finalnot": self.finalnot,
            "ortalama": self.ortalama
        }

# Öğrenci Verileri
students = [
    Ogrenci(1, "Ahmet", "Yılmaz", "10A", 40, 60),
    Ogrenci(2, "Ayşe", "Kara", "11B", 70, 80),
    Ogrenci(3, "Mehmet", "Demir", "12C", 50, 90),
    Ogrenci(4, "Elif", "Çelik", "9A", 30, 50)
]

data = [student.to_dict() for student in students]

# DataFrame oluşturma
df = pd.DataFrame(data)

# Streamlit Arayüzü
st.title("Öğrenci Yönetim Sistemi")

menu = st.sidebar.selectbox("Menü", ["Tüm Öğrenciler", "ID ile Öğrenci Bul", "Yeni Öğrenci Ekle"])

if menu == "Tüm Öğrenciler":
    st.subheader("Tüm Öğrenciler")
    st.dataframe(df)

elif menu == "ID ile Öğrenci Bul":
    st.subheader("ID ile Öğrenci Verilerini Getir")
    student_id = st.number_input("Öğrenci ID Giriniz", min_value=1, step=1)
    student = df[df['id'] == student_id]

    if not student.empty:
        st.write(student)
    else:
        st.warning("Bu ID'ye ait öğrenci bulunamadı!")

elif menu == "Yeni Öğrenci Ekle":
    st.subheader("Yeni Öğrenci Ekle")
    adı = st.text_input("Adı")
    soyadı = st.text_input("Soyadı")
    sınıfı = st.text_input("Sınıfı")
    vizenot = st.number_input("Vize Notu", min_value=0, max_value=100, step=1)
    finalnot = st.number_input("Final Notu", min_value=0, max_value=100, step=1)

    if st.button("Ekle"):
        new_id = max([student.id for student in students]) + 1
        new_student = Ogrenci(new_id, adı, soyadı, sınıfı, vizenot, finalnot)
        students.append(new_student)
        df.loc[len(df)] = new_student.to_dict()
        st.success("Yeni öğrenci başarıyla eklendi!")
        st.dataframe(df)

# Not: Kalıcı veri kaydı için bir veritabanı veya dosya sistemi entegrasyonu gerekir.
