import streamlit as st
st.title("Calculation")


num1=st.number_input("enter the number 1",step=1)
num2=st.number_input("enter number 2", step=1)

sum=num1+num2
if st.button("ADD"):
    st.write("sum is:",sum)


sub=num1-num2
if st.button("SUB"):
    st.write("sum is:",sub)

multi=num1*num2
if st.button("Multi"):
    st.write("multi is:",multi)



