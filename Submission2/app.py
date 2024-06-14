import streamlit as st
import joblib
import pandas as pd
import os

# Memuat model dan scaler
model = joblib.load('random_forest_model.joblib')
scaler = joblib.load('scaler.joblib')

def preprocess_input(input_data):
    # Encoding variabel kategorikal
    categorical_cols = input_data.select_dtypes(include=['object']).columns
    input_data = pd.get_dummies(input_data, columns=categorical_cols, drop_first=True)
    
    # Normalisasi fitur numerik
    numeric_cols = input_data.select_dtypes(include=['float64', 'int64']).columns
    input_data[numeric_cols] = scaler.transform(input_data[numeric_cols])
    
    return input_data


def preprocess_input(input_data):
    # Encoding variabel kategorikal
    categorical_cols = input_data.select_dtypes(include=['object']).columns
    input_data = pd.get_dummies(input_data, columns=categorical_cols, drop_first=True)
    
    # Normalisasi fitur numerik
    numeric_cols = input_data.select_dtypes(include=['float64', 'int64']).columns
    input_data[numeric_cols] = scaler.transform(input_data[numeric_cols])
    
    return input_data

# Judul aplikasi
st.title("Student Dropout Prediction")
st.write("Silahkan isi data pada bagian sidebar, kemudian setelah semua data terisi maka anda bisa menekan tombol 'Predict' untuk memprediksi mahasiswa/i akan mengalami Dropout atau tidak.")
st.write("Anda juga dapat mengarahkan kursor pada icon tanda tanya untuk mengetahui detail data yang diminta.")

# Pilihan dan deskripsi untuk Marital Status
marital_status_options = {
    1: "Single",
    2: "Married",
    3: "Widower",
    4: "Divorced",
    5: "Facto Union",
    6: "Legally Separated"
}

# Pilihan dan deskripsi untuk Application Mode
application_mode_options = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)"
}

# Pilihan dan deskripsi untuk Course
course_options = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)"
}

# Pilihan dan deskripsi untuk Previous Qualification
previous_qualification_options = {
    1: "Secondary education",
    2: "Higher education - bachelor's degree",
    3: "Higher education - degree",
    4: "Higher education - master's",
    5: "Higher education - doctorate",
    6: "Frequency of higher education",
    9: "12th year of schooling - not completed",
    10: "11th year of schooling - not completed",
    12: "Other - 11th year of schooling",
    14: "10th year of schooling",
    15: "10th year of schooling - not completed",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    42: "Professional higher technical course",
    43: "Higher education - master (2nd cycle)"
}

# Pilihan dan deskripsi untuk Nacionality
nacionality_options = {
    1: "Portuguese",
    2: "German", 
    6: "Spanish",
    11: "Italian",
    13: "Dutch",
    14: "English",
    17: "Lithuanian",
    21: "Angolan",
    22: "Cape Verdean",
    24: "Guinean",
    25: "Mozambican",
    26: "Santomean",
    32: "Turkish",
    41: "Brazilian",
    62: "Romanian",
    100: "Moldova (Republic of)",
    101: "Mexican",
    103: "Ukrainian",
    105: "Russian",
    108: "Cuban",
    109: "Colombian"
}

# Pilihan dan deskripsi untuk Mother's Qualification
qualification_options = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    22: "Technical-professional course",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}

