import streamlit as st

def main():
    st.set_page_config(page_title="Chat With PDF", page_icon = ":books:")

    st.header("Chat with PDFs :books:")
    st.text_input("Ask a question")

    with st.sidebar:
        st.subheader("Your documents")
        st.file_uploader("Upload your documents here and click 'Process'")
        st.button("Process")

if __name__ == "__main__":
    main()