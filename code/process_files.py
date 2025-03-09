'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''

import streamlit as st
import packaging
from io import StringIO
import json

st.title("Process Package Data Files (Multiple)")

if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'total_lines' not in st.session_state:
    st.session_state.total_lines = 0
if 'total_files' not in st.session_state:
    st.session_state.total_files = 0

file_test2 = st.file_uploader("Upload first package file:")

if file_test2:
    filename = file_test2.name
    json_filename = filename.replace(".txt",".json")
    packages = []
    text = StringIO(file_test2.getvalue().decode("utf-8")).read()
    for line in text.split("\n"):
        line = line.strip()
        pkg_data = packaging.parse_packaging(line)
        total = packaging.calc_total_units(pkg_data)
        unit = packaging.get_unit(pkg_data)
        packages.append(pkg_data)
    count = len(packages)
    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)
    summary = f"{count} packages written to {json_filename}"

    st.session_state.summaries.append(summary)
    st.session_state.total_files += 1
    st.session_state.total_lines += count

    for s in st.session_state.summaries:
        st.info(s, icon="💾")
    st.success(f"{st.session_state.total_files} files processed, {st.session_state.total_lines} total lines procesed")