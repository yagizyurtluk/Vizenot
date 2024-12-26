import streamlit as st
import pandas as pd

# GitHub Bağlantıları
st.sidebar.title("📂 GitHub Projelerim")
st.sidebar.markdown("[📚 Öğrenci Yönetim Sistemi](https://github.com/kullanici/ogrenci-yonetim-sistemi)")
st.sidebar.markdown("[🚀 Proje 2](https://github.com/kullanici/proje-2)")
st.sidebar.markdown("[🔧 Proje 3](https://github.com/kullanici/proje-3)")

# Öğrenci Sınıfı
class Ogrenci:
    def __init__(self, id, adi, soyadi, sinifi, vizenot, finalnot):
        self.id = id
        self.adi = adi
        self.soyadi = soyadi
        self.sinifi = sinifi
        self.vizenot = vizenot
        self.finalnot = finalnot
        self.ortalama = round((vizenot * 0.4) + (finalnot * 0.6), 2)

    def to_dict(self):
        return {
            "ID": self.id,
            "Adı": self.adi,
            "Soyadı": self.soyadi,
            "Sınıfı": self.sinifi,
            "Vize Notu": self.vizenot,
            "Final Notu": self.finalnot,
            "Ortalama": self.ortalama
        }

# Öğrenci Verileri
students = [
    Ogrenci(1, "Ahmet", "Yılmaz", "10A", 40, 60),
    Ogrenci(2, "Ayşe", "Kara", "11B", 70, 80),
    Ogrenci(3, "Mehmet", "Demir", "12C", 50, 90),
    Ogrenci(4, "Elif", "Çelik", "9A", 30, 50)
]

# DataFrame oluşturma
data = [student.to_dict() for student in students]
df = pd.DataFrame(data)

# Streamlit Arayüzü
st.title("📚 Öğrenci Yönetim Sistemi")

menu = st.sidebar.radio("📋 Menü", ["Tüm Öğrenciler", "ID ile Öğrenci Bul", "Yeni Öğrenci Ekle"])

if menu == "Tüm Öğrenciler":
    st.subheader("👩‍🎓 Tüm Öğrenciler")
    st.dataframe(df, use_container_width=True)

elif menu == "ID ile Öğrenci Bul":
    st.subheader("🔍 ID ile Öğrenci Verilerini Getir")
    student_id = st.number_input("Öğrenci ID Giriniz", min_value=1, step=1)
    student = df[df['ID'] == student_id]

    if not student.empty:
        st.table(student)
    else:
        st.warning("❌ Bu ID'ye ait öğrenci bulunamadı!")

elif menu == "Yeni Öğrenci Ekle":
    st.subheader("➕ Yeni Öğrenci Ekle")
    adı = st.text_input("Adı")
    soyadı = st.text_input("Soyadı")
    sınıfı = st.text_input("Sınıfı")
    vizenot = st.number_input("Vize Notu", min_value=0, max_value=100, step=1)
    finalnot = st.number_input("Final Notu", min_value=0, max_value=100, step=1)

    if st.button("Ekle"):
        if adı and soyadı and sınıfı:
            new_id = max([student.id for student in students]) + 1
            new_student = Ogrenci(new_id, adı, soyadı, sınıfı, vizenot, finalnot)
            students.append(new_student)
            df.loc[len(df)] = new_student.to_dict()
            st.success("✅ Yeni öğrenci başarıyla eklendi!")
            st.dataframe(df, use_container_width=True)
        else:
            st.error("⚠️ Lütfen tüm alanları doldurunuz!")

# Not: Kalıcı veri kaydı için bir veritabanı veya dosya sistemi entegrasyonu gerekir.
