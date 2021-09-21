!pip install --user plotly
!pip install --user dash

import plotly.express as px

fig = px.bar(df, x='store', y='counts', color='items')
fig.show()
