Sentinela V1 - Multitool real
https://github.com/ogredzin/sentinela.git

O que e
Sentinela V1 e uma suite open source de 3 ferramentas sem censura e sem simulacoes. Compile, clone ou edite a vontade - o codigo e seu.

Funcionalidades
1. IP Logger
Gera um .bat que captura: IP publico, nome do PC, usuario, SO, data/hora e envia tudo para Discord Webhook. Use seu proprio webhook - e so colar a URL.

2. DDoS Real
- 300 tarefas concorrentes (asyncio + aiohttp)
- Requisicoes GET ou POST escolhidas aleatoriamente
- Loop infinito - pare apenas com Ctrl+C
- Funciona em qualquer URL com http/https

3. IP Bomb UDP
- Envia pacotes UDP sem delay, sem limite
- Protocolo puro - so precisa do IP e porta
- Travamento/reset e efeito real, nao simulacao

Instalacao completa (Windows, Linux, WSL)
1. Clone o repo
git clone https://github.com/ogredzin/sentinela.git
cd sentinela

2. Crie ambiente (opcional, mas recomendado)
python -m venv venv
source venv/bin/activate      # Linux
venv\Scripts\activate         # Windows

3. Instale dependencias
pip install --upgrade pip
pip install -r requirements.txt

4. Rode
python src/sentinela.py

Passo a passo rapido (Windows PowerShell)
git clone https://github.com/ogredzin/sentinela.git
cd sentinela
pip install -r requirements.txt
python src/sentinela.py

Arquivos do repo
sentinela/
├── LICENSE              # MIT - faca o que quiser
├── README.md            # Este arquivo
├── requirements.txt     # 3 bibliotecas pequenas
└── src/
    └── sentinela.py     # Codigo principal (~250 linhas)

Requisitos minimos
- Python 3.8+ (3.11 roda mais rapido)
- 5 MB de disco
- Conexao com internet para baixar dependencias

Dependencias
aiohttp>=3.9
colorama
requests

Comandos uteis
Atualizar pip:              python -m pip install --upgrade pip
Instalar tudo de novo:      pip install -r requirements.txt --force-reinstall
Ver versao do Python:       python --version

Execucao
python src/sentinela.py
Menu simples:
1 - IP Logger
2 - DDoS
3 - IP Bomb
4 - Sair

IP Logger
Digite a URL do webhook Discord quando solicitado. O arquivo Sentinela_IP_Logger.bat sera criado na mesma pasta. Envie para o alvo; quando ele executar, os dados aparecerao no seu canal.

DDoS
Digite a URL completa (ex: https://exemplo.com). A ferramaenta dispara 300 tarefas infinitas ate você parar com Ctrl+C.

IP Bomb
Digite o IP e a porta (padrao 8080). O programa envia pacotes UDP sem delay ate você parar com Ctrl+C.

Notas
- Nao ha limites codificados - cuidado com o proprio IP.
- Funciona em VPS, WSL, terminal Linux ou prompt Windows.
- Codigo completo em src/sentinela.py - edite quanto quiser.

 Licenca
MIT License - veja o arquivo LICENSE. Faca o que quiser: copiar, modificar, vender, distribuir. Nao tem garantia alguma.

Reportar problemas
Abra uma issue em https://github.com/ogredzin/sentinela/issues ou faca um fork e mande pull request.

Contato
Criador: Crastnet4
Repo oficial: https://github.com/ogredzin/sentinela.git