# Pilihan dan deskripsi untuk Occupation
occupation_options = {
    0: "Student",
    1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities",
    3: "Intermediate Level Technicians and Professions",
    4: "Administrative staff",
    5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry",
    7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers",
    9: "Unskilled Workers",
    10: "Armed Forces Professions",
    90: "Other Situation",
    99: "(blank)",
    101: "Armed Forces Officers",
    102: "Armed Forces Sergeants",
    103: "Other Armed Forces personnel",
    112: "Directors of administrative and commercial services",
    114: "Hotel, catering, trade and other services directors",
    121: "Specialists in the physical sciences, mathematics, engineering and related techniques",
    122: "Health professionals",
    123: "Teachers",
    124: "Specialists in finance, accounting, administrative organization, public and commercial relations",
    125: "Specialists in information and communication technologies (ICT)",
    131: "Intermediate level science and engineering technicians and professions",
    132: "Technicians and professionals, of intermediate level of health",
    134: "Intermediate level technicians from legal, social, sports, cultural and similar services",
    135: "Information and communication technology technicians",
    141: "Office workers, secretaries in general and data processing operators",
    143: "Data, accounting, statistical, financial services and registry-related operators",
    144: "Other administrative support staff",
    151: "Personal service workers",
    152: "Sellers",
    153: "Personal care workers and the like",
    154: "Protection and security services personnel",
    161: "Market-oriented farmers and skilled agricultural and animal production workers",
    163: "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence",
    171: "Skilled construction workers and the like, except electricians",
    172: "Skilled workers in metallurgy, metalworking and similar",
    173: "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like",
    174: "Skilled workers in electricity and electronics",
    175: "Workers in food processing, woodworking, clothing and other industries and crafts",
    181: "Fixed plant and machine operators",
    182: "Assembly workers",
    183: "Vehicle drivers and mobile equipment operators",
    191: "Cleaning workers",
    192: "Unskilled workers in agriculture, animal production, fisheries and forestry",
    193: "Unskilled workers in extractive industry, construction, manufacturing and transport",
    194: "Meal preparation assistants",
    195: "Street vendors (except food) and street service providers"
}

# Pilihan dan deskripsi untuk jawaban antara ya dan tidak
answered_options = {
    1: "Yes",
    0: "No"
}

# Input pengguna dengan keterangan yang lebih informatif
marital_status = st.sidebar.selectbox('Marital Status', 
                                      list(marital_status_options.keys()), 
                                      format_func=lambda x: marital_status_options[x], 
                                      help="Status pernikahan mahasiswa.")

application_mode = st.sidebar.selectbox('Application Mode', 
                                        list(application_mode_options.keys()), 
                                        format_func=lambda x: application_mode_options[x], 
                                        help="Metode aplikasi yang digunakan oleh mahasiswa.")

application_order = st.sidebar.number_input('Application Order', 
                                            value=1, 
                                            help="Urutan aplikasi mahasiswa (antara 0 - pilihan pertama; dan 9 - pilihan terakhir).")

course = st.sidebar.selectbox('Course', 
                              list(course_options.keys()), 
                              format_func=lambda x: course_options[x], 
                              help="Program studi yang diambil oleh mahasiswa.")

daytime_evening_attendance = st.sidebar.selectbox('Daytime/Evening Attendance', 
                                                  [1, 0], 
                                                  format_func=lambda x: f"{'Daytime' if x == 1 else 'Evening'}", 
                                                  help="Kehadiran siang atau malam.")

previous_qualification = st.sidebar.selectbox('Previous Qualification', 
                                              list(previous_qualification_options.keys()), 
                                              format_func=lambda x: previous_qualification_options[x], 
                                              help="Kualifikasi mahasiswa sebelumnya.")

previous_qualification_grade = st.sidebar.number_input('Previous Qualification Grade', 
                                                       value=100.0, 
                                                       help="Nilai kualifikasi sebelumnya.")

nacionality = st.sidebar.selectbox('Nacionality', 
                                   list(nacionality_options.keys()), 
                                   format_func=lambda x: nacionality_options[x], 
                                   help="Kewarganegaraan mahasiswa.")

mothers_qualification = st.sidebar.selectbox('Mother\'s Qualification', 
                                             list(qualification_options.keys()), 
                                             format_func=lambda x: qualification_options[x], 
                                             help="Kualifikasi pendidikan ibu mahasiswa.")

fathers_qualification = st.sidebar.selectbox('Father\'s Qualification', 
                                             list(qualification_options.keys()), 
                                             format_func=lambda x: qualification_options[x], 
                                             help="Kualifikasi pendidikan ayah mahasiswa.")

