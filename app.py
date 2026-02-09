import streamlit as st
import pandas as pd

# عنوان التطبيق
st.title("🛠️ Domain Intelligence & Generation Tool")
st.markdown("**أداة تحليل الكلمات المفتاحية وتوليد أسماء نطاقات براندابل**")

st.write("---")
uploaded_file = st.file_uploader("ارفع ملف dotDB (CSV أو Excel)", 
                                 type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
        
        st.success(f"✅ تم رفع الملف بنجاح! عدد الصفوف الأصلي: {len(df)}")
        
        # تنظيف البيانات
        if 'keyword' in df.columns:  # تغيير إلى 'keyword' بدلاً من 'Keyword' للتوافق
            df['keyword'] = df['keyword'].str.lower().str.strip()  # تحويل لأحرف صغيرة وإزالة مسافات
            st.success("✅ تم تنظيف عمود 'keyword' (تحويل لصغيرة وإزالة مسافات)!")
        
        # فلتر أساسي: فقط الكلمات ذات extension_count > 700 (يمكن تعديل الرقم)
        if 'extension_count' in df.columns:  # تغيير إلى 'extension_count' للتوافق
            df_filtered = df[df['extension_count'] > 700]
            st.info(f"📊 بعد الفلتر (>700): {len(df_filtered)} كلمة مفتاحية متبقية")
            st.dataframe(df_filtered.head(20))  # يعرض أول 20 صف بعد الفلتر
        else:
            st.dataframe(df.head(20))  # إذا لم يكن هناك عمود فلتر، عرض الأصلي
        
        st.write(f"**عدد الأعمدة:** {len(df.columns)}")
        st.write(f"**أسماء الأعمدة:** {list(df.columns)}")
        
    except Exception as e:
        st.error(f"خطأ في قراءة أو معالجة الملف: {e}")
else:
    st.info("👆 ارفع ملف CSV أو Excel من dotDB للبدء")
