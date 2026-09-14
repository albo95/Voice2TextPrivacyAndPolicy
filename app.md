# Matt — Transcriber per WhatsApp · App & SEO Master File

> File di riferimento: dati App Store + keyword research + strategia SEO del sito.
> Ultimo aggiornamento: 2026-09-14

---

## 1. Dati App Store

| Campo | Valore |
|---|---|
| Nome | **Transcriber per WhatsApp: Matt** (EN: *Transcriber for WhatsApp: Matt*) |
| Sottotitolo | Trascrizione e Riassunti AI (EN: *Transcribe and AI Summary*) |
| App ID | 6618147237 |
| URL Store (IT) | https://apps.apple.com/it/app/transcriber-per-whatsapp-matt/id6618147237 |
| URL Store (global) | https://apps.apple.com/app/id6618147237 |
| Sviluppatore | Alberto Bruno |
| Categoria | Utilities |
| Rating | 4.9 ★ (19 valutazioni, store IT) — lo screenshot store dichiara "5k+ utenti felici" |
| Versione | 2.2.1 (settembre 2026) |
| Prima release | 23/09/2024 |
| Lingue app | AR, EN, FR, DE, IT, PT, RU, ES, TR |
| Età | 4+ |
| Modello | Free + **Pro** (trascrizione on-device con framework Apple) + **Premium** (trascrizione AI via AssemblyAI); entrambi settimanale o annuale, niente lifetime. Riassunti e titoli via OpenAI in entrambi |
| Supporto | albosapps@gmail.com |
| Sito | https://matt-transcriber.netlify.app |

### Tagline store
**"Capisci ogni messaggio in pochi secondi."** — "Un vocale di 4 minuti diventa una lettura di 15 secondi: Tocca il messaggio → Condividi → Matt → Fatto."

