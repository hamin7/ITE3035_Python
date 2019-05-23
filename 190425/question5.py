items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line,
                     # it does the characters that are after it in html_str
                     # are on the next line

for item in items:
    html_str = html_str + "<li>" + str(item) + "</li>" "\n"

html_str = html_str + "</ul>"

print(html_str)
