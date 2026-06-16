---
name: mm-carousel-pro
description: >
  Sistema de design premium para carrosséis de Instagram da MM AutoTech.
  Use sempre que for criar/gerar carrossel, slides ou post multi-imagem para
  @mmautotech8. Estética dark-first tech-automotiva (vermelho + preto + grafite),
  com fontes Archivo/Inter self-hosted, ícones Lucide e componentes de marca.
  Tudo auto-contido — sem conectores externos na geração.
---

# MM Carousel Pro — Sistema de Design

Gera carrosséis 1080×1350 (4:5) coesos e premium para a MM AutoTech.
Layout em **420×525** e export com `device_scale_factor = 1080/420`.

## Marca (ler antes de escrever qualquer copy)

- MM AutoTech — oficina em **João Monlevade (MG)**, **marca nova (2026)**.
  ⚠️ **Nunca citar Guarulhos.**
- Serviços: diagnóstico/scanner OBD-II, ar-condicionado, injeção, freios,
  suspensão, câmbio, direção hidráulica, retífica.
- Tom: técnico, direto, confiável.
- ⚠️ **PROIBIDO:** "desde 1989", "+30 anos", "décadas", qualquer tempo de mercado.
  Autoridade = **tecnologia + transparência + diagnóstico justo**.

## Tokens

Use `tokens.css`. Resumo: vermelho `#E10600`, preto `#0A0A0B`, grafite `#141418`,
texto `#EDEDEF`, secundário `#9A9AA2`. Display = **Archivo** (600/700/800),
corpo = **Inter** (400–700). Gradiente e glow definidos em tokens.

## Assets (vendados, licença livre)

- **Fontes:** `assets/fonts/*.woff2` (Archivo + Inter, OFL). Embutir como base64
  no HTML para o export não depender de rede.
- **Ícones:** `assets/icons/*.svg` (Lucide, MIT). São `stroke="currentColor"`:
  controle a cor pelo CSS `color:` do contêiner. Inline no HTML (remover
  width/height fixos e definir por uso).
- **Logo oficial:** `assets/logo/mm-logo.png` (cromado 3D, fundo transparente).
  Embutir como base64 **uma vez** no CSS (`.mmlogo{background:url(...)}`) e usar
  divs dimensionadas. Aparece na capa (grande), no topo de cada slide e no CTA.

## Estrutura de slides (listicle 7 — padrão)

| # | Tipo | Fundo | Conteúdo |
|---|------|-------|----------|
| 1 | Capa | escuro `#0A0A0B` + glow vermelho + grid + barra de acento | **logo oficial grande** + gancho forte + "arrasta →" |
| 2–6 | Itens | alterna preto `#0A0A0B` / grafite `#141418` | logo no topo, nº fantasma gigante, ícone em token, eyebrow, título, corpo, chip de diagnóstico |
| 7 | CTA | escuro + glow vermelho | logo + headline + botão WhatsApp + @handle |

### Módulo de slide de item (estrutura fixa = "estruturado")
1. **Top meta bar:** monograma MM • label da série (ex.: "AR-CONDICIONADO") • contador "02 / 07".
2. **Número fantasma** (Archivo 800, ~150px, baixa opacidade) ao fundo.
3. **Ícone** em token arredondado com tint vermelho.
4. **Eyebrow** vermelho (ex.: "CAUSA 02").
5. **Título** (Archivo 700, ~32px).
6. **Corpo** (Inter 400, 16px, `--mm-muted`), máx ~320px largura.
7. **Chip de diagnóstico** com ícone `scan-line`: "DIAGNÓSTICO › …".
8. **Rodapé:** barra de progresso + `@mmautotech8`.

## Regras de export (Playwright)

- Viewport 420×525, `device_scale_factor = 1080/420`.
- `wait_until="networkidle"` + 1s (fontes já base64, mas garante layout).
- Esconder chrome do frame IG; capturar só `.carousel-viewport` com `clip`.
- Snap por slide: `track.style.transition='none'` antes de transladar.

## Fluxo

1. Gerar HTML via **Python** (`Path.write_text`) — nunca heredoc de shell.
2. Exportar PNGs e mostrar para revisão. **Não publicar sem aprovação.**
3. Ajustar só os slides citados; não regerar tudo à toa.
