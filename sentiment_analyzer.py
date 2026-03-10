import streamlit as st
from textblob import TextBlob

# Configure the page
st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="😊",
    layout="centered"
)

# App title and description
st.title(" Text Sentiment Analyzer")
st.write("Enter any text below and discover its sentiment!")

# Create a text area for user input
user_input = st.text_area(
    "Enter your text here:",
    placeholder="Type or paste your text here...",
    height=150
)

# Analyze button
if st.button("Analyze Sentiment", type="primary"):
    if user_input.strip():
        # Create TextBlob object and analyze sentiment
        blob = TextBlob(user_input)
        sentiment = blob.sentiment
        
        # Extract polarity and subjectivity
        polarity = sentiment.polarity
        subjectivity = sentiment.subjectivity
        
        # Determine sentiment category
        if polarity > 0.1:
            category = "Positive 😊"
            color = "green"
        elif polarity < -0.1:
            category = "Negative 😞"
            color = "red"
        else:
            category = "Neutral 😐"
            color = "gray"
        
        # Display results
        st.divider()
        st.subheader("Analysis Results")
        
        # Show sentiment category with colored badge
        st.markdown(f"**Sentiment:** :{color}[{category}]")
        
        # Show detailed scores
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                label="Polarity Score",
                value=f"{polarity:.2f}",
                help="Ranges from -1 (negative) to +1 (positive)"
            )
        with col2:
            st.metric(
                label="Subjectivity Score",
                value=f"{subjectivity:.2f}",
                help="Ranges from 0 (objective) to 1 (subjective)"
            )
        
        # Progress bars for visual representation
        st.write("**Visual Breakdown:**")
        
        # Polarity bar (convert -1 to 1 range to 0 to 100)
        polarity_percentage = (polarity + 1) / 2 * 100
        st.write("Polarity (0% = Very Negative, 50% = Neutral, 100% = Very Positive)")
        st.progress(int(polarity_percentage))
        
        # Subjectivity bar
        st.write("Subjectivity (0% = Pure Facts, 100% = Pure Opinion)")
        st.progress(int(subjectivity * 100))
        
    else:
        st.warning("⚠️ Please enter some text to analyze!")

# Footer with instructions
st.divider()
st.markdown("""
### 💡 How to Use:
1. **Enter text** in the box above (reviews, tweets, comments, etc.)
2. **Click "Analyze Sentiment"** to see the results
3. **Interpret the scores:**
   - **Polarity:** How positive or negative the text is
   - **Subjectivity:** How factual or opinion-based the text is
""")
