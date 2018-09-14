import pygal

line_chart = pygal.Line()
line_chart.title = 'Programming Language Popularity For The Past 5 Years (in %)'
line_chart.x_labels = map(str, range(2013, 2019))
line_chart.add('Python', [10.1, 10.5, 11.9, 14.4, 19.4, 24.6])
line_chart.add('Java', [26.9, 26.6, 26.2, 24.7, 22.8, 22.1])
line_chart.add('PHP', [14.2, 12.8, 11.9, 10.8, 9, 7.8])
line_chart.add('C#', [10.2, 9.8, 9.5, 9.1, 8.1, 7.7])
line_chart.add('Javascript', [7.8, 7.8, 7.5, 7.8, 8.3, 8.5])
line_chart.render_to_file('pop_lang_linegraph.svg')