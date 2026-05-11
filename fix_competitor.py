import re

with open('app.py', 'r') as f:
    content = f.read()

old_chart = "        fig = px.scatter(competitors, x='followers', y='engagement_rate', text='brand', size='engagement_rate', color='top_content', color_discrete_sequence=[DARK, ROSE, PURPLE, SAGE], title=\"Followers vs Engagement Rate\")"

new_chart = """        fig = px.bar(
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
        fig.update_yaxes(title_text="")"""

content = content.replace(old_chart, new_chart)

with open('app.py', 'w') as f:
    f.write(content)
print("Done!")
