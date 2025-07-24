# Sistema Avaliador e Sugeridor de Currículos

## 🚀 Visão Geral do Projeto

Este projeto nasceu da minha própria experiência e da dificuldade comum em alinhar um currículo eficazmente com as expectativas do mercado e as descrições das vagas. Muitas vezes, o que parece um bom currículo para um, pode não ser para outro, e a busca por vagas relevantes consome um tempo precioso.

Com o objetivo de simplificar e otimizar esse processo, desenvolvi um sistema web que não apenas lê o seu currículo em PDF, mas também o avalia de forma inteligente, oferece sugestões personalizadas de melhoria e ainda sugere vagas de emprego que realmente combinam com o seu perfil e objetivos. Tudo isso de forma **gratuito e sem a necessidade de cadastro ou login**, priorizando a acessibilidade e a privacidade do usuário.

---

## 🌟 Recursos Principais

* **Upload de Currículo em PDF:** Interface intuitiva para o envio de arquivos PDF.
* **Leitura e Extração de Conteúdo:** Utiliza Processamento de Linguagem Natural (PLN) para extrair informações relevantes do currículo (experiência, habilidades, educação, etc.).
* **Avaliação Inteligente:** Atribui uma nota de **0 a 10** ao currículo com base em critérios predefinidos, análise de palavras-chave, estrutura e relevância para o mercado de trabalho.
* **Sugestões Personalizadas de Melhoria:** Oferece dicas específicas e acionáveis para otimizar o currículo, aproveitando o poder de Modelos de Linguagem (LLMs) para gerar insights relevantes.
* **Busca e Sugestão de Vagas:** Compara o perfil do currículo com descrições de vagas para sugerir oportunidades alinhadas aos objetivos e competências do usuário.

---

## 🛠️ Tecnologias Utilizadas e Porquê

Este projeto é arquitetado em um modelo de **Frontend** e **Backend**, comunicando-se através de APIs. A escolha das tecnologias foi pensada para garantir **eficiência, escalabilidade (futura) e facilidade de desenvolvimento**, mesmo para um projeto complexo.

### Backend (API)

* **Python:** A escolha natural para o backend devido à sua vasta e robusta ecossistema de bibliotecas para **Processamento de Linguagem Natural (PLN)** e **Machine Learning (ML)**, que são o coração da inteligência do sistema. Sua sintaxe clara e legibilidade aceleram o desenvolvimento.
* **FastAPI:** Um framework web moderno e de alta performance para Python. Foi escolhido por sua velocidade, por oferecer validação de dados automática (com Pydantic) e por gerar documentação interativa (Swagger UI) de forma automática, o que facilita enormemente o desenvolvimento e o consumo da API pelo frontend.
* **`pdfplumber` / `PyPDF2`:** Bibliotecas essenciais para a tarefa inicial de extrair texto dos arquivos PDF dos currículos. `pdfplumber` é frequentemente preferido pela sua capacidade de lidar melhor com layouts complexos e tabelas.
* **`SpaCy` / `NLTK`:** Ferramentas fundamentais para PLN em Python. São utilizadas para tarefas como tokenização (dividir o texto em palavras), lematização (reduzir palavras à sua forma base) e, crucialmente, **Reconhecimento de Entidades Nomeadas (NER)** para identificar automaticamente informações como nomes, habilidades e instituições de ensino no currículo.
* **`Scikit-learn`:** A biblioteca padrão para Machine Learning em Python. É empregada para construir modelos de classificação, realizar análise de similaridade textual (comparando currículos com descrições de vagas) e auxiliar na lógica da pontuação do currículo.
* **`Transformers` (Hugging Face) / Google Gemini API:** Para funcionalidades avançadas, como a **geração de sugestões de melhoria**. A integração com modelos de linguagem de grande escala (LLMs) permite que o sistema crie texto coeso e personalizado, oferecendo dicas realmente úteis para o usuário. A **Google Gemini API** (via Google AI Studio) foi considerada pela sua capacidade e seu plano de uso gratuito para iniciantes.
* **SQLite:** Um sistema de gerenciamento de banco de dados leve, baseado em arquivo. Escolhido por sua simplicidade e por não exigir um servidor de banco de dados separado, o que o torna ideal para um projeto inicial, mantendo os custos de implantação baixos.

### Frontend (Interface do Usuário)

