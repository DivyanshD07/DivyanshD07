from jinja2 import Template
t = Template("Hello {{ something }}!")
print(t.render(something="world"))

t = Template("My favourite numbers: {%for n in range(1,10) %}{{n}} " "{% endfor %}")
print(t.render())
