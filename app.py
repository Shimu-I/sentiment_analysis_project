import streamlit as st
import matplotlib.pyplot as plt
import sentiment

def plot_sentiment_graph(labels, scores):
    if len(labels) != len(scores):
        st.error("Mismatch between labels and scores lengths!")
        return
    if not all(isinstance(score, (int, float)) for score in scores):
        st.error("Scores must be numeric!")
        return
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(labels, scores, color='skyblue')
    ax.set_xlabel('Sentiment Labels')
    ax.set_ylabel('Scores')
    ax.set_title('Sentiment Scores')
    st.pyplot(fig)

st.markdown("""
<style>
.stTextInput>div>div>input {
    height: 150px;
    font-size: 20px;
}
.stButton>button {
    border-radius: 50%;
    width: 100px;
    height: 100px;
    font-size: 18px;
    margin: 0 auto;
    display: block;
}
.emoji-card {
    display: inline-block;
    width: 100px;
    height: 100px;
    border: 2px solid #ccc;
    border-radius: 10px;
    text-align: center;
    font-size: 40px;
    line-height: 50px;
    margin: 10px;
    transition: all 0.3s ease;
    position: relative;
}
.emoji-card .emoji-name {
    font-size: 14px;
    position: absolute;
    bottom: 10px;
    width: 100%;
    text-align: center;
}
.emoji-card.highlight {
    border-color: #ff4b4b;
    transform: translateY(-10px);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
.emoji-container {
    text-align: center;
}
.result-box {
    margin-top: 20px;
    padding: 20px;
    border: 2px solid #ccc;
    border-radius: 10px;
    text-align: center;
    background-color: #d4edda;
    margin-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

st.title("Sentiment Analysis")
st.markdown("""
<div>
<h2>Real Time Sentiment Analysis</h2>
</div>
""", unsafe_allow_html=True)

text = st.text_input("Enter your text here:", "")

emoji_mapping = {
    "positive": "😊",
    "neutral": "😐",
    "negative": "😠"
}
emoji_names = {
    "positive": "Happy",
    "neutral": "Neutral",
    "negative": "Angry"
}

st.markdown('<div class="emoji-container">', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f'<div class="emoji-card" id="positive" role="img" aria-label="Happy">😊<div class="emoji-name">Happy</div></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="emoji-card" id="neutral" role="img" aria-label="Neutral">😐<div class="emoji-name">Neutral</div></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="emoji-card" id="negative" role="img" aria-label="Angry">😠<div class="emoji-name">Angry</div></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

if st.button("Predict"):
    if not text.strip():
        st.warning("Please enter some text to analyze.")
    else:
        try:
            labels, scores, top_sentiment = sentiment.calculatesentiment(text)

            # Validate top_sentiment
            if top_sentiment not in emoji_mapping:
                st.error("Invalid sentiment detected!")
                top_sentiment = "neutral"  # Fallback to neutral for invalid cases
            emoji_result = emoji_mapping[top_sentiment]
            sentiment_name = emoji_names[top_sentiment]

            # Highlight the corresponding emoji card
            st.markdown(f"""
            <script>
            document.querySelectorAll('.emoji-card').forEach(card => {{
                card.classList.remove('highlight');
            }});
            document.getElementById('{top_sentiment}').classList.add('highlight');
            </script>
            """, unsafe_allow_html=True)

            # Display the result
            st.markdown(f"""
            <div class="result-box">
                <h3 style="color: black;">Sentiment Result:</h3>
                <div class="result-emoji" style="font-size: 100px; padding: 10px;">
                    {emoji_result}
                </div>
                <p style="color: black;"><strong>{sentiment_name}</strong></p>
            </div>
            """, unsafe_allow_html=True)

            # Plot the sentiment scores
            plot_sentiment_graph(labels, scores)

        except Exception as e:
            st.error(f"Error analyzing sentiment: {str(e)}")