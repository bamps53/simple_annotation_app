import streamlit as st
from PIL import Image
import os
import glob

if "file_uploader_key" not in st.session_state:
    st.session_state["file_uploader_key"] = 0
# else:
    # st.session_state["file_uploader_key"] += 1

if "uploaded_files" not in st.session_state:
    st.session_state["uploaded_files"] = []

data_dir = 'public/projects'
is_new_project = st.sidebar.checkbox('New project')
if is_new_project:
    folder_name = st.sidebar.text_input('Folder name')
    if folder_name == '':
        st.stop()
    else:
        st.session_state["file_uploader_key"] += 1
        # st.experimental_rerun()
else:
    prev_folder_name = st.session_state.get('folder_name', '')
    folder_name = st.sidebar.selectbox('Folder name', sorted(os.listdir(data_dir)))
    st.write(prev_folder_name)
    st.write(folder_name)
    st.write(st.session_state.uploaded_files)
    if prev_folder_name and prev_folder_name != folder_name:
        st.session_state.folder_name = ""
        st.session_state["file_uploader_key"] += 1
        st.experimental_rerun()

st.session_state['folder_name'] = folder_name
save_dir = os.path.join(data_dir, folder_name)
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

uploaded_files = st.file_uploader("Choose a image file", type="jpg", accept_multiple_files=True, key=st.session_state["file_uploader_key"],)
if uploaded_files:
    st.session_state["uploaded_files"] = uploaded_files

num_images = len(glob.glob(os.path.join(save_dir, '*.jpg')))
st.write(st.session_state["file_uploader_key"])
st.write(num_images)
for i, uploaded_file in enumerate(uploaded_files):
    img = Image.open(uploaded_file)
    # 指定したフォルダに画像を保存
    index = i + num_images
    img_path = os.path.join(save_dir, f"image{index:04}.jpg")
    img.save(img_path, "JPEG")

num_images = len(glob.glob(os.path.join(save_dir, '*.jpg')))
st.write(num_images)
image_index = st.sidebar.number_input('Image index', min_value=0, max_value=num_images, value=0)
image_path = os.path.join(save_dir, f"image{image_index:04}.jpg")

st.write(image_path)
if os.path.exists(image_path):
    st.image(image_path, use_column_width=True)
else:
    st.write('No image')
