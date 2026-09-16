# Guida SEO — Matt Transcriber: da "sito su Netlify" a "sito che porta download"

> Audit del 16/09/2026 sul repo e sul sito live. Parte A = cosa è già stato fatto nel repo. Parte B = cosa devi fare tu, in ordine. Parte C = strategia continuativa (contenuti, backlink, ASO).
> Obiettivo: farsi trovare su Google/Bing/ChatGPT in tutte e 7 le lingue e trasformare le visite in download.

---

## Diagnosi in una riga

Il codice del sito era già sopra la media (hreflang, sitemap, canonical, dati strutturati, immagini con dimensioni). **Il problema è che il sito non risulta indicizzato**: `site:matt-transcriber.netlify.app` non restituisce nessuna pagina. Non c'è Search Console, non c'è misurazione, non ci sono backlink (a parte la scheda App Store) e manca il dominio proprio. Il codice lo sistemo io; indicizzazione, dominio, misurazione e link li puoi fare solo tu.

Aspettative realistiche: italiano (competizione bassa) → prime visite 4–8 settimane dopo l'indicizzazione. EN/DE/FR/ES/PT → 3–6 mesi e solo con backlink.

---

## Parte A — Fatto nel repo il 16/09/2026 (va online al prossimo push)

| Cosa | Dove | Effetto |
|---|---|---|
| **Smart App Banner** `<meta name="apple-itunes-app">` su tutte le 59 pagine | generato da `scripts/i18n.py` | Safari su iPhone mostra il banner nativo "Scarica/Apri" con icona e rating: la CTA con la conversione più alta per un'app iOS |
| **Screenshot in WebP** (da 320–430 KB a 50–75 KB l'uno, −80%) | `Assets/screenshots/*/*.webp`, PNG rimossi | LCP e peso pagina mobile molto più bassi (Core Web Vitals = ranking + conversione) |
| **Cache asset** un anno, `immutable` | `_headers` | Ritorni e navigazione tra pagine istantanei. ⚠️ Se cambi un file in `Assets/` mantenendo il nome, rinominalo (es. `screenshot-1-v2.webp`) |
| **File interni nascosti** (`app.md`, `GUIDA-SEO.md`, `scripts/*`, `.gitignore` → 404) | `_redirects` | Prima erano pubblici su Netlify (200) |
| **Pagina 404** con link alle 7 lingue e badge store, `noindex` | `404.html` | Netlify la serve da sola; niente più pagina grigia |
| **JSON-LD `WebSite` + `Organization`** sulle 7 home | generato da `scripts/i18n.py` | Nome sito e brand nei risultati, base per i sitelink |
| **Script link campagna App Store** | `scripts/campaign_links.py` | Un comando aggiunge `pt`/`ct`/`mt` a tutti i 171 link store (ct = `site-<lingua>-<pagina>`) |
| **Script migrazione dominio** | `scripts/set_domain.py` | Un comando sostituisce l'host in canonical/hreflang/og/JSON-LD/robots/sitemap e rigenera tutto |
| Header di sicurezza `nosniff`, `Referrer-Policy` | `_headers` | Igiene, nessun effetto SEO diretto |

Verificato: 182 blocchi JSON-LD validi su 59 pagine, script idempotenti, redirect JS `#privacy-policy` → `/privacy-policy/` intatto.

Da controllare tu dopo il push (5 minuti):
- `curl -I https://matt-transcriber.netlify.app/app.md` → `404`
- `curl -I https://matt-transcriber.netlify.app/Assets/screenshots/it/screenshot-1.webp` → `200` con `cache-control: public, max-age=31536000, immutable`
- Apri la home da Safari su iPhone: deve comparire il banner dell'app in alto
- [Rich Results Test](https://search.google.com/test/rich-results) sulla home: FAQ, Video, SoftwareApplication validi

---

## Parte B — Da fare tu, in questo ordine

### B1. Compra il dominio e collegalo (1 ora, 10–15 €/anno)

**Perché:** fiducia e click nei risultati (`matttranscriber.com/guide/...` batte `matt-transcriber.netlify.app/...`), brand search, portabilità (i backlink restano tuoi se lasci Netlify), URL credibili in App Store Connect, email `support@…`.

**Quale.** Un solo dominio generico con le sottocartelle lingua che già hai. Mai 7 domini nazionali, mai un `.it` come principale (penalizza fuori dall'Italia).
| Dominio | Stato al 16/09 | Note |
|---|---|---|
| `matttranscriber.com` | **libero** (whois) | Scelta consigliata |
| `matt-transcriber.app` / `matttranscriber.app` | non verificato | Ottimo per un'app (HTTPS forzato); controlla su [get.app](https://get.app) |
| `matttranscriber.it`, `matt-transcriber.it` | liberi | Solo per proteggere il brand, con redirect al `.com` |

**Dove:** [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/) (prezzo di costo, niente rincari al rinnovo). Alternative: Porkbun, Namecheap. Privacy WHOIS e rinnovo automatico attivi.

**Collegamento a Netlify:**
1. Netlify → Site → **Domain management → Add a domain** → `matttranscriber.com`.
2. DNS: o **Netlify DNS** (cambi i nameserver dal registrar) o DNS su Cloudflare con i record che Netlify ti mostra (A per l'apex, CNAME per `www`). Su Cloudflare metti il record in **DNS only** (nuvola grigia), altrimenti il certificato Let's Encrypt di Netlify va in conflitto.
3. Imposta il dominio come **Primary domain**. Netlify fa il **301 automatico** da `matt-transcriber.netlify.app/*` e da `www`. HTTPS arriva in pochi minuti.
4. Prova `https://matt-transcriber.netlify.app/#privacy-policy` → deve finire su `https://matttranscriber.com/privacy-policy/` (il browser conserva il `#hash` attraverso il 301, quindi i link stampati nella descrizione App Store restano validi).

**Nel repo (2 minuti):**
```bash
python3 scripts/set_domain.py matttranscriber.com
grep -r 'netlify.app' . --include='*.html' | wc -l    # deve dare 0
git add -A && git commit -m "Dominio custom matttranscriber.com" && git push
```
Lo script aggiorna 1700 riferimenti in 62 file, il `BASE` di `i18n.py`, `robots.txt` e la sitemap.

**Fuori dal repo:**
- App Store Connect → App Information: **Marketing URL, Support URL, Privacy Policy URL** con il nuovo dominio (le URL si aggiornano senza nuova release; i link nella descrizione cambiali alla prossima).
- **Non cancellare mai** il sito `netlify.app`: il 301 deve restare per sempre per le versioni dell'app già pubblicate.

### B2. Google Search Console (30 minuti, la cosa più importante)

1. [search.google.com/search-console](https://search.google.com/search-console) → **Aggiungi proprietà → Dominio** `matttranscriber.com` → verifica con record **TXT** nel DNS (copre http/https/www/sottodomini). Se non hai ancora il dominio, fai intanto la proprietà **Prefisso URL** `https://matt-transcriber.netlify.app/` verificata con il tag HTML: incolla il `<meta name="google-site-verification">` nell'`<head>` di `index.html` e pusha.
2. **Sitemap → aggiungi** `sitemap.xml`. Atteso: "Riuscito, 58 URL".
3. **Controllo URL → Richiedi indicizzazione** (limite ~10/giorno) per: le 7 home (`/`, `/en/`, `/fr/`, `/de/`, `/es/`, `/es-419/`, `/pt-br/`) e le 7 guide "trascrivere vocali WhatsApp". Il resto lo trova dalla sitemap.
4. Se hai fatto prima la proprietà `netlify.app` e poi il dominio: **Impostazioni → Cambio di indirizzo** dalla vecchia alla nuova (entrambe verificate). Trasferisce i segnali in giorni.
5. Dopo 7–14 giorni: **Indicizzazione → Pagine**: obiettivo 58 indicizzate. "Scansionata, attualmente non indicizzata" sulle pagine tradotte è normale all'inizio.
6. **Rendimento**, filtri **Paese** e **Query**: è l'unica fonte di verità su quali lingue e keyword funzionano. 15 minuti ogni settimana.

### B3. Bing Webmaster Tools (10 minuti)
[bing.com/webmasters](https://www.bing.com/webmasters) → **Importa da Google Search Console**. Copre Bing, DuckDuckGo, Yahoo, ChatGPT Search e Copilot.

### B4. Link campagna App Store (20 minuti: senza, non saprai mai quanti download porta il sito)
1. App Store Connect → **App Analytics → Campagne (Campaign links)** → crea un provider (es. "Sito web") e un link qualsiasi. Nell'URL generato trovi `?pt=XXXXXXX&ct=...&mt=8`: copia il numero dopo `pt=`.
2. Nel repo:
   ```bash
   python3 scripts/campaign_links.py XXXXXXX
   git add -A && git commit -m "Link campagna App Store" && git push
   ```
   Tutti i 171 link store ricevono `pt=…&ct=site-<lingua>-<pagina>&mt=8` (es. `site-it-home`, `site-de-transcribe-whatsapp`, `site-en-legal`). Per rimuoverli: `python3 scripts/campaign_links.py --remove`.
3. Dopo qualche giorno, in App Analytics → **Acquisizione → Campagne** vedi impression, visualizzazioni scheda, download e ricavi per lingua e per pagina. Niente cookie, niente banner.

### B5. Analytics senza cookie (15 minuti, opzionale ma utile)
Una tra: **Netlify Analytics** (9 $/mese, lato server, zero script), **Cloudflare Web Analytics** (gratis se il DNS è su Cloudflare, uno script leggero), **Plausible** o **Umami** (~9 $/mese o self-host). Evita GA4: banner cookie obbligatorio in UE e pagina più pesante. Con Plausible/Umami aggiungi un evento custom sul click di `a[href*="apps.apple.com"]` per sapere quali pagine convertono.

### B6. Netlify: controlli una tantum
- **Deploy previews**: Site configuration → Build & deploy → Deploy contexts. Se non li usi, disattivali; altrimenti verifica con `curl -I` su un URL `deploy-preview-N--…` che ci sia `x-robots-tag: noindex` (Netlify lo aggiunge da solo, ma controlla).
- **Asset optimization**: lascia disattivata (i file sono già ottimizzati e la cache è gestita da `_headers`).

### B7. Verifiche di qualità (dopo il push)
- [PageSpeed Insights](https://pagespeed.web.dev/) sulla home mobile IT ed EN: obiettivo Performance ≥ 90, LCP < 2,5 s. (Il 16/09 la quota API era esaurita: misura tu.)
- [hreflang checker](https://technicalseo.com/tools/hreflang/) su `/` e `/de/`: nessun errore di reciprocità.
- `aggregateRating` nello schema (4.9, 19 valutazioni) deve restare **reale**: allinealo allo store IT a ogni aggiornamento del sito. Il rating nello snippet alza il CTR, ma solo se vero.

---

## Parte C — Strategia continuativa

### C1. Multilingua: come rankare in ogni paese
L'architettura è giusta. Ciò che ora decide il ranking per lingua:
1. **Qualità nativa dei testi.** FR/DE/ES/ES-419/PT-BR sono traduzioni AI. Fai rileggere landing + guida pillar a un madrelingua per lingua (Fiverr/Upwork, 20–40 € a lingua, o utenti dell'app in cambio di Premium). Priorità: title, H1, primo paragrafo, FAQ.
2. **Keyword research per lingua, non traduzione delle keyword italiane.** Esempi: DE "WhatsApp Sprachnachricht in Text umwandeln" e "Sprachnachricht transkribieren lassen"; ES-419 "audios de WhatsApp" più di "notas de voz"; PT-BR "transcrever áudio do WhatsApp". Strumenti: Google Suggest e "Le persone hanno chiesto anche" con `&gl=de&hl=de` nell'URL di Google, poi Search Console dopo 4 settimane. Aggiorna i cluster in `app.md`.
3. **Un backlink per lingua vale più di dieci in italiano** (C2).
4. **Scheda App Store localizzata** in tutte le lingue del sito: l'utente tedesco che atterra su una scheda inglese converte meno. I link store per paese sul sito sono già giusti.
5. **AR, RU, TR**: l'app li supporta, il sito no. Competizione bassissima e mercati WhatsApp enormi (soprattutto AR e TR). Quando le 7 lingue sono stabili: nuova riga in `LOCALES` di `i18n.py` + traduzione madrelingua.
6. **Niente redirect automatico per lingua** (IP/browser): Googlebot scansiona dagli USA e vedrebbe solo EN. Il menu manuale è corretto.

### C2. Backlink e distribuzione (ciò che manca davvero)
Hai 1 link in entrata. Nessun sito nuovo ranka in EN/DE/FR/ES senza link. Dal più facile:

**Gratis, subito**
- Directory: AlternativeTo, **Product Hunt** (lancio con il video demo, ideale per EN), Uneed, SaaSHub, AppAdvice, Softonic iOS, AppAgg, Indie Hackers.
- Profili: GitHub README, LinkedIn, X, Threads, Mastodon con link al sito.
- **YouTube**: carica il video demo (UI inglese) con titolo/descrizione EN; 3 Shorts con titoli IT/DE/FR/ES/PT. I video YouTube compaiono nei risultati Google per "come trascrivere vocali WhatsApp". Link al sito in descrizione.
- Reddit/Quora/forum: r/whatsapp, r/iphone, r/iOSapps, r/productivity, Quora IT/EN, Apple Support Communities, forum locali (Hardware Upgrade IT, MacGeneration FR, iPhone-Ticker DE, Applesfera ES). Rispondi a chi chiede "come trascrivo un vocale" linkando **la guida** e dichiarando che sei lo sviluppatore. Utile sì, spam no.

**Con un po' di lavoro**
- Outreach a blog/newsletter su app iPhone e "trucchi WhatsApp" in ogni lingua: test dell'app in cambio di codici Premium. Obiettivo: 1 link nuovo a settimana, alternando lingua.
- Guest post con la guida "leggere i vocali senza ascoltarli" (la più condivisa).
- HARO/Connectively/Qwoted (EN) per citazioni su "voice notes", "WhatsApp productivity".

**Da evitare**: link comprati, PBN, "1000 backlink a 5 $", scambi massicci tra i tuoi siti.

### C3. Contenuti: pagine da aggiungere, in ordine
1. **"La trascrizione di WhatsApp non funziona / non disponibile nella mia lingua"**: WhatsApp ha la trascrizione nativa dal 2024 ma limitata; è la query in crescita più forte. Con tabella "WhatsApp nativo vs Matt".
2. **"Migliori app per trascrivere vocali WhatsApp su iPhone (2026)"**: listicle onesto con 4–5 app, Matt primo.
3. **Prezzi / Pro vs Premium**: intento commerciale ("matt transcriber prezzo"), trasparenza = fiducia.
4. **"Trascrivere vocali WhatsApp gratis"**: intento altissimo in IT/ES/PT; sii onesto sui limiti del free.
5. **Casi d'uso verticali** (IT+EN prima): gruppi di lavoro, genitori/nonni, studenti e lezioni, riunioni Zoom/Meet importate come video.
6. **Novità/Changelog** aggiornato a ogni release.
7. **FAQ/Supporto estesa**: ogni domanda ricevuta via email diventa una voce.

Per ogni pagina nuova: riga in `GUIDES` di `i18n.py` + `python3 scripts/i18n.py` (hreflang, sitemap, banner, menu); title ≤ 60 caratteri con keyword all'inizio; primo paragrafo che risponde subito; ≥ 3 link interni in entrata; screenshot reale con `alt`; badge store dopo il primo blocco utile e in fondo; claim di prodotto controllati su `app.md`. Se hai già lanciato `campaign_links.py`, rilancialo dopo aver aggiunto pagine.

Manutenzione: ogni 3–4 mesi rileggi le guide pillar, aggiorna "2026" nei title a gennaio, sostituisci screenshot quando cambia la UI (rinominando i file).

### C4. ASO: dove arrivano davvero i download
Per un'utility iOS il 60–80% dei download viene dalla **ricerca App Store**. Il sito è il secondo canale e serve a intercettare Google, dare fiducia e ricevere traffico da social/forum.
- Titolo, sottotitolo e keyword field localizzati con le stesse keyword del sito (coerenza = brand search). Usa la skill `/app-store-aso` in Claude Code per una revisione.
- Richiesta recensione in-app (`SKStoreReviewController`) dopo la terza trascrizione riuscita, mai al primo avvio. Rating e numero di recensioni: fattore ASO n. 2 e alimentano il rich snippet del sito.
- **Custom Product Pages** "WhatsApp" e "Telegram", linkate dalle guide corrispondenti.
- **Apple Search Ads Basic**: 5–10 €/giorno su "trascrivere vocali whatsapp" in IT per 2 settimane, per validare quali keyword convertono; poi le spingi sul sito.
- Rispondi alle recensioni in ogni lingua.

---

## Piano operativo

**Questa settimana (2 ore)**
- [ ] Push delle modifiche del 16/09 + i 4 controlli della Parte A
- [ ] B1 dominio (acquisto, Netlify primary, `set_domain.py`, App Store Connect)
- [ ] B2 Search Console (proprietà Dominio, sitemap, 14 richieste di indicizzazione)
- [ ] B3 Bing import
- [ ] B4 campaign links (`campaign_links.py`)

**Settimane 2–3**
- [ ] B5 analytics, B6 controlli Netlify, B7 PageSpeed/hreflang
- [ ] YouTube (demo + 3 Shorts) e 5 directory (Product Hunt programmato)
- [ ] Revisione madrelingua landing + pillar DE/FR/ES/PT-BR

**Mese 2**
- [ ] Pagine C3 n. 1 e 2 in IT+EN, poi nelle altre lingue
- [ ] 10 risposte utili su forum/Reddit/Quora per lingua
- [ ] Outreach: 5 blog IT/EN, 3 per DE/FR/ES
- [ ] Apple Search Ads Basic test IT
- [ ] Prima analisi Search Console: pagine in posizione 8–20 → migliora title e primo paragrafo

**Mese 3 e routine**
- [ ] Pagine C3 n. 3–5; changelog a ogni release
- [ ] 1 backlink nuovo a settimana
- [ ] Ogni settimana 15 min: Search Console + App Analytics campagne
- [ ] Ogni release: claim su sito (`app.md` è la fonte), screenshot (rinominati), rating nello schema, chip video se cambia l'onboarding
- [ ] Ogni 3 mesi: guide pillar, link rotti (`npx linkinator https://matttranscriber.com --recurse`), Core Web Vitals

---

## Riferimenti
- Search Console: https://search.google.com/search-console
- Bing Webmaster: https://www.bing.com/webmasters
- PageSpeed Insights: https://pagespeed.web.dev/ · Rich Results Test: https://search.google.com/test/rich-results · hreflang: https://technicalseo.com/tools/hreflang/
- Google, siti multilingua: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites
- Apple Smart App Banner: https://developer.apple.com/documentation/webkit/promoting-apps-with-smart-app-banners
- Apple campaign links: https://developer.apple.com/app-store/app-analytics/
- Netlify domini: https://docs.netlify.com/domains/ · headers: https://docs.netlify.com/routing/headers/ · redirects: https://docs.netlify.com/routing/redirects/
- Apple Search Ads: https://searchads.apple.com/
