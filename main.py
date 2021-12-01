###### FUNÇÃO 1 ######

def standardize_names(character_name):
    stripped_name = character_name.strip()

    return '-'.join(stripped_name.split(' '))

print(standardize_names('     Super Man'))


###### FUNÇÃO 2 ######

def standardize_title(title):
    return title.title()

print(standardize_title("cinco quartos de laranja"))


###### FUNÇÃO 3 ######

def standardize_text(text):
    line_text = ' '.join(text.split())
    splitted_text = line_text.split('. ')
    text_capitalized = []
    for sentence in splitted_text:
        # if i == 0:
        #     sent = splitted_text[i][1:]
        #     text_capitalized.append(sent.capitalize())
        # else:
        text_capitalized.append(sentence.capitalize())

    return '. '.join(text_capitalized)

example_text = """
a famosa atriz Constance Rattigan recebe uma encomenda
desagradável: uma lista com números de telefone de
pessoas que morreram recentemente. é uma coisa assustadora,
considerando que os nomes das poucas pessoas vivas presentes
na lista estão assinalados em vermelho com uma cruz. O da
própria Constance é um deles.
"""

print(standardize_text(example_text))


###### FUNÇÃO 4 ######

def title_creator(text):
    return text.title().center(len(text) + 40, '-')

print(title_creator("pense num deserto"))


###### FUNÇÃO 5 ######

def text_merge(text_a, text_b):
    text_a_standardized = standardize_text(text_a)
    text_b_standardized = standardize_text(text_b)

    text_a_dot_removed = text_a_standardized[:-1]
    text_b_lowered = text_b_standardized[0].lower() + text_b_standardized[1:]

    output = text_a_dot_removed + ' ' + text_b_lowered

    return(output)



text_of_blog_a = """
na Londres do pós-guerra, a escritora     Juliet tenta encontrar
uma   trama para seu novo livro. ela recebe ajuda por meio de uma
   carta de um      desconhecido, um nativo da ilha de Guernsey,
em cujas mãos havia chegado um livro    que há tempos tinha
pertencido    a Juliet.
"""

text_of_blog_b = """
O romance "Cinco Quartos de Laranja" é como   um vinho intenso e
delicado.    usando metáforas culinárias, personagens peculiares
 e acontecimentos sobrenaturais,      Harris cria uma história
complexa e      bela ao mesmo tempo.
"""

print(text_merge(text_of_blog_a, text_of_blog_b))
