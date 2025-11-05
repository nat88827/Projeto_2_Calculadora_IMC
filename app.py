import streamlit as st


generos= {
    'MPB':{
        'Jorge Vercillo':'https://www.youtube.com/watch?v=PEMo-a8jbFw&list=RDPEMo-a8jbFw&start_radio=1',
        'Chico Buarque':'https://www.youtube.com/watch?v=wBfVsucRe1w&list=RDwBfVsucRe1w&start_radio=1'

    },
    'Pagode':{
        'Pericles':'https://www.youtube.com/watch?v=AENA_nvF-L0&list=RDAENA_nvF-L0&start_radio=1',
        'Alexandre Pires': 'https://www.youtube.com/watch?v=YuV7vUtV820&list=RDYuV7vUtV820&start_radio=1'
    },
    'Forró':{
        'Luiz Gonzaga': 'https://www.youtube.com/watch?v=zsFSHg2hxbc&list=RDzsFSHg2hxbc&start_radio=1',
        'Falamansa':'https://www.youtube.com/watch?v=QDAHMMMtFBI&list=RDQDAHMMMtFBI&start_radio=1'

    },
    'Samba':{
        'Alcione': 'https://www.youtube.com/watch?v=DwsKhZLj01M&list=RDDwsKhZLj01M&start_radio=1',
        'Cartola': 'https://www.youtube.com/watch?v=56mu8KSUYqk&list=RD56mu8KSUYqk&start_radio=1'
    }

}



#SIDEBAR

st.title('Sonicstar')
st.sidebar.image('sonic.png',width=200)

genero=st.sidebar.selectbox('Escolha um gênero musical: ', generos.keys())
artista=st.sidebar.selectbox("Os artistas desse gênero são: ",generos[genero].keys())

#PRINCIPAL
st.title(artista)
st.markdown('----')

video, sobre= st.tabs(['Vídeo', 'Sobre o artista'])
with video:
    st.video(generos[genero][artista])

with sobre:
    if artista== "Jorge Vercillo":
        st.markdown('''Jorge Vercillo nasceu em 11 de outubro de 1968, no Rio de Janeiro. Desde jovem demonstrou interesse pela música e começou sua carreira cantando em bares e festivais locais. Seu estilo mistura MPB, pop e elementos do samba, com letras poéticas e reflexivas.
Ganhou destaque nacional no final dos anos 1990 com músicas como “Final Feliz”, “Monalisa” e “Que Nem Maré”. Com o tempo, consolidou-se como um dos grandes nomes da música brasileira contemporânea, reconhecido pela sensibilidade e profundidade de suas composições.

        ''')

    elif artista== "Chico Buarque":
        st.markdown('''Francisco Buarque de Hollanda nasceu em 19 de junho de 1944, no Rio de Janeiro. É cantor, compositor, escritor e dramaturgo, e se tornou uma das figuras mais importantes da Música Popular Brasileira. Sua obra é marcada por letras poéticas, críticas sociais e políticas, especialmente durante o período da ditadura militar.
Entre suas canções mais famosas estão “Construção”, “Roda Viva”, “A Banda” e “Apesar de Você”. Além da música, Chico também é autor de livros e peças de teatro premiadas, como “Budapeste” e “Leite Derramado”. É considerado um dos maiores artistas da cultura brasileira.

        ''')

    elif artista== "Pericles":
        st.markdown('''Péricles Aparecido Fonseca de Faria nasceu em 22 de junho de 1969, em Santo André (SP). Ficou conhecido como vocalista do grupo Exaltasamba, onde alcançou enorme sucesso nos anos 1990 e 2000 com hits do pagode romântico.
Após sair do grupo em 2012, iniciou uma carreira solo bem-sucedida, com álbuns que misturam samba, pagode e romantismo. Sucessos como “Se Eu Largar o Freio” e “Cuidado Cupido” reforçaram sua popularidade. Péricles é conhecido por sua voz marcante e carisma, sendo um dos artistas mais respeitados do samba atual.

        ''')

    elif artista== "Alexandre Pires":
        st.markdown('''Alexandre Pires nasceu em 8 de janeiro de 1976, em Uberlândia (MG). Ele iniciou sua carreira como vocalista do grupo Só Pra Contrariar, que se tornou um dos maiores fenômenos da música brasileira nos anos 1990, com canções como “Domingo” e “Que Se Chama Amor”.
Em carreira solo, Alexandre conquistou sucesso internacional, gravando em português e espanhol. Entre seus maiores hits estão “Usted Se Me Llevó La Vida” e “Amor Verdadero”. Reconhecido pela versatilidade e talento, ele transitou com sucesso entre o pagode, o samba e a música romântica.

        ''')

    elif artista== "Luiz Gonzaga":
        st.markdown('''Luiz Gonzaga do Nascimento nasceu em 13 de dezembro de 1912, em Exu, Pernambuco, e faleceu em 2 de agosto de 1989. Conhecido como o “Rei do Baião”, foi o principal responsável por popularizar os ritmos nordestinos como baião, xote e forró em todo o Brasil.
Com sua sanfona e trajes típicos de vaqueiro, levou a cultura nordestina para os grandes centros urbanos. Entre seus clássicos estão “Asa Branca”, “A Vida do Viajante” e “Baião”. Sua obra influenciou gerações e tornou-se um símbolo da identidade nordestina e da música popular brasileira.

        ''')

    elif artista== "Falamansa":
        st.markdown('''A banda Falamansa foi formada em 1998 em São Paulo por Tato, Alemão, Dezinho e Valdir. Surgiu durante o movimento do forró universitário, que buscava reviver os ritmos nordestinos entre os jovens.
O grupo conquistou o público com letras alegres e positivas, misturando tradição e modernidade. Canções como “Xote dos Milagres”, “Rindo à Toa” e “Asas” se tornaram grandes sucessos. O Falamansa é reconhecido por manter viva a essência do forró de forma leve e contemporânea.

        ''')

    elif artista== "Alcione":
        st.markdown('''Alcione Dias Nazareth, conhecida como “Marrom”, nasceu em 21 de novembro de 1947, em São Luís do Maranhão. Desde jovem demonstrou talento para o canto e instrumentos de sopro. Mudou-se para o Rio de Janeiro, onde construiu uma sólida carreira na música popular e no samba.
Dona de uma voz poderosa e marcante, Alcione é autora de sucessos como “Não Deixe o Samba Morrer”, “Você Me Vira a Cabeça” e “Meu Ébano”. Com mais de 40 anos de carreira, é uma das intérpretes mais respeitadas do Brasil, reconhecida por sua força artística e carisma.

        ''')


    elif artista== "Cartola":
        st.markdown('''Angenor de Oliveira, conhecido como Cartola, nasceu em 11 de outubro de 1908, no Rio de Janeiro, e faleceu em 30 de novembro de 1980. Foi cantor, compositor e um dos fundadores da escola de samba Estação Primeira de Mangueira.
Com um estilo poético e sensível, escreveu alguns dos maiores clássicos do samba, como “As Rosas Não Falam”, “O Mundo é um Moinho” e “Alvorada”. Apesar de ter sido reconhecido tardiamente, tornou-se um ícone da música brasileira e uma referência eterna para o samba e a poesia popular.

        ''')

    
