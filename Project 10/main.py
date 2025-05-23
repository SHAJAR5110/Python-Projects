import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="📀 Data sweeper", layout="wide")

st.title("📀 Data sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

uploaded_files= st.file_uploader("Upload your CSV or Excel file", type=['csv', 'xlsx'], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        file_ext = os.path.splitext(file.name)[1].lower()
        
        if file_ext == ".csv":
            df = pd.read_csv(file)
        elif file_ext == ".xlsx":
            df = pd.read_excel(file)
        else:
            st.error(f"Invalid file format {file_ext}. Please upload a CSV or Excel file.")
            continue
        # Display info about the uploaded file
        st.write(f"File Name: {file.name}")
        st.write(f"File Sizw: {file.size/1024}")
        
        #show 5 rows of the df
        st.write("Preview of the Head of the DataFrame")
        st.dataframe(df.head())
        
        #option for data cleaning
        st.subheader("Data Cleaning Options")     
        if st.checkbox(f"Clean Data for {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove Duplicates {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed..!")
            with col2:
                if st.button(f"Fill Missing Values {file.name}"):
                    numeric_cols = df.select_dtypes(include=['number']).columns
                    df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
                    st.write("Missing Values have been filled..!")
        #choose specific columns to keep or convert
        st.subheader("Select Columns to Convert")
        columns = st.multiselect("Choose columns for {file.name}", df.columns,default=df.columns)
        df = df[columns]
        
        #create some visualizations
        st.subheader("Data Visualizations")
        if st.checkbox(f"Show visualizations for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])
        
        #Cover the file ==> CSV to Excel    
        st.subheader("Conversion Options")
        convertion_type = st.radio(f"Convert {file.name} to: ",["CSV","Excel"], key=file.name)
        if st.button(f"Convert {file.name}"):
            buffer = BytesIO()
            if convertion_type == "CSV":
                df.to_csv(buffer, index=False)
                file_name = file.name.replace(file_ext, ".csv")
                mine_type = "text/csv"
            elif convertion_type == "Excel":
                df.to_excel(buffer, index=False)
                file_name = file.name.replace(file_ext, ".xlsx")
                mine_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                buffer.seek(0)
                
                #Download the file
            st.download_button(
                label=f"Download {file.name} as {convertion_type}",
                data=buffer,
                file_name=file_name,
                mime=mine_type)
            st.success(f"{file.name} has been converted to {convertion_type} successfully..!'🎉✨")
            