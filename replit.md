# Conecta ZL: Notícias que nos unem

## Visão Geral
Portal de notícias da Zona Leste desenvolvido em Django + Python com sistema de autenticação, publicação de artigos, comentários moderados, curtidas, geolocalização e API REST. Redesenhado completamente com nova identidade visual roxa (#6E349D) e foco na comunidade local.

## Mudanças Recentes
- **17/11/2025**: Melhorias de UX e Identidade Visual
  - ✅ **Nova Logo**: Substituída pela logo oficial do Conecta ZL com responsividade otimizada em navbar e landing page
  - ✅ **Navbar Minimalista**: Removido texto "Conecta ZL" e "Notícias que nos unem", mantendo apenas a logo
  - ✅ **Navbar Centralizada**: Abas INICIO, DESTAQUES e NOTICIAS centralizadas com layout responsivo em 3 colunas
  - ✅ **Banner Full-Width**: Banner principal da landing page ocupa 100% da largura da tela (edge-to-edge)
  - ✅ **Footer Completo**: Adicionados links de redes sociais (X, YouTube, Instagram), Política de Privacidade, Termos de Uso e Anuncie Conosco
  - ✅ **Formulário Moderno de Postagem**: Redesign completo da página /article/create/ com layout similar ao X e LinkedIn
  - ✅ **Superusuário Admin**: Criado conta admin (username: admin, senha: admin123) para acesso ao painel administrativo
  - ✅ **Responsividade Mobile**: Todas as alterações otimizadas para dispositivos móveis e desktop
  - ✅ **Arquitetura Full-Width**: Implementado sistema de blocks fullwidth no base.html para conteúdo que quebra o container

- **04/11/2025**: Redesign Completo "Conecta ZL: Notícias que nos unem"
  - ✅ **Nova Identidade Visual**: Paleta roxa (#6E349D primary, #EFEDE3 secondary, #1E1E2A support)
  - ✅ **Novas Fontes**: Almarai Bold para títulos, Kameron para subtítulos
  - ✅ **Landing Page Redesenhada**: Hero banner roxo com "Conectando a Comunidade com Fatos e Notícias do Bairro!"
  - ✅ **Página de Destaques**: Layout moderno com destaque principal e seções de mais curtidas/comentadas
  - ✅ **Feed de Notícias**: Estilo Twitter com cards modernos e ações interativas
  - ✅ **Página de Perfil do Jornalista**: Layout de rede social com banner, avatar, estatísticas e grid de publicações
  - ✅ **Navbar Modernizada**: Logo circular roxo + "Conecta ZL" + tagline "Notícias que nos unem"
  - ✅ **Seção de Interação Comunitária**: "O que está acontecendo no seu bairro?" com botão Foto/Vídeo
  - ✅ **Bug Fix Crítico**: Guards de autenticação adicionados para acesso seguro a user.profile

- **04/11/2025**: Sistema de Administração Completo Implementado
  - ✅ Sistema de aprovação de artigos (apenas admins podem aprovar publicações)
  - ✅ Dashboard administrativo com estatísticas e gráficos em tempo real
  - ✅ Interface de aprovação/rejeição de artigos com notas de feedback
  - ✅ Gerenciamento de comentários pendentes
  - ✅ Gerenciamento de usuários e alteração de perfis
  - ✅ Redirecionamento inteligente após login (admins → dashboard, outros → home)
  - ✅ Controle duplo de visibilidade (published + approval_status)
  - ✅ Gráficos interativos com Chart.js
  
- **03/11/2025**: Projeto inicial criado com todas as funcionalidades principais implementadas
  - Sistema de autenticação com três perfis (leitor, jornalista, administrador)
  - CRUD completo de artigos com editor rico (django-summernote)
  - Sistema de comentários com moderação
  - Sistema de curtidas dinâmicas
  - Geolocalização com mapas (folium)
  - API REST completa com Django REST Framework
  - Interface responsiva com TailwindCSS

## Arquitetura do Projeto

### Estrutura de Apps
```
portal_noticias/          # Projeto principal Django
├── users/               # App de usuários e perfis
│   ├── models.py       # Profile com roles (leitor, jornalista, admin)
│   ├── views.py        # Login, logout, registro com redirecionamento inteligente
│   └── admin.py        # Admin panel customizado
├── articles/           # App de artigos/notícias
│   ├── models.py       # Article com sistema de aprovação, Like
│   ├── views.py        # CRUD de artigos, curtidas
│   ├── admin_views.py  # Dashboard e painel administrativo completo
│   └── admin.py        # Admin com Summernote
├── comments/           # App de comentários
│   ├── models.py       # Comment com moderação
│   ├── views.py        # Adicionar/deletar comentários
│   └── admin.py        # Moderação de comentários
└── api/                # App de API REST
    ├── serializers.py  # Serializers DRF
    ├── views.py        # ViewSets
    └── urls.py         # Rotas da API
```

### Tecnologias Utilizadas
- **Backend**: Django 4.2.7
- **API**: Django REST Framework
- **Editor Rico**: django-summernote
- **Tags**: django-taggit
- **Mapas**: folium
- **Imagens**: Pillow
- **Banco de Dados**: PostgreSQL (Neon)
- **Frontend**: HTML5, CSS3, JavaScript Vanilla
- **Fontes**: Google Fonts (Almarai Bold, Kameron)
- **Design**: Sistema de cores personalizado (Purple #6E349D, Off-white #EFEDE3)

## Funcionalidades Principais

### 1. Sistema de Autenticação
- Cadastro de usuários com escolha de perfil
- Login/Logout
- Três tipos de perfil:
  - **Leitor**: pode ler, comentar e curtir artigos
  - **Jornalista**: pode criar e gerenciar próprios artigos
  - **Administrador**: acesso total, moderação

### 2. Artigos
- CRUD completo (Criar, Ler, Atualizar, Deletar)
- Editor de texto rico com django-summernote
- Upload de imagens
- Sistema de tags
- Geolocalização (latitude, longitude, nome do local)
- Contador de visualizações
- Sistema de destaques para página inicial
- Slug automático gerado do título
- **NOVO**: Sistema de aprovação com 3 status (pendente, aprovado, rejeitado)
- **NOVO**: Controle duplo de visibilidade (published + approval_status)
- **NOVO**: Jornalistas criam artigos com status "pendente" automaticamente
- **NOVO**: Admins podem criar artigos já aprovados
- **NOVO**: Notas de aprovação/rejeição para feedback aos jornalistas

### 3. Comentários
- Sistema de comentários moderados
- Aprovação manual via admin
- Usuários podem deletar próprios comentários
- Administradores podem deletar qualquer comentário

### 4. Curtidas
- Sistema de curtidas/descurtidas dinâmico
- JavaScript Vanilla para interação sem reload
- Contador de curtidas por artigo
- Um usuário pode curtir apenas uma vez por artigo

### 5. Geolocalização
- Integração com folium para mapas interativos
- Marcação de localização em artigos
- Visualização de mapas na página de detalhe do artigo

### 6. API REST
- Endpoints para artigos e comentários
- Filtros de busca e ordenação
- Paginação automática (10 itens por página)
- Permissões: leitura pública, escrita autenticada
- Endpoints disponíveis:
  - `/api/articles/` - Listar/criar artigos
  - `/api/articles/{slug}/` - Detalhe de artigo
  - `/api/comments/` - Listar/criar comentários
  - `/api/comments/{id}/` - Detalhe de comentário

### 7. Interface
- Design responsivo com TailwindCSS
- Paginação na página inicial
- Sistema de mensagens (feedback visual)
- Cards de artigos com imagem, resumo e estatísticas

## Configuração

### Variáveis de Ambiente Necessárias
```
DATABASE_URL
PGDATABASE
PGUSER
PGPASSWORD
PGHOST
PGPORT
```

### Comandos Importantes
```bash
# Criar migrações
python manage.py makemigrations

# Aplicar migrações
python manage.py migrate

# Criar superusuário
python manage.py createsuperuser

# Executar servidor
python manage.py runserver 0.0.0.0:5000

# Acessar admin
http://localhost:5000/admin/
```

## Estrutura de URLs

### Principais
- `/` - Landing page com hero banner e feed de notícias
- `/destaques/` - Página de destaques da semana
- `/noticias/` - Feed completo de notícias (estilo Twitter)
- `/jornalista/<username>/` - Perfil do jornalista com publicações
- `/article/<slug>/` - Detalhe do artigo
- `/article/create/` - Criar novo artigo (jornalista/admin)
- `/article/<slug>/edit/` - Editar artigo
- `/article/<slug>/delete/` - Deletar artigo
- `/login/` - Login
- `/register/` - Registro
- `/logout/` - Logout
- `/admin/` - Painel administrativo
- `/api/` - API REST

## Permissões e Roles

### Leitor
- ✓ Visualizar artigos publicados
- ✓ Comentar em artigos
- ✓ Curtir artigos
- ✓ Deletar próprios comentários
- ✗ Criar artigos
- ✗ Editar artigos

### Jornalista
- ✓ Todas as permissões de Leitor
- ✓ Criar artigos
- ✓ Editar próprios artigos
- ✓ Deletar próprios artigos
- ✗ Marcar artigos como destaque
- ✗ Moderar comentários

### Administrador
- ✓ Todas as permissões
- ✓ Editar/deletar qualquer artigo
- ✓ Marcar artigos como destaque
- ✓ Moderar comentários
- ✓ Gerenciar usuários

## Modelos de Dados

### Profile (users)
- user (OneToOne → User)
- role (leitor/jornalista/admin)
- bio
- avatar
- created_at

### Article (articles)
- title
- slug (único)
- content (HTML rico)
- excerpt
- image
- author (FK → User)
- created_at / updated_at
- published (boolean)
- views (contador)
- featured (destaque)
- tags (TaggableManager)
- latitude / longitude / location_name

### Comment (comments)
- article (FK → Article)
- user (FK → User)
- content
- created_at / updated_at
- approved (boolean para moderação)

### Like (articles)
- user (FK → User)
- article (FK → Article)
- created_at
- Unique constraint: (user, article)

## Próximas Melhorias Sugeridas
1. Sistema de notificações para comentários e curtidas
2. Busca avançada com filtros por categoria, tags, autor e data
3. Dashboard com estatísticas de visualizações e engajamento
4. Sistema de compartilhamento em redes sociais
5. Versionamento de artigos com histórico de edições
6. Upload de vídeos além de imagens
7. Newsletter por email
8. Sistema de favoritos/bookmarks
9. Modo escuro
10. PWA para instalação como app

## Notas de Desenvolvimento
- O projeto usa PostgreSQL em produção (Replit Neon database)
- TailwindCSS carregado via CDN (para produção, usar build)
- Cache desabilitado para melhor experiência de desenvolvimento
- Django Debug Toolbar pode ser adicionado para debugging
- Testes unitários podem ser adicionados em cada app

## Segurança
- CSRF protection habilitado
- Autenticação obrigatória para ações sensíveis
- Validação de permissões em todas as views
- Upload de arquivos com validação
- Senhas hashadas com Django Auth
- X-Frame-Options configurado para embedding

## Performance
- Paginação implementada (9 artigos por página)
- Queries otimizadas com select_related/prefetch_related
- Índices em campos slug (unique)
- Cache pode ser habilitado para melhor performance

## Suporte
Para dúvidas ou sugestões sobre o projeto, consulte a documentação do Django ou entre em contato com a equipe de desenvolvimento.