### Proposta di valore (dalla descrizione store v2.2, aggiornata 14/09/2026)
1. **Trascrizioni precise, senza buchi**: riconoscimento vocale AI, funziona anche con rumore di fondo, accenti marcati, chi parla veloce.
2. **Tutto in automatico**: rileva la lingua da solo (anche più lingue nello stesso messaggio) e **riconosce i diversi interlocutori** (chi ha detto cosa).
3. **Riassunti AI** con punti chiave, 3 livelli (Essenziale / Conciso / Dettagliato). Anche su testi lunghi e thread.
4. **Oltre 90 lingue di trascrizione** + traduzione in tempo reale nella propria lingua.
5. **Molto più dei vocali**: vocali e testi condivisi da WhatsApp/Telegram/qualsiasi app; import di file audio (riunioni, memo, lezioni) e **file video** (Matt estrae l'audio). Le guide citano anche documenti .txt/.pdf.
6. **La privacy la scegli tu — due motori**: Trascrizione AI (Premium: cloud sicuro, nulla conservato, lingua + interlocutori automatici) oppure Trascrizione on-device (Pro: 100% su iPhone, offline, 25+ lingue). I riassunti AI usano sempre il cloud.
7. **Archivio ricercabile** per contenuto o data.

⚠️ Claim superati, da NON riusare nei testi marketing: "100% on-device di default", "40+ lingue", "tecnologia Apple Speech", "Trascrizione Avanzata" / "AssemblyAI" (il nome del provider resta solo nella privacy policy).

### Flusso d'uso chiave (da comunicare ovunque)
`Tieni premuto il vocale → Inoltra/Condividi → Matt → leggi la trascrizione` (pochi secondi, senza uscire da WhatsApp). Il gancio "in 3 secondi" è stato sostituito con "in pochi secondi" / "in seconds" il 14/09/2026.

### Disclaimer obbligatorio
Strumento NON ufficiale. Nessuna affiliazione con WhatsApp LLC o Telegram. (Va ripetuto nel footer di ogni pagina.)

### Asset
- `Assets/app-icon-1024.png`, `Assets/app-icon-512.png`, `Assets/RoundedIcon.png`
- `Assets/og-image.png` (1200×630, per Open Graph)
- `Assets/screenshots/{it,en}/screenshot-1..5.png` (600×1299, scaricati dallo store il 14/09/2026, set v2.2):
  1. "La migliore Trascrizione per WhatsApp e Telegram" — con riconoscimento speaker (usato anche come hero)
  2. "Riassumi messaggi lunghi" — 7 minuti di audio → 15 secondi di lettura
  3. "Accurato anche con vocali rumorosi"
  4. "Traduci qualsiasi messaggio"
  5. "Risparmia ore quando messaggi" — 4.9 ★, 5k+ utenti felici
- `Assets/videos/onboarding-demo.mp4` (82 s, 560×1148, H.264 crf 31 senza audio, ~4 MB; ricodificato dall'originale HEVC 750×1538 dell'11/08/2026 perché HEVC non si riproduce su Firefox/Chrome Windows) + `onboarding-demo-poster.jpg` (primo frame). I capitoli delle chip su `/` e `/en/` replicano gli step dell'onboarding in-app (loopStart–loopEnd): 📝 0–10 dentro WhatsApp & Telegram · 🎯 10–14 audio disturbati · 🌍 14–23 lingua automatica · 🌐 23–35 traduzione · 🗣️ 35–60 interlocutori · ✨ 60–82 riassunto AI. Se cambia l'onboarding, aggiornare chip, `duration` e `uploadDate` del VideoObject.
- `Assets/videos/whatsapp-howto.mp4`, `telegram-howto.mp4` + poster (guide).
- ⚠️ `~/.gitignore_global` ignora `*.mp4`: il `.gitignore` del repo li riabilita con `!*.mp4`. Senza, i video non arrivano su Netlify (404 fino al 14/09/2026).
- `Assets/appstore-badge-it.svg`, `Assets/appstore-badge-en.svg` (badge ufficiali Apple)

---

## 2. Keyword research

### Logica
L'intento che converte in download è: *ho un vocale (lungo) su WhatsApp e non posso/voglio ascoltarlo* → cerca su Google → atterra su una guida che risolve → CTA App Store. Le query "problema" (senza ascoltare, vocali lunghi, riassunto) convertono meglio delle query generiche "speech to text" (dominate da tool desktop e competitor grossi).

### 🇮🇹 Italiano — mercato primario (store IT, screenshot IT, competizione bassa)

**Primary keywords** (landing page + guida pillar):
| Keyword | Intento | Target |
|---|---|---|
| trascrivere vocali whatsapp | transazionale | Home + guida pillar |
| trascrizione vocali whatsapp | transazionale | Home |
| trascrivere messaggi vocali whatsapp iphone | transazionale | Guida pillar |
| app per trascrivere vocali whatsapp | commerciale | Home |
| vocali whatsapp in testo | transazionale | Guida "convertire" |

**Long-tail** (una guida ciascuna):
| Keyword cluster | Guida |
|---|---|
| come trascrivere i vocali di whatsapp su iphone / trascrivere audio whatsapp gratis | `guide/trascrivere-vocali-whatsapp/` (pillar) |
| convertire vocali whatsapp in testo / audio whatsapp in testo | `guide/convertire-vocali-whatsapp-in-testo/` |
| riassumere vocali whatsapp / riassunto messaggio vocale lungo | `guide/riassumere-vocali-whatsapp/` |
| tradurre vocali whatsapp / tradurre messaggi vocali in italiano | `guide/tradurre-vocali-whatsapp/` |
| leggere i vocali senza ascoltarli / ascoltare vocali di nascosto senza visualizzare | `guide/leggere-vocali-whatsapp-senza-ascoltarli/` |
| trascrivere vocali telegram | `guide/trascrivere-vocali-telegram/` |
| trascrivere audio in testo iphone / trascrivere registrazioni lezioni riunioni | `guide/trascrivere-audio-in-testo-iphone/` |

### 🇬🇧 English — mercato secondario (volume alto, competizione più alta)

**Primary:** transcribe whatsapp voice message · whatsapp voice message to text · whatsapp audio transcription app iphone

**Long-tail** (una guida ciascuna):
| Keyword cluster | Guida |
|---|---|
| how to transcribe whatsapp voice messages on iphone | `en/guides/transcribe-whatsapp-voice-messages/` (pillar) |
| convert whatsapp voice message to text | `en/guides/convert-whatsapp-voice-message-to-text/` |
| summarize whatsapp voice messages / long voice note summary | `en/guides/summarize-whatsapp-voice-messages/` |
| translate whatsapp voice messages | `en/guides/translate-whatsapp-voice-messages/` |
| read voice messages without listening | `en/guides/read-whatsapp-voice-messages-without-listening/` |
| transcribe telegram voice messages | `en/guides/transcribe-telegram-voice-messages/` |
| transcribe audio to text on iphone (lectures, meetings, voice memos) | `en/guides/transcribe-audio-to-text-iphone/` |

### Keyword da NON inseguire (per ora)
- "speech to text", "voice to text app" — troppo generiche, SERP dominata da Google/Otter/Notta.
- "whatsapp transcription android" — l'app è solo iOS: attirerebbe traffico che non converte (ok solo menzionarlo in FAQ).
- Brand altrui ("TranscribeMe", "Transcriber for WhatsApp <competitor>") — rischioso e poco utile.

---

## 3. Architettura del sito

```
/                       → landing IT (lang=it) — hero, download, screenshot, come funziona, guide, FAQ, CTA, footer
/en/                    → landing EN (lang=en)
/guide/<slug>/          → 7 guide IT
/en/guides/<slug>/      → 7 guide EN
/privacy-policy/        → privacy (EN, invariata nei contenuti)
/terms-of-use/          → terms (EN, invariati nei contenuti)
/sitemap.xml, /robots.txt
```

**Retro-compatibilità link store** (NON rompere mai):
`/#privacy-policy` e `/#terms-of-use` → redirect JS su index verso le nuove pagine. Sono i link stampati nella descrizione App Store.

**Hreflang:** ogni pagina IT ↔ EN gemella, `x-default` → versione EN.
**Schema.org:** SoftwareApplication + FAQPage sulla landing; Article + BreadcrumbList + FAQPage sulle guide.

### SEO on-page checklist (applicata a ogni pagina)
- Title ≤ 60 caratteri con keyword primaria all'inizio
- Meta description 140–155 caratteri con CTA
- H1 unico = keyword primaria; H2 = varianti/long-tail
- Alt text keyword-rich sugli screenshot
- Internal linking: guide ↔ guide correlate ↔ home; FAQ → "Scopri di più" verso la guida
- Immagini con width/height + loading=lazy (no CLS)
- Canonical assoluto + Open Graph + Twitter Card
