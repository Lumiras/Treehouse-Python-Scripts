import mistune

text = "This *is* a text ##block in **Python**. I'm trying #stuff in this to *see* if **it** wo*rk*s"

print(mistune.markdown(text))
