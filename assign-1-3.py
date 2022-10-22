import os
from tkinter import image_names
import pandas as pd
import plotly.express as px

if not os.path.exists('./images'):
    os.mkdir('./images')

import_data = pd.read_csv(r'gapminder.csv')
csv_dataframe = pd.DataFrame(import_data)
marker = []
for i in range(len(csv_dataframe)):
    match (csv_dataframe.iloc[i]['continent']):
        case 'Asia':
            marker.append(1)
        case 'Europe':
            marker.append(2)
        case 'Africa':
            marker.append(3)
        case 'Americas':
            marker.append(4)
        case 'Oceania':
            marker.append(5)
csv_dataframe['Markers'] = marker
print(csv_dataframe.min())


#
# Part 1.1 - Encode Year by x-position, Life Expectancy by y-position
#
fig_year_life = px.scatter(csv_dataframe, 'year', 'lifeExp', labels={'year': 'Year', 'lifeExp': 'Life Expectancy (years)'}, height=700, width=1200)
fig_year_life.update_layout(
    title={
        'text': 'Evolution of Life Expectancy over Time', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
fig_year_life.update_xaxes(type='linear', nticks=20, tick0=1957, dtick=5)
fig_year_life.show()
fig_year_life.write_image("./images/YearVLifeExp.svg")

#
# Part 1.2 - Encode Year by x-position, Life Expectancy by y-position, Continent by color
#
fig_year_life_cont_color = px.scatter(csv_dataframe, 'year', 'lifeExp', labels={'year': 'Year', 'lifeExp': 'Life Expectancy (years)'}, color='continent', height=700, width=1200)
fig_year_life_cont_color.update_layout(
    title={
        'text': 'Evolution of Life Expectancy over Time by Continent', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
fig_year_life_cont_color.update_xaxes(type='linear', nticks=20, tick0=1957, dtick=5)
fig_year_life_cont_color.show()
fig_year_life_cont_color.write_image('./images/YearVLifeExpVContColor.svg')

#
# Part 1.3 - Encode Year by x-position, Life Expectancy by y-position, Continent by symbol
#
fig_year_life_cont_symbol = px.scatter(csv_dataframe, 'year', 'lifeExp', labels={'year': 'Year', 'lifeExp': 'Life Expectancy (years)'}, symbol='continent', height=900, width=1200)
fig_year_life_cont_symbol.update_layout(
    title={
        'text': 'Evolution of Life Expectancy over Time by Continent', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
fig_year_life_cont_symbol.update_traces(marker=dict(size=9, line=dict(width=0.7, color='silver')))
fig_year_life_cont_symbol.update_xaxes(type='linear', nticks=20, tick0=1957, dtick=5)
fig_year_life_cont_symbol.show()
fig_year_life_cont_symbol.write_image('./images/YearVLifeExpVContSymbol.svg')

#
# Part 1.4 - Encode Year by x-position, Life Expectancy by y-position, Continent by size
#
fig_year_life_cont_size = px.scatter(csv_dataframe, 'year', 'lifeExp', labels={'year': 'Year', 'lifeExp': 'Life Expectancy (years)'}, size='Markers', height=900, width=1200)
fig_year_life_cont_size.update_layout(
    title={
        'text': 'Evolution of Life Expectancy over Time by Continent', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
fig_year_life_cont_size.update_xaxes(type='linear', nticks=20, tick0=1957, dtick=5)
fig_year_life_cont_size.show()
fig_year_life_cont_size.write_image('./images/YearVLifeExpVContSize.svg')

#
# Part 2.1 - Encode GDP by x-position, Life Expectancy by y-position
#
fig_year_gdp = px.scatter(csv_dataframe, 'gdpPercap', 'lifeExp', labels={'gdpPercap': 'GDP per Capita', 'lifeExp': 'Life Expectancy (years)'}, height=800, width=1200)
fig_year_gdp.update_layout(
    title={
        'text': 'Change in Life Expectancy with GDP', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
fig_year_gdp.show()
fig_year_gdp.write_image('./images/gdpVLifeExp.svg')

#
# Part 2.1 - Encode GDP by x-position, Life Expectancy by y-position, Population by color
# ##
csv_dataframe_sorted = csv_dataframe.sort_values('pop')
fig_year_gdp_pop_color = px.scatter(csv_dataframe_sorted, 'gdpPercap', 'lifeExp', labels={'gdpPercap': 'GDP per Capita', 'lifeExp': 'Life Expectancy (years)'}, color='pop', height=800, width=1200)
fig_year_gdp_pop_color.update_layout(
    title={
        'text': 'Change in Life Expectancy with GDP by Population', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
fig_year_gdp_pop_color.show()
fig_year_gdp_pop_color.write_image('./images/gdpVLifeExpVPopColor.svg')

#
# Part 2.1 - Encode GDP by x-position, Life Expectancy by y-position, Population by size
# #
fig_year_gdp_pop_size = px.scatter(csv_dataframe, 'gdpPercap', 'lifeExp', labels={'gdpPercap': 'GDP per Capita', 'lifeExp': 'Life Expectancy (years)'}, size='pop', height=800, width=1200)
fig_year_gdp_pop_size.update_layout(
    title={
        'text': 'Change in Life Expectancy with GDP by Population', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
fig_year_gdp_pop_size.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
fig_year_gdp_pop_size.show()
fig_year_gdp_pop_size.write_image('./images/gdpVLifeExpVPopSize.svg')

#
# Part 2.1 - Encode GDP by x-position, Life Expectancy by y-position, Population by brightness
#
fig_year_gdp_pop_brightness = px.scatter(csv_dataframe_sorted, 'gdpPercap', 'lifeExp', labels={'gdpPercap': 'GDP per Capita', 'lifeExp': 'Life Expectancy (years)'}, color='pop', color_continuous_scale='gray', height=800, width=1200)
fig_year_gdp_pop_brightness.update_layout(
    title={
        'text': 'Change in Life Expectancy with GDP by Population', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
fig_year_gdp_pop_brightness.update_traces(marker=dict(line=dict(width=1, color='DarkSlateGrey')))
fig_year_gdp_pop_brightness.show()
fig_year_gdp_pop_brightness.write_image('./images/gdpVLifeExpVPopBrightness.svg')

#
# Part 3.1 - Visualise all 6 attributes on one chart
#
csv_dataframe_sorted_gdp = csv_dataframe.sort_values('gdpPercap')

relative_gdp = []
for i in range(len(csv_dataframe_sorted_gdp)):
    relative_gdp.append((csv_dataframe_sorted_gdp.iloc[i]['gdpPercap']/113523.132900)*800)
csv_dataframe_sorted_gdp['relative_gdp'] = relative_gdp

fig_everything = px.scatter(csv_dataframe_sorted_gdp, 'year', 'lifeExp', labels={'year': 'Year', 'lifeExp': 'Life Expectancy (years)'}, color='gdpPercap', symbol='continent', size='pop', height=800, width=1200)
fig_everything.update_layout(
    title={
        'text': 'Evolution of Life Expectancy over time by Continent, Country, Population and GDP', 
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    }
)
# fig_everything.update_traces(marker=dict(line=dict(width=csv_dataframe_sorted_gdp['relative_gdp'], color='DarkSlateGrey')))
fig_everything.update_layout(showlegend=False)
fig_everything.show()
fig_everything.write_image('./images/everything.svg')


