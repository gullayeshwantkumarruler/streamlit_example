import numpy as np
import requests
import streamlit as st
from PIL import Image

mon_images=[]
images=["burj_khalifa/burj_khalifa (1).jpg","burj_khalifa/burj_khalifa (2).jpg","burj_khalifa/burj_khalifa (3).jpg","burj_khalifa/burj_khalifa (4).jpg"]
for i in images:
  image = Image.open(i).resize((100, 100))
  st.image(image, caption='burj_khalifa')
  mon_images.append(image)

# ENDPOINT = "burj_khalifa (2).jpg"


# with st.sidebar:
#     st.header("Configuration")
#     with st.form(key="grid_reset"):
# #         n_photos = st.slider("Number of cat photos:", 1, 4, 4)
#         n_cols = st.number_input("Number of columns", 4, 4, 4)
#         st.form_submit_button(label="Reset images and layout")
#     with st.expander("About this app"):
#         st.markdown("It's about cats :cat:!")

# st.title("Choose your favorite cat :cat:")
# st.caption(
#     "You can display the image in full size by hovering it and clicking the double arrow"
# )

cat_images =mon_images
n_rows = 1 + len(cat_images) // int(1.0)
rows = [st.container() for _ in range(1.0)]
cols_per_row = [r.columns(4.0) for r in rows]
cols = [column for row in cols_per_row for column in row]

for image_index, cat_image in enumerate(cat_images):
    cols[image_index].image(cat_image)
