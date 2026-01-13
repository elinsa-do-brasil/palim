# Palim

App customizado para o sistema de tickets Palim, construído sobre Frappe Helpdesk.

## Recursos

- Customizações upgrade-safe usando fixtures
- Extensões de DocTypes via hooks
- Scripts client-side e server-side personalizados

## Instalação

```bash
bench get-app palim /path/to/palim
bench --site palim.com.br install-app palim
```

## Desenvolvimento

Para exportar fixtures após customizações:

```bash
bench --site palim.com.br export-fixtures
```

## Estrutura

```
palim/
├── hooks.py          # Configuração de hooks e fixtures
├── overrides/        # Extensões de classes de DocTypes
├── fixtures/         # Customizações exportadas
├── public/js/        # Scripts JavaScript customizados
└── templates/        # Templates Jinja personalizados
```
