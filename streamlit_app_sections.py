import streamlit as st

with st.echo('below'):
	from st_pages import Page, Section, add_page_title, show_pages

	'## Declaring the pages in your app:'

	show_pages(
		[
			Page('streamlit_app_sections.py', 'Home'),
			Section(name='Data Blog', icon=':bar_chart:'),
			Page('data_blog/points_against_blog.py', 'Points Against Analysis'),
			Section(name='2022 Power Rankings', icon=':trophy:'),
			Page('power_rankings/2022/week_one.py'),
			Section(name='2021 Power Rankings', icon=':trophy:'),
			Page('power_rankings/2021/week_one.py')
		]
	)

	add_page_title()
