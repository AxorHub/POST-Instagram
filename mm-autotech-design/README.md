# mm-autotech-design

Plugin de design **auto-contido** para a MM AutoTech. Reúne o sistema de design
da marca + assets confiáveis vendados localmente, para gerar carrosséis premium
de Instagram **sem depender de conectores/APIs externas** na hora de gerar.

## Estrutura

```
mm-autotech-design/
├── .claude-plugin/plugin.json        # manifesto do plugin
└── skills/mm-carousel-pro/
    ├── SKILL.md                      # sistema de design (regras, layouts, do/don't)
    ├── tokens.css                    # cores, tipografia, espaçamento
    ├── components.html               # snippets de componentes reutilizáveis
    ├── fonts.css                     # @font-face das fontes self-hosted
    ├── templates/                    # (reservado p/ layouts por tipo de slide)
    └── assets/
        ├── fonts/                    # Archivo + Inter (.woff2, subset latin)
        ├── icons/                    # SVGs Lucide
        └── logo/                     # monograma MM
```

## Procedência e licenças dos assets

| Asset | Origem | Licença |
|-------|--------|---------|
| Fontes **Archivo**, **Inter** (`.woff2`) | Google Fonts | **OFL 1.1** (uso livre, inclusive comercial) |
| Ícones (`assets/icons/*.svg`) | [Lucide](https://lucide.dev) (`lucide-icons/lucide`) | **ISC/MIT** |
| Monograma **MM** | Criado para a marca | Próprio |

Todos os arquivos são embutidos no repositório — nenhuma chamada de rede é
necessária para renderizar/exportar os slides.

## ⚠️ Regra de marca

A MM AutoTech é uma marca **nova (2026)**. **Nunca** citar tempo de mercado
("desde 1989", "+30 anos", "décadas"). Autoridade vem de **tecnologia de
diagnóstico, transparência e diagnóstico justo**.