mothers_occupation = st.sidebar.selectbox('Mother\'s Occupation', 
                                          list(occupation_options.keys()), 
                                          format_func=lambda x: occupation_options[x], 
                                          help="Pekerjaan ibu mahasiswa.")

fathers_occupation = st.sidebar.selectbox('Father\'s Occupation', 
                                          list(occupation_options.keys()), 
                                          format_func=lambda x: occupation_options[x], 
                                          help="Pekerjaan ayah mahasiswa.")

admission_grade = st.sidebar.number_input('Admission Grade', 
                                           value=100.0, 
                                           help="Nilai masuk mahasiswa (antara 0 hingga 200).")

displaced = st.sidebar.selectbox('Displaced', 
                                 list(answered_options.keys()), 
                                 format_func=lambda x: answered_options[x], 
                                 help="Apakah mahasiswa adalah orang yang dipindahkan?")

educational_special_needs = st.sidebar.selectbox('Education Special Needs', 
                                                 list(answered_options.keys()), 
                                                 format_func=lambda x: answered_options[x], 
                                                 help="Apakah mahasiswa memiliki kebutuhan pendidikan khusus?")

debtor = st.sidebar.selectbox('Debtor',
                              list(answered_options.keys()), 
                              format_func=lambda x: answered_options[x], 
                              help="Apakah mahasiswa adalah debitur?")

tuition_fees_up_to_date = st.sidebar.selectbox('Tuition Fees Up-to-Date',
                                               list(answered_options.keys()), 
                                               format_func=lambda x: answered_options[x],  
                                               help="Apakah biaya kuliah mahasiswa sudah diperbarui.")

gender = st.sidebar.selectbox('Gender', [1, 0], format_func=lambda x: f"{'Male' if x == 1 else 'Female'}", help="Jenis kelamin mahasiswa.")

scholarship_holder = st.sidebar.selectbox('Scholarship Holder', 
                                          list(answered_options.keys()), 
                                          format_func=lambda x: answered_options[x],  
                                          help="Apakah mahasiswa adalah penerima beasiswa.")

age_at_enrollment = st.sidebar.number_input('Age at Enrollment', value=18, help="Usia mahasiswa saat pendaftaran.")

international = st.sidebar.selectbox('International', 
                                     list(answered_options.keys()), 
                                     format_func=lambda x: answered_options[x],   
                                     help="Apakah mahasiswa adalah mahasiswa internasional.")

curricular_units_1st_sem_credited = st.sidebar.number_input('Curricular Units 1st Sem (credited)', value=0, help="Jumlah unit kurikuler yang dikreditkan oleh mahasiswa di semester pertama.")

curricular_units_1st_sem_enrolled = st.sidebar.number_input('Curricular Units 1st Sem (enrolled)', value=0, help="Jumlah unit kurikuler yang didaftarkan oleh mahasiswa di semester pertama.")

curricular_units_1st_sem_evaluations = st.sidebar.number_input('Curricular Units 1st Sem (evaluations)', value=0, help="Jumlah unit kurikuler yang dievaluasi oleh mahasiswa di semester pertama.")

curricular_units_1st_sem_approved = st.sidebar.number_input('Curricular Units 1st Sem (approved)', value=0, help="Jumlah unit kurikuler yang disetujui oleh mahasiswa di semester pertama.")

curricular_units_1st_sem_grade = st.sidebar.number_input('Curricular Units 1st Sem (grade)', value=0.0, help="Nilai satuan kurikuler 1st semester.")

curricular_units_1st_sem_without_evaluations = st.sidebar.number_input('Curricular Units 1st Sem (without evaluations)', value=0, help="Satuan kurikuler 1st semester tanpa evaluasi.")

curricular_units_2nd_sem_credited = st.sidebar.number_input('Curricular Units 2nd Sem (credited)', value=0, help="Jumlah unit kurikuler 2nd semester diakui.")

