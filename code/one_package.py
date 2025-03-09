'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
import packaging

st.title("Process Package Data")

pkg_data = st.text_input("Enter package data:")
if pkg_data:
    parsed_data = packaging.parse_packaging(pkg_data)
    
    total_size = packaging.calc_total_units(parsed_data)
    unit_type = packaging.get_unit(parsed_data)

    st.text(parsed_data)
    for item in parsed_data:
        name, size = next(iter(item.items()))
        st.info(f"**{name}** ➡️ {size}")

    st.success(f"**Total Package Size:** {total_size} {unit_type}")