* **Vue.js:** Um framework JavaScript progressivo para a construção de interfaces de usuário (UI). Foi escolhido por sua **curva de aprendizado suave**, excelente documentação e flexibilidade, permitindo a criação de uma interface dinâmica, responsiva e agradável para o usuário. Sua reatividade facilita a exibição das análises do currículo em tempo real.
* **HTML5 / CSS3:** As linguagens padrão para estruturação e estilização de conteúdo web, garantindo que a aplicação seja acessível e visualmente atraente.
* **Axios:** Um cliente HTTP baseado em Promises para o navegador e Node.js. Utilizado para fazer as requisições assíncronas do frontend para a API do backend, enviando o currículo e recebendo os resultados.

---

## 🏗️ Roteiro de Desenvolvimento (Passo a Passo)

Este projeto foi construído modularmente, seguindo as seguintes etapas principais:

1.  **Módulo 1: Configuração do Ambiente e Leitura de PDF:**
    * Instalação e configuração de ferramentas essenciais (Python, VS Code).
    * Criação de um ambiente de desenvolvimento isolado.
    * Implementação inicial para extrair texto bruto de arquivos PDF.

2.  **Módulo 2: Backend Básico com FastAPI (API):**
    * Introdução ao framework FastAPI para criar endpoints (rotas) da API.
    * Configuração de uma rota para receber arquivos PDF via HTTP.
    * Integração da lógica de leitura de PDF dentro da API.

3.  **Módulo 3: Processamento de Linguagem Natural (PLN) para Currículos:**
    * Aplicação de técnicas de PLN para estruturar e normalizar o texto extraído.
    * Identificação e extração de informações-chave do currículo (experiência, educação, habilidades).

4.  **Módulo 4: Avaliação do Currículo e Geração de Nota:**
    * Definição de critérios para a avaliação do currículo (ex: densidade de palavras-chave, clareza, formatação implícita).
    * Desenvolvimento da lógica para calcular uma pontuação objetiva de 0 a 10.

5.  **Módulo 5: Geração de Sugestões de Melhoria:**
    * Integração com a API de um Modelo de Linguagem (LLM) para criar sugestões personalizadas.
    * Criação de "prompts" eficazes para guiar a LLM na geração de dicas úteis e relevantes para o currículo.

6.  **Módulo 6: Busca e Sugestão de Vagas:**
    * Desenvolvimento de um mecanismo para coletar (ou simular a coleta) e armazenar descrições de vagas.
    * Implementação de um algoritmo de similaridade para comparar o currículo do usuário com as vagas disponíveis e sugerir as mais relevantes.

7.  **Módulo 7: Frontend com Vue.js:**
    * Configuração do ambiente de desenvolvimento Vue.js.
    * Criação da interface de usuário, incluindo o formulário de upload e as áreas para exibir a nota, as sugestões e as vagas.
    * Implementação da comunicação assíncrona com o backend via requisições HTTP.

8.  **Módulo 8: Implantação (Deploy):**
    * Hospedagem do Backend (FastAPI) em uma plataforma de baixo ou nenhum custo (ex: Heroku, Fly.io, Vercel Functions).
    * Hospedagem do Frontend (Vue.js) em um serviço de hospedagem estática gratuito (ex: Netlify, Vercel, GitHub Pages).
    * Configuração final para garantir que o frontend e o backend se comuniquem corretamente na nuvem.

---

## 🤝 Como Contribuir

Este projeto é um esforço contínuo e contribuições são muito bem-vindas! Se você tiver ideias para melhorias, novas funcionalidades ou quiser corrigir algum bug, sinta-se à vontade para:

1.  Abrir uma [Issue](https://github.com/SEU_USUARIO/SEU_REPOSITORIO/issues) para discutir a mudança proposta.
2.  Fazer um [Fork](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) do repositório.
3.  Criar uma nova branch (`git checkout -b feature/minha-nova-feature`).
4.  Realizar suas alterações e fazer o commit (`git commit -m 'feat: minha nova feature'`).
5.  Fazer o push para a branch (`git push origin feature/minha-nova-feature`).
6.  Abrir um [Pull Request](https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/proposing-changes-with-pull-requests/creating-a-pull-request).

---

## 📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](https://opensource.org/license/mit) para mais detalhes.

---

## 📧 Contato

Se tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

* **Adriel Donegá** - adrieldonega@live.com - [Linkedin](https://www.linkedin.com/in/adrieldonega)
* **Me contrate:** (11) 961212420

---
