Tecnologia a ser utilizada: Python
Orientações:
Usando Python, escreva o código de uma API com as seguintes rotas:
[POST] /vowel_count -- conta vogais em palavras
Requisição: {"words": ["batman", "robin", "coringa"]}
Resposta: {"batman": 2, "robin": 2, "coringa": 3}
[POST] /sort -- ordena palavras em um array, aceitando ordenação reversa
Requisição: {"words": ["batman", "robin", "coringa"], "order": "asc"}
Resposta: ["batman", "coringa", "robin"]
Requisição: {"words": ["batman", "robin", "coringa"], "order": "desc"}
Resposta: ["robin", "coringa", "batman"]
Caso as requisições estejam fora dos padrões especificados acima, retorne o código HTTP
apropriado (ex: método não é POST, rota inexistente, content type não é application/json)
Construa um pipeline no GitHub Actions ou GitLab que rode 3 etapas: lint, testes e deploy
utilizando uma ferramenta como Python Anywhere, Heroku, AWS ou outra de sua
preferência.
Documentação, mensagens de commit, qualidade de código, testes unitários...tudo conta na
avaliação, portanto capriche.
Quando terminar, envie por e-mail a URL da API e do repositório onde seu código estiver.
Entregar nos seguintes e-mails: para renato.almeida@soupilar.com.br e
teixeira.laary@gmail.com

Qualquer dúvida, enviar por email: renato.almeida@soupilar.com.br


## TODO's

- [x] Setup do projeto fastapi, com uma rota hello-world 
- [x] Setup ferramental para testes (pytest)
- [x] Criar teste para rota hello-world
- [ ] Validar requisição antes de processar. (Método HTTP, rota que não existe, content type deve ser application/json)
- [ ] Criar rota /vowel_count- 
- [ ] Criar rota /sort 
- [ ] Construir pipeline com lint, testes e deploy 
