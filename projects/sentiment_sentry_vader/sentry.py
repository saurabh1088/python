from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def analyze_mood():
    analyzer = SentimentIntensityAnalyzer()
    
    print("--- 🤖 Sentiment Sentry Active ---")
    print("Type 'exit' to quit.")
    
    while True:
        text = input("\nEnter text to analyze: ")
        
        if text.lower() == 'exit':
            break
            
        # Get the scores
        scores = analyzer.polarity_scores(text)
        compound = scores['compound']
        
        # Logic Layer: Interpret the 'compound' score
        if compound >= 0.05:
            mood = "🌟 Positive"
        elif compound <= -0.05:
            mood = "💢 Negative"
        else:
            mood = "😐 Neutral"
            
        print(f"Analysis: {mood} (Score: {compound})")

if __name__ == "__main__":
    analyze_mood()