curricular_units_2nd_sem_enrolled = st.sidebar.number_input('Curricular Units 2nd Sem (enrolled)', value=0, help="Jumlah unit kurikuler 2nd semester terdaftar.")

curricular_units_2nd_sem_evaluations = st.sidebar.number_input('Curricular Units 2nd Sem (evaluations)', value=0, help="Jumlah unit kurikuler 2nd semester dievaluasi.")

curricular_units_2nd_sem_approved = st.sidebar.number_input('Curricular Units 2nd Sem (approved)', value=0, help="Jumlah unit kurikuler 2nd semester disetujui.")

curricular_units_2nd_sem_grade = st.sidebar.number_input('Curricular Units 2nd Sem (grade)', value=0.0, help="Nilai satuan kurikuler 2nd semester.")

curricular_units_2nd_sem_without_evaluations = st.sidebar.number_input('Curricular Units 2nd Sem (without evaluations)', value=0, help="Satuan kurikuler 2nd semester tanpa evaluasi.")

unemployment_rate = st.sidebar.number_input('Unemployment Rate', value=0.0, help="Tingkat pengangguran.")

inflation_rate = st.sidebar.number_input('Inflation Rate', value=0.0, help="Tingkat inflasi.")

gdp = st.sidebar.number_input('GDP', value=0.0, help="Produk domestik bruto.")

# Membuat DataFrame dari input pengguna
input_data = pd.DataFrame({
    'Marital_status': [marital_status],
    'Application_mode': [application_mode],
    'Application_order': [application_order],
    'Course': [course],
    'Daytime_evening_attendance': [daytime_evening_attendance],
    'Previous_qualification': [previous_qualification],
    'Previous_qualification_grade': [previous_qualification_grade],
    'Nacionality': [nacionality],
    'Mothers_qualification': [mothers_qualification],
    'Fathers_qualification': [fathers_qualification],
    'Mothers_occupation': [mothers_occupation],
    'Fathers_occupation': [fathers_occupation],
    'Admission_grade': [admission_grade],
    'Displaced': [displaced],
    'Educational_special_needs': [educational_special_needs],
    'Debtor': [debtor],
    'Tuition_fees_up_to_date': [tuition_fees_up_to_date],
    'Gender': [gender],
    'Scholarship_holder': [scholarship_holder],
    'Age_at_enrollment': [age_at_enrollment],
    'International': [international],
    'Curricular_units_1st_sem_credited': [curricular_units_1st_sem_credited],
    'Curricular_units_1st_sem_enrolled': [curricular_units_1st_sem_enrolled],
    'Curricular_units_1st_sem_evaluations': [curricular_units_1st_sem_evaluations],
    'Curricular_units_1st_sem_approved': [curricular_units_1st_sem_approved],
    'Curricular_units_1st_sem_grade': [curricular_units_1st_sem_grade],
    'Curricular_units_1st_sem_without_evaluations': [curricular_units_1st_sem_without_evaluations],
    'Curricular_units_2nd_sem_credited': [curricular_units_2nd_sem_credited],
    'Curricular_units_2nd_sem_enrolled': [curricular_units_2nd_sem_enrolled],
    'Curricular_units_2nd_sem_evaluations': [curricular_units_2nd_sem_evaluations],
    'Curricular_units_2nd_sem_approved': [curricular_units_2nd_sem_approved],
    'Curricular_units_2nd_sem_grade': [curricular_units_2nd_sem_grade],
    'Curricular_units_2nd_sem_without_evaluations': [curricular_units_2nd_sem_without_evaluations],
    'Unemployment_rate': [unemployment_rate],
    'Inflation_rate': [inflation_rate],
    'GDP': [gdp]
})

# Preprocessing input
input_data_preprocessed = preprocess_input(input_data)

# Melakukan prediksi
if st.button('Predict'):
    prediction = model.predict(input_data_preprocessed)
    prediction_label = {0: 'Graduate', 1: 'Dropout', 2: 'Enrolled'}
    st.write(f'Prediction: {prediction_label[prediction[0]]}')