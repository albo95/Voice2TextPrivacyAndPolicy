# Cosa devo fare io — sito Matt Transcriber

> Aggiornata il 16/09/2026. Il sito è online su **https://matt-transcriber.com**.
> Tutta la parte tecnica (codice, dominio, redirect, sitemap) è **già fatta**. Qui c'è **solo quello che devi fare tu**, in ordine.
> Spunta ogni casella quando hai finito. Quando c'è scritto **"scrivi a Claude"**, apri Claude in questa cartella e incolla la frase.

---

## OGGI

### ☐ 1. Pubblicare le modifiche (1 minuto)

Scrivi a Claude: **`pusha`**

Serve a mettere online il sito aggiornato con il nuovo indirizzo.

---

### ☐ 2. App Store Connect: cambiare i link (10 minuti)

1. Vai su [appstoreconnect.apple.com](https://appstoreconnect.apple.com) → **App** → **Matt**.
2. A sinistra clicca **Informazioni app** (App Information).
   - **URL informativa sulla privacy** → scrivi `https://matt-transcriber.com/privacy-policy/`
   - Clicca **Salva** in alto a destra.
3. A sinistra clicca la **versione attuale** dell'app (es. "1.x Pronta per la vendita").
   - **URL assistenza** → `https://matt-transcriber.com/`
   - **URL marketing** → `https://matt-transcriber.com/`
   - Clicca **Salva**.

Non serve pubblicare una nuova versione dell'app.

⚠️ **Non cancellare e non rinominare mai il progetto su Netlify.** Il vecchio indirizzo `matt-transcriber.netlify.app` deve restare attivo, perché le versioni dell'app già scaricate lo usano. Adesso porta in automatico al sito nuovo.

---

### ☐ 3. Google Search Console: dire a Google che il sito esiste (20 minuti)

**È la cosa più importante di tutta la guida.** Oggi Google non conosce il sito, quindi chi cerca non lo trova.

**3a. Aggiungi il sito**
1. Vai su [search.google.com/search-console](https://search.google.com/search-console) e fai login con il tuo account Google.
2. Clicca **Aggiungi proprietà**.
3. Nel riquadro di **sinistra ("Dominio")** scrivi `matt-transcriber.com` → **Continua**.
4. Google ti mostra un codice lungo che inizia con `google-site-verification=`.
   - **Se vedi un pulsante tipo "Verifica con Cloudflare":** cliccalo, fai login su Cloudflare e conferma. Fatto.
   - **Altrimenti:**
     1. clicca **Copia** accanto al codice;
     2. in un'altra scheda apri [dash.cloudflare.com](https://dash.cloudflare.com) → **matt-transcriber.com** → **DNS** → **Records** → **Add record**;
     3. **Type:** `TXT` · **Name:** `@` · **Content:** incolla il codice → **Save**;
     4. torna su Google e clicca **Verifica**. Se dà errore, riprova tra 10 minuti.

**3b. Invia la mappa del sito**
1. Nel menu a sinistra clicca **Sitemap**.
2. Nel campo scrivi `sitemap.xml` → **Invia**.
3. Va bene quando lo stato diventa **"Riuscito"** (anche dopo qualche ora).

**3c. Chiedi a Google di leggere le pagine principali**
In alto c'è una barra di ricerca **"Controlla qualsiasi URL"**. Per **ognuno** dei 7 indirizzi qui sotto:
incollalo nella barra → premi Invio → aspetta qualche secondo → clicca **Richiedi indicizzazione** → aspetta la conferma → passa al successivo.

```
https://matt-transcriber.com/
https://matt-transcriber.com/en/
https://matt-transcriber.com/fr/
https://matt-transcriber.com/de/
https://matt-transcriber.com/es/
https://matt-transcriber.com/es-419/
https://matt-transcriber.com/pt-br/
```

Google ne accetta circa 10 al giorno. Le altre pagine le trova da solo con la sitemap.

---

### ☐ 4. Bing (vale anche per ChatGPT e Copilot) (5 minuti, dopo il punto 3)

1. Vai su [bing.com/webmasters](https://www.bing.com/webmasters).
2. Accedi **con lo stesso account Google** del punto 3.
3. Scegli **Importa da Google Search Console** → **Consenti** → seleziona `matt-transcriber.com` → **Importa**.

---

## DOMANI

### ☐ 5. Contare i download che arrivano dal sito (10 minuti)

Senza questo passo non saprai mai se il sito porta download.

1. [appstoreconnect.apple.com](https://appstoreconnect.apple.com) → **App Analytics** (Analisi app) → apri **Matt**.
2. Cerca il pulsante **"Genera link campagna"** (Generate a Campaign Link), di solito nella scheda **Acquisizione / Sources**.
3. Nel campo **Campagna** scrivi `sito` e genera il link.
4. Nel link che compare c'è un pezzo tipo `pt=123456789`. **Copia solo il numero.**
5. Scrivi a Claude: **`lancia campaign_links con pt=123456789 e pusha`** (usa il tuo numero).

Dopo 2–3 giorni, in App Analytics → **Acquisizione → Campagne** vedrai quanti download arrivano da ogni pagina del sito.

---

### ☐ 6. Due controlli veloci (5 minuti)

- ☐ **Da iPhone, con Safari**, apri `matt-transcriber.com`: in alto deve comparire la barra con l'icona di Matt e il pulsante **Apri** o **Visualizza**.
- ☐ **Netlify** → progetto matt-transcriber → **Project configuration** → **Build & deploy** → **Deploy Previews**: se non sai cosa sono, mettili su **disattivati** (evita che Google trovi copie del sito).

Se qualcosa non va, manda lo screenshot a Claude.

---

## TRA 2 SETTIMANE

### ☐ 7. Controllare che Google stia leggendo il sito (5 minuti)

Search Console → menu **Pagine**. Il numero accanto a **"Indicizzate"** deve salire verso **58**.
- Se è **0**: manda uno screenshot a Claude.
- Se vedi "Scansionata, attualmente non indicizzata" su alcune pagine: è normale all'inizio, non fare niente.

Da qui in poi, **ogni lunedì 15 minuti:** Search Console → **Rendimento** → guarda le schede **Query** (cosa cercano) e **Paesi**. Una volta al mese manda lo screenshot a Claude con: *"guarda Search Console e dimmi cosa migliorare"*.

---

## PER FAR ARRIVARE PIÙ PERSONE (settimane 2–8)

Google mette in alto i siti che **altri siti linkano**. Oggi Matt ha un solo link, quello dell'App Store. Questa è la parte che porta davvero visite.

### ☐ 8. Iscrivere Matt a questi siti (1 ora in tutto, gratis)

Per ognuno: crea un account, aggiungi l'app, metti come sito `https://matt-transcriber.com` e il link App Store.
- ☐ [AlternativeTo](https://alternativeto.net) → aggiungi Matt come alternativa per "WhatsApp transcription"
- ☐ [SaaSHub](https://www.saashub.com)
- ☐ [Uneed](https://www.uneed.best)
- ☐ [AppAgg](https://appagg.com)
- ☐ [Indie Hackers](https://www.indiehackers.com) → racconta in un post come hai creato l'app
- ☐ Metti `matt-transcriber.com` nella bio di LinkedIn, Instagram, X e Threads

### ☐ 9. YouTube (1 ora)

- ☐ Carica il video demo dell'app. Titolo: `How to transcribe WhatsApp voice messages on iPhone`. Nella descrizione metti come prima riga `https://matt-transcriber.com`.
- ☐ Fai 3 Shorts, con titoli in italiano, tedesco e spagnolo. Per i titoli scrivi a Claude: *"dammi 3 titoli per Shorts YouTube in IT, DE, ES"*.

### ☐ 10. Product Hunt (una volta sola, preparalo bene)

Scrivi a Claude: *"aiutami a preparare il lancio su Product Hunt"*. Scegli un martedì o un mercoledì.

### ☐ 11. Ogni settimana, 30 minuti: rispondere a chi cerca aiuto

1. Su Google cerca `come trascrivere vocali whatsapp reddit` oppure `transcribe whatsapp voice message reddit`.
2. Apri le discussioni recenti su Reddit, Quora o nei forum Apple.
3. Rispondi spiegando davvero come fare, metti il link alla **guida** del sito (non alla home) e scrivi *"sono lo sviluppatore"*.

Obiettivo: 2–3 risposte a settimana. ❌ Mai copia-incolla uguali, mai comprare link.

### ☐ 12. Scrivere a un blog a settimana

Cerca su Google `migliori app iPhone blog` o `trucchi WhatsApp` (anche in inglese, tedesco e spagnolo). Scrivi all'autore. Per il testo della mail scrivi a Claude: *"scrivimi la mail per un blogger, in [lingua], offrendo un codice Premium"*.

### ☐ 13. Traduzioni rilette da un madrelingua (entro un mese)

Il tedesco, il francese, lo spagnolo e il portoghese del sito sono tradotti con l'AI.
1. Trova una persona per lingua: su [Fiverr](https://www.fiverr.com) cerca "proofreading German" (20–40 €), oppure chiedi a un utente dell'app in cambio di Premium.
2. Fagli rileggere **solo la home** e **la guida WhatsApp** della sua lingua.
3. Manda le correzioni a Claude: *"applica queste correzioni al tedesco"*.

---

## DAL SECONDO MESE

### ☐ 14. Una pagina nuova ogni 2 settimane

Scrivi a Claude, una alla volta: *"crea la pagina [titolo] in tutte le lingue seguendo la guida SEO"*. In questo ordine:
1. ☐ La trascrizione di WhatsApp non funziona o non c'è nella mia lingua
2. ☐ Migliori app per trascrivere i vocali WhatsApp su iPhone
3. ☐ Prezzi: Pro o Premium?
4. ☐ Trascrivere vocali WhatsApp gratis
5. ☐ Matt per il lavoro, per gli studenti, per genitori e nonni

### ☐ 15. App Store (a ogni nuova versione dell'app)

La maggior parte dei download arriva dalla **ricerca dentro l'App Store**, non da Google.
- ☐ Scrivi a Claude **`/app-store-aso`** per migliorare titolo, sottotitolo e parole chiave.
- ☐ Rispondi alle recensioni, anche a quelle in altre lingue.
- ☐ Scrivi a Claude: *"è uscita la versione X, ecco cosa è cambiato: …, aggiorna il sito"*. Aggiorna anche il voto (oggi 4.9 ★ con 19 valutazioni).
- ☐ *(Facoltativo)* Prova [Apple Search Ads Basic](https://searchads.apple.com): 5 € al giorno per 2 settimane, solo in Italia.

---

## Quando aspettarsi risultati

- **Italia:** prime visite da Google 4–8 settimane dopo il punto 3.
- **Altre lingue:** 3–6 mesi, e solo se fai i punti 8–13.
- Se dopo 2 mesi Search Console mostra 0 visite, manda lo screenshot a Claude.

## Link che ti servono
- Google Search Console: https://search.google.com/search-console
- App Store Connect: https://appstoreconnect.apple.com
- Cloudflare: https://dash.cloudflare.com
- Netlify: https://app.netlify.com
- Bing: https://www.bing.com/webmasters
