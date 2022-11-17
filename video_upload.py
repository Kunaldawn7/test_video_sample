import os
import sys
import streamlit as st
import cv2
import tempfile
import time



st.title('Video Upload and display')



output_video_file = f'output_recorded.mp4'

if os.path.exists(output_video_file):
    os.remove(output_video_file)


# with st.form('Upload', clear_on_submit=True):
up_file = st.file_uploader("Upload a Video", ['mp4','mov', 'avi'])
    # uploaded = st.form_submit_button("Upload")

stframe = st.empty()

ip_vid_str = '<p style="font-family:Helvetica; font-weight: bold; font-size: 16px;">Input Video</p>'
warning_str = '<p style="font-family:Helvetica; font-weight: bold; color: Red; font-size: 17px;">Please Upload a Video first!!!</p>'

warn = st.empty()


download_button = st.empty()

if up_file:
    
    download_button.empty()
    tfile = tempfile.NamedTemporaryFile(delete=False)

    warn.empty()
    tfile.write(up_file.read())

    vf = cv2.VideoCapture(tfile.name)

    
    # txt = st.sidebar.markdown(ip_vid_str, unsafe_allow_html=True)   
    # ip_video = st.sidebar.video(tfile.name) 

    while vf.isOpened():
        ret, frame = vf.read()
        if not ret:
            break

        # convert frame from BGR to RGB before processing it.
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # out_frame, _ = upload_process_frame.process(frame, pose)
        stframe.image(frame)
        # video_output.write(out_frame[...,::-1])
        time.sleep(0.5)

    
    vf.release()
    # video_output.release()
    stframe.empty()
    # ip_video.empty()
    # txt.empty()
    tfile.close()
    
    









    
    

    


