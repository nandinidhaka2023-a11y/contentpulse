import streamlit as st
import pymupdf

st.set_page_config(page_title="ContentPulse", page_icon="📱", layout="wide")

st.title("📱 ContentPulse")
st.subheader("Social Media Content Analyzer")
st.write("Upload your social media content and discover ways to improve engagement.")

st.divider()

uploaded_file = st.file_uploader(
    "📂 Upload your social media content",
    type=["pdf", "png", "jpg", "jpeg"]
)

if uploaded_file:

    try:
        text = ""

        with st.spinner("🔍 Analyzing your content..."):

            if uploaded_file.type == "application/pdf":

                doc = pymupdf.open(
                    stream=uploaded_file.read(),
                    filetype="pdf"
                )

                for page in doc:
                    text += page.get_text()

                doc.close()

            else:
                st.warning("⚠️ Image uploaded.")
                st.info("OCR is required for image text extraction.")

        if text.strip():

            st.success("✅ Content extracted successfully!")

            st.header("📝 Extracted Content")
            st.text_area("Your content:", text, height=250)

            words = text.split()
            word_count = len(words)

            sentences = [
                s.strip()
                for s in text.replace("!", ".").replace("?", ".").split(".")
                if s.strip()
            ]

            sentence_count = max(len(sentences), 1)
            avg_words = round(word_count / sentence_count, 1)

            questions = text.count("?")

            hashtags = sum(
                1 for word in words if word.startswith("#")
            )

            hooks = [
                "how", "why", "best", "tips", "secret",
                "new", "learn", "easy", "guide", "ways"
            ]

            lower = text.lower()

            hook_count = sum(
                1 for word in hooks if word in lower
            )

            st.header("📊 Content Insights")

            c1, c2, c3, c4 = st.columns(4)

            c1.metric("Word Count", word_count)
            c2.metric("Avg. Words / Sentence", avg_words)
            c3.metric("Questions", questions)
            c4.metric("Hashtags", hashtags)

            score = 50

            if word_count >= 20:
                score += 10

            if word_count <= 150:
                score += 10

            if questions > 0:
                score += 10

            if hook_count > 0:
                score += 10

            if hashtags > 0:
                score += 10

            score = min(score, 100)

            st.header("⚡ Engagement Potential")
            st.progress(score / 100)
            st.metric("ContentPulse Score", f"{score}/100")

            st.header("💡 Recommendations")

            if word_count > 150:
                st.warning("✂️ Consider shortening your content.")
            else:
                st.success("✅ Content length looks suitable.")

            if questions == 0:
                st.info("💬 Add a question to encourage interaction.")
            else:
                st.success("💬 Good! A question encourages interaction.")

            if hook_count == 0:
                st.info("🎯 Consider adding a stronger opening hook.")
            else:
                st.success("🎯 Hook language detected.")

            if hashtags == 0:
                st.info("🏷️ Consider adding relevant hashtags.")
            else:
                st.success("��️ Hashtags detected.")

        elif uploaded_file.type == "application/pdf":

            st.warning("⚠️ No selectable text found.")
            st.info("This PDF appears to be scanned. OCR is required.")

    except Exception as e:

        st.error("❌ Error processing the file.")
        st.code(str(e))
