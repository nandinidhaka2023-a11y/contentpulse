# Approach

ContentPulse is a web-based Social Media Content Analyzer developed using Python and Streamlit. The goal is to help users evaluate their social media content and identify simple ways to improve its clarity and engagement potential.

The application provides a file-upload interface for PDF documents. For selectable-text PDFs, PyMuPDF is used to extract the document content. The extracted text is then processed using lightweight rule-based techniques. The system calculates key content metrics including total word count, average words per sentence, number of questions, hashtags, and the presence of potential hook words such as “how”, “why”, “tips”, and “secret”.

These metrics are combined into a transparent engagement-potential score ranging from 0 to 100. The application also generates actionable recommendations based on the detected characteristics, such as reducing lengthy content, adding questions, strengthening the opening hook, or including relevant hashtags.

To improve usability, the application includes a loading state while processing files and basic exception handling for unexpected errors. The project uses Git and GitHub for version control, with dependencies documented in `requirements.txt`, and is deployed using Streamlit Community Cloud.

The current version focuses on selectable-text PDF analysis. OCR for scanned documents and image-based content is planned as a future enhancement.