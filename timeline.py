import plotly.express as px
import pandas as pd

df = pd.DataFrame([
    dict(Title="<b>Prisoners of Geography</b><br>Tim Marshall", Start='2020-05-13', Finish='2020-06-28', Rating=9.5),
    dict(Title="<b>The Hockey Stick and the Climate Wars</b><br>Michael E. Mann", Start='2020-06-03', Finish='2020-07-31', Rating=9.5),
    dict(Title="<b>Factfulness</b><br>Hans Rosling", Start='2020-07-31', Finish='2020-09-12', Rating=8),
    dict(Title="<b>Brave new world revisited</b><br>Aldous Huxley", Start='2020-08-14', Finish='2020-09-03', Rating=3),
    dict(Title="<b>The Population Bomb</b><br>Paul R. Ehrlich", Start='2020-09-04', Finish='2020-09-21', Rating=2),
    dict(Title="<b>Foundation</b><br>Isaac Asimov", Start='2020-09-22', Finish='2020-10-01', Rating=10),
    dict(Title="<b>The Naked Sun</b><br>Isaac Asimov", Start='2020-12-22', Finish='2021-01-01', Rating=9),
    dict(Title="<b>The Uninhabitable Earth</b><br>David Wallace-Wells", Start='2021-01-03', Finish='2021-02-07', Rating=3.5),
    dict(Title="<b>The New Climate War</b><br>Michael E. Mann", Start='2021-02-08', Finish='2021-07-19', Rating=9.5),
    dict(Title="<b>Volcanoes: A Very Short Introduction</b><br>Michael J. Branney & Jan Zalasiewicz", Start='2021-07-20', Finish='2021-08-03', Rating=7.5),
    dict(Title="<b>The Strangest Man</b><br>James Dashner", Start='2021-08-04', Finish='2021-08-25', Rating=6.5),
    dict(Title="<b>Fahrenheit 451</b><br>Ray Bradbury", Start='2021-08-31', Finish='2021-09-28', Rating=8.5),
    dict(Title="<b>Organic Chemistry: A Very Short Introduction</b><br>Graham Patrick", Start='2021-12-10', Finish='2022-01-15', Rating=7.5),
    #dict(Title="<b>The Hundred Years' War on Palestine</b><br>Rashid Khalidi", Start='2022-12-10'),
    dict(Title="<b>Firmament</b><br>Simon Clark", Start='2022-01-29', Finish='2022-07-10', Rating=6.5),
    #dict(Title="<b>Guns, Germs and Steel</b><br>Jared Diamond", Start='2022-07-11'),
])

fig = px.timeline(df, x_start="Start", x_end="Finish", y="Title", color="Rating", range_color=(0,10), range_x=('2020-04-01', '2022-07-23'), color_continuous_scale=px.colors.sequential.Viridis, width=1920, height=1080)
fig.update_yaxes(autorange="reversed") # otherwise Titles are listed from the bottom up
#fig.add_annotation(align='center', x='2022-05-22', text='Exams', y=12, showarrow=False)
fig.update_layout(
    paper_bgcolor="#ffffff",
    plot_bgcolor="#EFFFFF",
    font_family="Arial",
    font_size=12,
    font_color="#000000",
    title_font_family="Times New Roman",
    title_font_size=30,
    title_x=0.5,
    title_xanchor='center',
    title_text="<b>Reading Timeline and Personal Ratings</b>",
    xaxis_showgrid=False,
    yaxis_title="<b>Book Title</b><br>Author",
    yaxis_title_font_size=18,
    xaxis_title="<b>Date</b>",
    xaxis_title_font_size=18,
    yaxis_title_font_family="Times New Roman",
    xaxis_title_font_family="Times New Roman",
    coloraxis_colorbar_title_text="<b>Rating/10</b>",
    coloraxis_colorbar_title_side="bottom",
    coloraxis_colorbar_title_font_family="Times New Roman",
    coloraxis_colorbar_title_font_size=18,
    coloraxis_colorbar_thickness=35,
    coloraxis_colorbar_len=0.95,
)
#fig.update_coloraxes(colorbar.tickangle=180)
fig.show()
