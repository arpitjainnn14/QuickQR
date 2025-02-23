import streamlit as st 
import segno as sg

st.title('QR Code generator')
st.subheader('Enter the link below for QR Generation')

link=st.text_input(label='URL Link',placeholder='enter the link here:')

submit_button=st.button('Submit')

if submit_button:
    qr_code=sg.make_qr(link)
    qr_code.save('qrcode.png',scale=5,border=10)

    st.image('qrcode.png',caption="Generated QR")
