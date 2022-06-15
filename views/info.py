import streamlit as st
import base64
from pptx import Presentation
from io import BytesIO
import streamlit.components.v1 as components


def load_view():

    st.title("Download center for the developers!")
    # with st.form(key="my_form"):

    col1, col2 = st.columns([1, 1])
    with col1:

        st.markdown("### Business case")

        # Opening file from file path
        with open("data/business_case.pdf", "rb") as f:
            base64_pdf = base64.b64encode(f.read()).decode("utf-8")

        # Embedding PDF in HTML
        pdf_display = f'<iframe style="width:100%;height:800px;" src="data:application/pdf;base64,{base64_pdf}" type="application/pdf">'

        # Displaying File
        st.markdown(pdf_display, unsafe_allow_html=True)

    with col2:
        from urllib.request import urlopen

        st.header("Download file's ")
        st.download_button(label="📝 Sprint 1", data=open("data/Sprint1.pptx", "rb"), file_name="data/Sprint1.pptx")
        st.download_button(label="📝 Sprint 2", data=open("data/Sprint2.pptx", "rb"), file_name="data/Sprint2.pptx")
        st.download_button(label="📝 Sprint 3", data=open("data/Sprint2.pptx", "rb"), file_name="data/Sprint2.pptx")
        st.download_button(label="📝 Sprint 4", data=open("data/Sprint4.pptx", "rb"), file_name="data/Sprint4.pptx")
        st.download_button(label="📝 Business case", data=open("data/business_case.pdf", "rb"), file_name="data/business_case.pdf")
        st.download_button(label="📝 Scrum process", data=open("data/scrum_pr.pdf", "rb"), file_name="data/scrum_pr.pdf")
        st.markdown(
            f'<div class="row-widget stDownloadButton"> \
                    <a href="https://github.com/FaridullahKhorshid/ProjectBigData/archive/refs/heads/master.zip"> \
                     <button kind="primary" class="css-1cpxqw2">🗂 Github Zip</button> \
                    </a> \
                </div>',
            unsafe_allow_html=True,
        )
        # st.download_button(
        #     label="Github master zip",
        #     data=urlopen("https://github.com/FaridullahKhorshid/ProjectBigData/archive/refs/heads/master.zip").read(),
        #     file_name="top_team.zip",
        # )
