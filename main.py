from string import Template

t = Template('$name is the $job of $company')
s = t.substitute(name='steve', job="ceo", company='apple')
print(s)
