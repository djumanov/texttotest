from ttq.parser import parse_text


with open('text.txt', encoding='utf-8') as f:
    input_text = f.read()


quiz = parse_text(input_text)
