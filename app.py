import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

st.set_page_config(page_title="StyleMetrics", page_icon="🖤", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #FDF6F0; } .stSelectbox div[data-baseweb="select"] { background-color: white !important; } .stSelectbox div[data-baseweb="select"] * { color: #1a1a1a !important; } [data-baseweb="popover"] { background-color: white !important; } [data-baseweb="popover"] * { color: #1a1a1a !important; } [data-baseweb="menu"] { background-color: white !important; } [data-baseweb="menu"] * { color: #1a1a1a !important; }
    .block-container { padding: 2rem 3rem; }
    h1, h2, h3, h4, p, label, div { color: #1a1a1a !important; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #2D1B33 0%, #1a1a2e 100%); }
    [data-testid="stSidebar"] * { color: white !important; }
    .stMetric { background: white; border-radius: 12px; padding: 1rem; border-left: 4px solid #D4A5A5; box-shadow: 0 2px 8px rgba(0,0,0,0.08); }
    .stMetric label { color: #333333 !important; font-weight: bold; }
    .stMetric [data-testid="stMetricValue"] { color: #1a1a1a !important; font-size: 1.8rem !important; }
    .insight-box { background: linear-gradient(135deg, #F8E8E8, #F0E6FF); border-radius: 12px; padding: 1.5rem; border-left: 4px solid #C084C8; margin-top: 1rem; }
    .insight-box * { color: #1a1a1a !important; }
    .stSelectbox label { color: #1a1a1a !important; font-weight: 600; }
</style>
""", unsafe_allow_html=True)

BASE = os.path.expanduser('~/Documents/StyleMetrics/data/')

@st.cache_data
def load_data():
    trends = pd.read_csv(BASE + 'trends.csv')
    competitors = pd.read_csv(BASE + 'competitors.csv')
    sentiment = pd.read_csv(BASE + 'sentiment.csv')
    return trends, competitors, sentiment

trends, competitors, sentiment = load_data()

COLORS = ['#D4A5A5','#A8C5DA','#C3B8D8','#A8D5B5','#F2C4A0','#E8A0BF','#B5D4E8','#D4C5A9']
DARK = '#2D1B33'
ROSE = '#D4A5A5'
PURPLE = '#C084C8'
SAGE = '#A8D5B5'

CHART_LAYOUT = dict(
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(family='Georgia', color='#1a1a1a', size=12),
    title_font=dict(size=15, color='#1a1a1a'),
    xaxis=dict(tickfont=dict(color='#1a1a1a', size=11), title_font=dict(color='#1a1a1a'), gridcolor='#F0EBE8'),
    yaxis=dict(tickfont=dict(color='#1a1a1a', size=11), title_font=dict(color='#1a1a1a'), gridcolor='#F0EBE8'),
    legend=dict(font=dict(color='#1a1a1a'))
)

st.markdown("<h1 style='text-align:center; font-size:2.8rem; letter-spacing:12px; color:#2D1B33 !important;'>STYLEMETRICS</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#333333 !important; letter-spacing:6px; font-size:12px;'>FASHION BRAND INTELLIGENCE DASHBOARD</p>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#C084C8 !important; font-size:13px; font-style:italic;'>Fashion Brand Launch Intelligence Platform</p>", unsafe_allow_html=True)
st.markdown("<hr style='border:none; height:2px; background:linear-gradient(90deg, transparent, #D4A5A5, #C084C8, transparent);'>", unsafe_allow_html=True)

page = st.sidebar.radio("NAVIGATE", ["Market Trends","Competitor Intelligence","Sentiment Analysis","Launch KPI Tracker"])
st.sidebar.markdown("---")
st.sidebar.markdown("<p style='font-size:11px; color:white !important;'>STYLEMETRICS v1.0<br>Built for Emerging Fashion Labels<br>by Chaitali Wayakule</p>", unsafe_allow_html=True)

if page == "Market Trends":
    st.markdown("<h2 style='color:#2D1B33 !important; letter-spacing:4px;'>MARKET TREND RADAR</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#333333 !important; font-style:italic;'>Rising fashion aesthetics across EU markets</p>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        country = st.selectbox("Select Market", trends['country'].unique())
        filtered = trends[trends['country'] == country].sort_values('interest', ascending=True)
        fig = px.bar(filtered, x='interest', y='keyword', orientation='h', color='keyword', color_discrete_sequence=COLORS, title=f"Search Interest — {country}")
        fig.update_layout(**CHART_LAYOUT, height=420, showlegend=False)
        fig.update_xaxes(range=[0,100], title_text="Interest Score (0-100)")
        fig.update_yaxes(title_text="")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        rising = trends[trends['trend']=='rising'].groupby('keyword').size().reset_index(name='markets').sort_values('markets', ascending=False)
        fig2 = px.bar(rising, x='markets', y='keyword', orientation='h', color='keyword', color_discrete_sequence=COLORS, title="Keywords Rising Across Most Markets")
        fig2.update_layout(**CHART_LAYOUT, height=420, showlegend=False)
        fig2.update_xaxes(title_text="Number of Markets")
        fig2.update_yaxes(title_text="")
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""<div class='insight-box'>
    <p style='color:#1a1a1a !important;'><b>KEY INSIGHT</b><br><br>
    Quiet luxury and minimalist fashion are rising across all 5 EU markets. Sustainable womenswear is strongest in Netherlands and Germany. 
    Asian fashion Europe is an underserved niche with rising interest — a clear positioning opportunity for Jean De Grey.</p>
    </div>""", unsafe_allow_html=True)

elif page == "Competitor Intelligence":
    st.markdown("<h2 style='color:#2D1B33 !important; letter-spacing:4px;'>COMPETITOR INTELLIGENCE</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#333333 !important; font-style:italic;'>How comparable emerging fashion brands are performing</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Engagement Rate", f"{competitors['engagement_rate'].mean():.1f}%")
    col2.metric("Avg Followers", f"{int(competitors['followers'].mean()):,}")
    col3.metric("Top Content Format", competitors['top_content'].mode()[0])

    col1, col2 = st.columns(2)
    with col1:
        fig = px.bar(
            competitors.sort_values('engagement_rate', ascending=True),
            x='engagement_rate', y='brand', orientation='h',
            color='top_content',
            color_discrete_sequence=[DARK, ROSE, PURPLE, SAGE],
            title="Engagement Rate by Brand",
            text='engagement_rate'
        )
        fig.update_traces(texttemplate='%{text}%', textposition='outside', textfont=dict(color='#1a1a1a', size=11))
        fig.update_layout(**CHART_LAYOUT, height=420, showlegend=True)
        fig.update_xaxes(title_text="Engagement Rate %", range=[0, 4])
        fig.update_yaxes(title_text="")
        fig.update_traces(textposition='top center', textfont=dict(size=9, color='#1a1a1a'))
        fig.update_layout(**CHART_LAYOUT, height=420)
        fig.update_xaxes(title_text="Followers")
        fig.update_yaxes(title_text="Engagement Rate %")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        content_counts = competitors['top_content'].value_counts().reset_index()
        content_counts.columns = ['format','count']
        fig2 = px.pie(content_counts, values='count', names='format', title="Content Format Distribution", color_discrete_sequence=[DARK, ROSE, PURPLE, SAGE], hole=0.4)
        fig2.update_layout(font=dict(family='Georgia', color='#1a1a1a', size=12), title_font=dict(size=15, color='#1a1a1a'), legend=dict(font=dict(color='#1a1a1a')), height=420)
        fig2.update_traces(textfont=dict(color='white'))
        st.plotly_chart(fig2, use_container_width=True)

    st.dataframe(competitors[['brand','style','followers','engagement_rate','posts_per_week','top_content']].sort_values('engagement_rate', ascending=False).reset_index(drop=True), use_container_width=True)

    st.markdown("""<div class='insight-box'>
    <p style='color:#1a1a1a !important;'><b>KEY INSIGHT</b><br><br>
    Smaller brands under 300K followers consistently outperform larger ones on engagement. Reels is the dominant top-performing format. 
    Asian-influenced brands like Rejina Pyo achieve 2.2% engagement — above industry average. Jean De Grey should target 2.0%+ from launch.</p>
    </div>""", unsafe_allow_html=True)

elif page == "Sentiment Analysis":
    st.markdown("<h2 style='color:#2D1B33 !important; letter-spacing:4px;'>CUSTOMER SENTIMENT ANALYSIS</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#333333 !important; font-style:italic;'>What 22,641 real fashion customers actually say they want</p>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    col1.metric("Reviews Analysed", "22,641")
    col2.metric("Overall Positive", "92.8%")
    col3.metric("Top Department", "Bottoms 93.7%")

    col1, col2 = st.columns(2)
    with col1:
        positive_by_dept = sentiment[sentiment['sentiment']=='positive'].groupby('Department Name').size().reset_index(name='count')
        fig = px.bar(positive_by_dept, x='Department Name', y='count', color='Department Name', color_discrete_sequence=COLORS, title="Positive Reviews by Department")
        fig.update_layout(**CHART_LAYOUT, height=400, showlegend=False)
        fig.update_xaxes(title_text="Department")
        fig.update_yaxes(title_text="Number of Positive Reviews")
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        sent_counts = sentiment['sentiment'].value_counts().reset_index()
        sent_counts.columns = ['sentiment','count']
        fig2 = px.pie(sent_counts, values='count', names='sentiment', title="Overall Sentiment Breakdown", color_discrete_sequence=[SAGE, ROSE, '#F2C4A0'], hole=0.4)
        fig2.update_layout(font=dict(family='Georgia', color='#1a1a1a', size=12), title_font=dict(size=15, color='#1a1a1a'), legend=dict(font=dict(color='#1a1a1a')), height=400)
        fig2.update_traces(textfont=dict(color='#1a1a1a'))
        st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""<div class='insight-box'>
    <p style='color:#1a1a1a !important;'><b>KEY INSIGHT</b><br><br>
    92.8% positive sentiment across all departments. Tops and Dresses drive the most volume. 
    For Jean De Grey, launching with a strong womenswear Tops and Dresses focus aligns with what customers love most.</p>
    </div>""", unsafe_allow_html=True)

elif page == "Launch KPI Tracker":
    st.markdown("<h2 style='color:#2D1B33 !important; letter-spacing:4px;'>LAUNCH KPI TRACKER</h2>", unsafe_allow_html=True)
    st.markdown("<p style='color:#333333 !important; font-style:italic;'>Track your brand performance from day one</p>", unsafe_allow_html=True)

    st.markdown("<h3 style='color:#2D1B33 !important;'>SET YOUR LAUNCH TARGETS</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    target_followers = col1.number_input("Follower Target (3 months)", value=5000, step=500)
    target_engagement = col2.number_input("Engagement Rate Target %", value=2.0, step=0.1)
    target_posts = col3.number_input("Posts Per Week Target", value=4, step=1)
    target_reach = col4.number_input("Avg Reach Per Post Target", value=1000, step=100)

    st.markdown("<h3 style='color:#2D1B33 !important;'>CURRENT PERFORMANCE</h3>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    current_followers = col1.number_input("Current Followers", value=0, step=100)
    current_engagement = col2.number_input("Current Engagement %", value=0.0, step=0.1)
    current_posts = col3.number_input("Posts This Week", value=0, step=1)
    current_reach = col4.number_input("Avg Reach Per Post", value=0, step=100)

    st.markdown("<h3 style='color:#2D1B33 !important;'>PROGRESS TO TARGETS</h3>", unsafe_allow_html=True)
    cols = st.columns(4)
    metrics = [("Followers", current_followers, target_followers), ("Engagement %", current_engagement, target_engagement), ("Posts/Week", current_posts, target_posts), ("Reach/Post", current_reach, target_reach)]
    for i, (label, current, target) in enumerate(metrics):
        pct = min((current / target * 100) if target > 0 else 0, 100)
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=pct,
            title={'text': label, 'font': {'size': 13, 'family': 'Georgia', 'color': '#1a1a1a'}},
            number={'suffix': "%", 'font': {'size': 20, 'color': '#1a1a1a'}},
            gauge={'axis': {'range': [0,100], 'tickcolor': '#1a1a1a'}, 'bar': {'color': PURPLE},
                   'steps': [{'range': [0,50], 'color': '#F8E8E8'}, {'range': [50,80], 'color': '#F0D8F0'}, {'range': [80,100], 'color': '#E0C8E8'}]}
        ))
        fig.update_layout(height=220, margin=dict(t=40,b=10,l=20,r=20), paper_bgcolor='white', font=dict(color='#1a1a1a'))
        cols[i].plotly_chart(fig, use_container_width=True)

    benchmarks = pd.DataFrame({
        "Metric": ["Engagement Rate","Posts Per Week","Reels Share","Story Views"],
        "Emerging Brand Average": ["2.0-2.4%","3-5 posts","60% of content","10-15% of followers"],
        "Top Performer": ["3.0%+","6-7 posts","80% of content","20%+ of followers"],
        "Your Brand Target": ["2.0%+","4 posts","70% of content","15% of followers"],
    })
    st.dataframe(benchmarks, use_container_width=True, hide_index=True)

    st.markdown("""<div class='insight-box'>
    <p style='color:#1a1a1a !important;'><b>KEY INSIGHT</b><br><br>
    Focus on engagement rate over follower count in the first 3 months. 
    A small highly engaged audience of 2,000 followers at 3% engagement is more valuable than 10,000 followers at 0.5%.</p>
    </div>""", unsafe_allow_html=True)

st.markdown("""
<style>
[data-baseweb="select"] * { color: white !important; background-color: #333 !important; }
[data-baseweb="popover"] * { color: #1a1a1a !important; background-color: white !important; }
[data-baseweb="menu"] li { color: #1a1a1a !important; background-color: white !important; }
</style>
""", unsafe_allow_html=True)
