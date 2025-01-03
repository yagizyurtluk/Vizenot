import streamlit as st
import pandas as pd

st.sidebar.title("📂 Projelerim")
selected_project = st.sidebar.selectbox("📂 Proje Seç", ["📚 Öğrenci Yönetim Sistemi", "🚀 Proje 2"])

project_links = {
    "📚 Öğrenci Yönetim Sistemi": "https://vizenot.streamlit.app",
    "🚀 Proje 2": "https://allpython.streamlit.app"
}

st.sidebar.markdown(f"[{selected_project}]({project_links[selected_project]})")

# Öğrenci Sınıfı
class Ogrenci:
    def __init__(self, id, adi, soyadi, vizenot, finalnot):
        self.id = id
        self.adi = adi
        self.soyadi = soyadi
        self.vizenot = vizenot
        self.finalnot = finalnot
        self.ortalama = round((vizenot * 0.4) + (finalnot * 0.6), 2)  # Hatalı parantez düzeltildi.

    def to_dict(self):
        return {
            "ID": self.id,
            "Adı": self.adi,
            "Soyadı": self.soyadi,
            "Vize Notu": self.vizenot,
            "Final Notu": self.finalnot,
            "Ortalama": self.ortalama
        }

students = [
    Ogrenci(1, "Ahmet", "Yılmaz", 40, 60),
    Ogrenci(2, "Ayşe", "Kara", 70, 80),
    Ogrenci(3, "Mehmet", "Demir", 50, 90),
    Ogrenci(4, "Elif", "Çelik", 30, 50)
]

data = [student.to_dict() for student in students]
df = pd.DataFrame(data)

st.title("📚 Öğrenci Yönetim Sistemi")

menu = st.sidebar.radio("📋 Menü", ["Tüm Öğrenciler", "ID ile Öğrenci Bul", "Yeni Öğrenci Ekle", "📜 Kaynak Kodları Göster"])

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
    vizenot = st.number_input("Vize Notu", min_value=0, max_value=100, step=1)
    finalnot = st.number_input("Final Notu", min_value=0, max_value=100, step=1)

    if st.button("Ekle"):
        if adı and soyadı:
            new_id = max([student.id for student in students]) + 1
            new_student = Ogrenci(new_id, adı, soyadı, vizenot, finalnot)
            students.append(new_student)
            df.loc[len(df)] = new_student.to_dict()
            st.success("✅ Yeni öğrenci başarıyla eklendi!")
            st.dataframe(df, use_container_width=True)
        else:
            st.error("⚠️ Lütfen tüm alanları doldurunuz!")

elif menu == "📜 Kaynak Kodları Göster":
    st.subheader("📜 Uygulama Kaynak Kodları")
    if st.button("📂 Kodları Göster"):
        with open(__file__, "r") as file:
            code = file.read()
        st.code(code, language="python")
