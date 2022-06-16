import streamlit as st
import base64


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

        st.header("Download file's ")

        st.markdown(
            f'<a href="https://github.com/FaridullahKhorshid/ProjectBigData/archive/refs/heads/master.zip"> \
                <button kind="primary" class="custom_button">🗂 Github Zip</button> \
            </a>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<a href="https://github.com/FaridullahKhorshid/ProjectBigData/blob/master/data/business_case.pdf?raw=true"> \
                <button kind="primary" class="custom_button">💼 Business case</button> \
            </a>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<a href="https://github.com/FaridullahKhorshid/ProjectBigData/blob/master/data/scrum_pr.pdf?raw=true"> \
                <button kind="primary" class="custom_button">📊 Scrum process</button> \
            </a>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<a href="https://github.com/FaridullahKhorshid/ProjectBigData/blob/master/data/Sprint1.pptx?raw=true"> \
                <button kind="primary" class="custom_button">📝 Sprint 1</button> \
            </a>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<a href="https://github.com/FaridullahKhorshid/ProjectBigData/blob/master/data/Sprint2.pptx?raw=true"> \
                <button kind="primary" class="custom_button">📝 Sprint 2</button> \
            </a>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<a href="https://github.com/FaridullahKhorshid/ProjectBigData/blob/master/data/Sprint4.pptx?raw=true"> \
                <button kind="primary" class="custom_button">📝 Sprint 4</button> \
            </a>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<a href="https://github.com/FaridullahKhorshid/ProjectBigData/blob/master/data/final_sprint.pptx?raw=true"> \
                <button kind="primary" class="custom_button">📝 Final Sprint</button> \
            </a>',
            unsafe_allow_html=True,
        )
