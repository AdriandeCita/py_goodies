# Uses Tinycss library
# Parses input file an saves it into output
# file in semi-minified syntax
# Saves comments in code
import tinycss

input_file = "style.css"
output_file = "out.css"

def rule_to_css(rule):
    str_out = ""
    for s in rule.selector:
        str_out += s.as_css()
    str_out += " {"
    for d in rule.declarations:
        str_out += str(d.name) + ": " + str(d.value.as_css()) + "; "
    return(str_out[:len(str_out)-1]+"}\n")

def stylesheet_to_css(stylesheet):
    str_out = ""
    for rule in stylesheet.rules:
        if rule.at_keyword:
            str_out += rule.at_keyword
            if rule.at_keyword == "@import":
                str_out += rule.uri
                str_out += ";\n"
            elif rule.at_keyword == "@media":
                for m in rule.media:
                    str_out += m
                str_out += " {"
                for r in rule.rules:
                    str_out += rule_to_css(r)
        else:
            str_out += rule_to_css(rule)
    return(str_out)

parser = tinycss.make_parser("page3")
stream_in = open(input_file, "r")
content = ""
rebuilt_stylesheet = ""

for line in stream_in:
    content += line
stream_in.close()

while True:
    index = -1
    index = content.find("/*")
    if index > -1:
        if index > 0:
            stylesheet = parser.parse_stylesheet(content[:index])
            rebuilt_stylesheet += stylesheet_to_css(stylesheet)
            content = content[index:]

        index = content.find("*/")
        if index > -1:
            rebuilt_stylesheet += content[:index+1]
            content = content[index+1:]
        else:
            rebuilt_stylesheet += content
            content = ""
    else:
        break
if len(content):
    stylesheet = parser.parse_stylesheet(content)
    rebuilt_stylesheet += stylesheet_to_css(stylesheet)

streamOut = open(output_file, "w+")
for l in rebuilt_stylesheet:
    streamOut.write(l)
streamOut.close()
