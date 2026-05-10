import streamlit as st
import pandas as pd

st.set_page_config(page_title="OncoPath", layout="wide")

st.title("🧬 OncoPath")
st.subheader("AI-powered cancer protein pathway analysis")

uploaded_file = st.file_uploader(
    "Upload CSV file containing protein names",
    type=["csv"]
)

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.success("File uploaded successfully")

    st.write("### Uploaded Data")
    st.dataframe(df)

    if st.button("Analyze"):
        st.write("## Inferred Cancer Pathways")

mock_pathways = [
    "PI3K-AKT signaling pathway",
    "MAPK signaling pathway",
    "Cell Cycle pathway",
    "p53 signaling pathway"
]

for pathway in mock_pathways:
    st.markdown(f"### {pathway}")
st.write("## Related Research Papers")

papers = [
    {
        "title": "Cancer signaling pathways and targeted therapy",
        "link": "https://pubmed.ncbi.nlm.nih.gov/"
    },
    {
        "title": "Protein interaction networks in cancer",
        "link": "https://pubmed.ncbi.nlm.nih.gov/"
    }
]

for paper in papers:
    st.markdown(f"- [{paper['title']}]({paper['link']})")
else:
    st.info("Please upload a CSV file to begin analysis")
