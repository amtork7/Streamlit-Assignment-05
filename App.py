import streamlit as st

# ------------------------------
# Language Selection (Bonus)
# ------------------------------
language = st.sidebar.radio(
    "Select Language / اختر اللغة",
    ["English", "العربية"]
)

if language == "English":
    st.title("🎓 Grade Calculator")

    st.markdown("""
    ## Instructions
    **Enter the scores** for four subjects, select a grading scale,
    and click **Calculate Grade**.

    ### Features
    - Four subject score inputs
    - Two grading scales
    - Letter grade calculation
    - Result displayed in a coloured message box
    """)

    subject1 = st.number_input("Subject 1 Score", 0, 100, 50)
    subject2 = st.number_input("Subject 2 Score", 0, 100, 50)
    subject3 = st.number_input("Subject 3 Score", 0, 100, 50)
    subject4 = st.number_input("Subject 4 Score", 0, 100, 50)

    grading_scale = st.radio(
        "Select Grading Scale",
        ["Standard", "Strict"]
    )

    st.info("Enter all scores before calculating.")

    if st.button("Calculate Grade"):

        average = (subject1 + subject2 + subject3 + subject4) / 4

        if grading_scale == "Standard":
            if average >= 90:
                grade = "A"
            elif average >= 80:
                grade = "B"
            elif average >= 70:
                grade = "C"
            elif average >= 60:
                grade = "D"
            else:
                grade = "F"

        else:  # Strict
            if average >= 95:
                grade = "A"
            elif average >= 85:
                grade = "B"
            elif average >= 75:
                grade = "C"
            elif average >= 65:
                grade = "D"
            else:
                grade = "F"

        if grade == "A":
            st.success(f"Excellent! Your grade is {grade} (Average: {average:.2f})")
        elif grade in ["B", "C"]:
            st.info(f"Your grade is {grade} (Average: {average:.2f})")
        elif grade == "D":
            st.warning(f"Your grade is {grade} (Average: {average:.2f})")
        else:
            st.error(f"Your grade is {grade} (Average: {average:.2f})")

else:
    st.title("🎓 حاسبة الدرجات")

    st.markdown("""
    ## التعليمات
    **أدخل درجات** أربعة مواد، واختر نظام التقييم،
    ثم اضغط على **حساب الدرجة**.

    ### المميزات
    - إدخال درجات أربع مواد
    - نظامان للتقييم
    - حساب التقدير
    - عرض النتيجة في رسالة ملونة
    """)

    subject1 = st.number_input("درجة المادة الأولى", 0, 100, 50)
    subject2 = st.number_input("درجة المادة الثانية", 0, 100, 50)
    subject3 = st.number_input("درجة المادة الثالثة", 0, 100, 50)
    subject4 = st.number_input("درجة المادة الرابعة", 0, 100, 50)

    grading_scale = st.radio(
        "اختر نظام التقييم",
        ["قياسي", "صارم"]
    )

    st.info("أدخل جميع الدرجات قبل الحساب.")

    if st.button("حساب الدرجة"):

        average = (subject1 + subject2 + subject3 + subject4) / 4

        if grading_scale == "قياسي":
            if average >= 90:
                grade = "A"
            elif average >= 80:
                grade = "B"
            elif average >= 70:
                grade = "C"
            elif average >= 60:
                grade = "D"
            else:
                grade = "F"
        else:
            if average >= 95:
                grade = "A"
            elif average >= 85:
                grade = "B"
            elif average >= 75:
                grade = "C"
            elif average >= 65:
                grade = "D"
            else:
                grade = "F"

        if grade == "A":
            st.success(f"ممتاز! تقديرك {grade} (المعدل: {average:.2f})")
        elif grade in ["B", "C"]:
            st.info(f"تقديرك {grade} (المعدل: {average:.2f})")
        elif grade == "D":
            st.warning(f"تقديرك {grade} (المعدل: {average:.2f})")
        else:
            st.error(f"تقديرك {grade} (المعدل: {average:.2f})")
