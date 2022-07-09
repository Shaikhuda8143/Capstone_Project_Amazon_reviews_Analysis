import streamlit as st
from textblob import TextBlob
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt
import plotly_express as px
from collections import Counter
import helper2
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def convert_to_df(sentiment):
	sentiment_dict = {'polarity':sentiment.polarity,'subjectivity':sentiment.subjectivity}
	sentiment_df = pd.DataFrame(sentiment_dict.items(),columns=['metric','value'])
	return sentiment_df
def analyze_token_sentiment(docx):
	analyzer = SentimentIntensityAnalyzer()
	pos_list = []
	neg_list = []
	neu_list = []
	for i in docx.split():
		res = analyzer.polarity_scores(i)['compound']
		if res > 0.1:
			pos_list.append(i)
			pos_list.append(res)

		elif res <= -0.1:
			neg_list.append(i)
			neg_list.append(res)
		else:
			neu_list.append(i)

	result = {'positives':pos_list,'negatives':neg_list,'neutral':neu_list}
	return result
mode=st.sidebar.radio('Choose',['Manual','Dataset','Reviews Analysis','About'])
if mode=='Manual':
		st.subheader("Manual")
		with st.form(key='nlpForm'):
			raw_text = st.text_area("Enter Text Here")
			submit_button = st.form_submit_button(label='Analyze')
# layout
		col1,col2 = st.columns(2)
		if submit_button:

			with col1:
				st.info("Results")
				sentiment = TextBlob(raw_text).sentiment
				st.write(sentiment)

				# Emoji
				if sentiment.polarity > 0:
					st.markdown("Sentiment:: Positive :smiley: ")
				elif sentiment.polarity < 0:
					st.markdown("Sentiment:: Negative :angry: ")
				else:
					st.markdown("Sentiment:: Neutral 😐 ")

				# Dataframe
				result_df = convert_to_df(sentiment)
				st.dataframe(result_df)

				# Visualization
				c = alt.Chart(result_df).mark_bar().encode(
					x='metric',
					y='value',
					color='metric')
				st.altair_chart(c,use_container_width=True)
				with col2:
					st.info("word Sentiment")

					token_sentiments = analyze_token_sentiment(raw_text)
					st.write(token_sentiments)

if mode == 'Dataset':
	st.subheader("Dataset")
	uploaded_file = st.sidebar.file_uploader("Choose a file")
	if uploaded_file is not None:
		df = pd.read_csv(uploaded_file)
		st.write(df)
		user_rating = df['Stars'].unique().tolist()

		user_rating.sort()
		# user_rating.insert(0, "overall")
		selected_review = st.sidebar.selectbox("Show Analysis wrt", user_rating)
		if st.sidebar.button("Show Analysis"):
			num_review, words = helper2.fetch_stats(selected_review, df)
			col1, col2 = st.columns(2)
			with col1:
				st.header("Total Reviews")
				st.title(num_review)
			with col2:
				st.header("Total words")
				st.title(words)
		most_common_df = helper2.most_common_words(selected_review, df)
		fig, ax = plt.subplots()
		ax.bar(most_common_df[0], most_common_df[1])
		plt.xticks(rotation='vertical')
		st.title('Most Common Words')
		st.pyplot(fig)
		st.dataframe(most_common_df)
		# Emoji Analysis
		emoji_df = helper2.emoji_helper(selected_review, df)
		st.title('Emoji Analysis')
		col1, col2 = st.columns(2)

		with col1:
			st.dataframe(emoji_df)
		with col2:
			fig,ax = plt.subplots()
			ax.pie(emoji_df[1].head(),labels=emoji_df[0].head(), autopct="%0.2f")
			st.pyplot(fig)



if mode == 'Reviews Analysis':
	st.subheader("Reviews Analysis")
	uploaded_file = st.sidebar.file_uploader("Choose a file")
	if uploaded_file is not None:
		df = pd.read_csv(uploaded_file)
		st.write(df)
		global numeric_columns
		global non_numeric_columns
		try:
			numeric_columns = list(df.select_dtypes(['int', 'float']).columns)
			non_numeric_columns = list(df.select_dtypes(['object']).columns)
			non_numeric_columns.append(None)
			print(non_numeric_columns)
		except Exception as e:
			print(e)
chart_select = st.sidebar.selectbox(label="Select the chart type",options=['Scatterplots', 'Lineplots', 'Histogram'])
if chart_select == 'Scatterplots':
	st.sidebar.subheader("Scatterplot Settings")
	try:
		x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
		y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
		plot = px.scatter(data_frame=df, x=x_values, y=y_values)
		# display the chart
		st.plotly_chart(plot)
	except Exception as e:
			print(e)
if chart_select == 'Lineplots':
	st.sidebar.subheader("Line Plot Settings")
	try:
		x_values = st.sidebar.selectbox('X axis', options=numeric_columns)
		y_values = st.sidebar.selectbox('Y axis', options=numeric_columns)
		plot = px.line(data_frame=df, x=x_values, y=y_values)
		st.plotly_chart(plot)
	except Exception as e:
		print(e)
if chart_select == 'Histogram':
	st.sidebar.subheader("Histogram Settings")
	try:
		x = st.sidebar.selectbox('Feature', options=numeric_columns)
		bin_size = st.sidebar.slider("Number of Bins", min_value=10,max_value=100, value=40)
		plot = px.histogram(x=x, data_frame=df)
		st.plotly_chart(plot)

	except Exception as e:
		print(e)

if mode == 'About':

	st.title("Group-4")
	st.header('Team Members')
	st.write("Farhat Imam")
	st.write("Shaik Huda")
	st.write("Siddhesh Ranjan Manjrekar")
	st.write("Rupesh M")
	st.write("prathyush B R")
	st.write("S K Mohammad Akhleem Nawaz")
	st.header('Mentor/Guided By')
	st.write("Rajasekhar")
	st.write("Bapuram Pallavi")



