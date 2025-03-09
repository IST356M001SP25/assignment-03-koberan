'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import packaging
from io import StringIO
import json

st.title("Process Package Data Files")

file_test = st.file_uploader("Upload package file:")

if file_test:
    filename = file_test.name
    json_filename = filename.replace(".txt",".json")
    packages = []
    text = StringIO(file_test.getvalue().decode("utf-8")).read()
    for line in text.split("\n"):
        line = line.strip()
        pkg_data = packaging.parse_packaging(line)
        total = packaging.calc_total_units(pkg_data)
        unit = packaging.get_unit(pkg_data)
        packages.append(pkg_data)
        st.info(f"{line} ➡️ Total 📦 Size: {total} {unit}")
    count = len(packages)
    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)
    st.success(f"{count} packages written to {json_filename}", icon="💾")