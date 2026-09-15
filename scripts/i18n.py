#!/usr/bin/env python3
"""Rigenera per tutte le pagine tradotte: blocco hreflang, menu lingua a tendina,
<script src="/site.js"> e sitemap.xml. Idempotente. Uso:  python3 scripts/i18n.py
Per aggiungere una lingua o una guida: aggiornare LOCALES / GUIDES qui sotto."""
import os, re, sys, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE = 'https://matt-transcriber.netlify.app'
TODAY = datetime.date.today().isoformat()

# code -> dir (cartella, '' = root), guides (segmento URL delle guide), hreflang (lista), flag, name, short, label (aria)
LOCALES = {
    'it':     dict(dir='',       guides='guide',       hreflang=['it'],            flag='🇮🇹', name='Italiano',                short='IT',    label='Lingua'),
    'en':     dict(dir='en',     guides='guides',      hreflang=['en', 'x-default'], flag='🇬🇧', name='English',               short='EN',    label='Language'),
    'fr':     dict(dir='fr',     guides='guides',      hreflang=['fr'],            flag='🇫🇷', name='Français',                short='FR',    label='Langue'),
    'de':     dict(dir='de',     guides='anleitungen', hreflang=['de'],            flag='🇩🇪', name='Deutsch',                 short='DE',    label='Sprache'),
    'es':     dict(dir='es',     guides='guias',       hreflang=['es', 'es-ES'],   flag='🇪🇸', name='Español (España)',        short='ES',    label='Idioma'),
    'es-419': dict(dir='es-419', guides='guias',       hreflang=['es-419'],        flag='🇲🇽', name='Español (Latinoamérica)', short='ES-LA', label='Idioma'),
    'pt-br':  dict(dir='pt-br',  guides='guias',       hreflang=['pt-BR', 'pt'],   flag='🇧🇷', name='Português (Brasil)',      short='PT-BR', label='Idioma'),
}

# chiave guida -> slug per lingua
GUIDES = {
    'transcribe-whatsapp': dict(it='trascrivere-vocali-whatsapp', en='transcribe-whatsapp-voice-messages', fr='transcrire-vocaux-whatsapp', de='whatsapp-sprachnachrichten-transkribieren', es='transcribir-audios-whatsapp'),
    'convert':             dict(it='convertire-vocali-whatsapp-in-testo', en='convert-whatsapp-voice-message-to-text', fr='convertir-vocal-whatsapp-en-texte', de='whatsapp-sprachnachricht-in-text-umwandeln', es='convertir-audio-whatsapp-en-texto'),
    'read-silently':       dict(it='leggere-vocali-whatsapp-senza-ascoltarli', en='read-whatsapp-voice-messages-without-listening', fr='lire-vocaux-whatsapp-sans-ecouter', de='whatsapp-sprachnachrichten-lesen-ohne-anhoeren', es='leer-audios-whatsapp-sin-escuchar'),
    'summarize':           dict(it='riassumere-vocali-whatsapp', en='summarize-whatsapp-voice-messages', fr='resumer-vocaux-whatsapp', de='whatsapp-sprachnachrichten-zusammenfassen', es='resumir-audios-whatsapp'),
    'translate':           dict(it='tradurre-vocali-whatsapp', en='translate-whatsapp-voice-messages', fr='traduire-vocaux-whatsapp', de='whatsapp-sprachnachrichten-uebersetzen', es='traducir-audios-whatsapp'),
    'telegram':            dict(it='trascrivere-vocali-telegram', en='transcribe-telegram-voice-messages', fr='transcrire-vocaux-telegram', de='telegram-sprachnachrichten-transkribieren', es='transcribir-audios-telegram'),
    'audio-files':         dict(it='trascrivere-audio-in-testo-iphone', en='transcribe-audio-to-text-iphone', fr='transcrire-audio-en-texte-iphone', de='audio-in-text-umwandeln-iphone', es='transcribir-audio-a-texto-iphone'),
}
for k, v in GUIDES.items():
    v.setdefault('es-419', dict(**{
        'transcribe-whatsapp': 'transcribir-notas-de-voz-whatsapp', 'convert': 'convertir-nota-de-voz-whatsapp-a-texto',
        'read-silently': 'leer-notas-de-voz-whatsapp-sin-escuchar', 'summarize': 'resumir-notas-de-voz-whatsapp',
        'translate': 'traducir-notas-de-voz-whatsapp', 'telegram': 'transcribir-notas-de-voz-telegram',
        'audio-files': 'transcribir-audio-a-texto-en-iphone'})[k])
    v.setdefault('pt-br', dict(**{
        'transcribe-whatsapp': 'transcrever-audios-whatsapp', 'convert': 'converter-audio-whatsapp-em-texto',
        'read-silently': 'ler-audios-whatsapp-sem-ouvir', 'summarize': 'resumir-audios-whatsapp',
        'translate': 'traduzir-audios-whatsapp', 'telegram': 'transcrever-audios-telegram',
        'audio-files': 'transcrever-audio-em-texto-iphone'})[k])

LEGAL = ['/privacy-policy/', '/terms-of-use/']


def url_for(locale, key):
    L = LOCALES[locale]
    d = ('/' + L['dir']) if L['dir'] else ''
    if key == 'home':
        return d + '/'
    return f"{d}/{L['guides']}/{GUIDES[key][locale]}/"


def path_for(locale, key):
    return os.path.join(ROOT, url_for(locale, key).lstrip('/'), 'index.html')


def hreflang_block(key):
    lines = []
    for loc, L in LOCALES.items():
        if not os.path.exists(path_for(loc, key)):
            continue
        for h in L['hreflang']:
            lines.append(f'    <link rel="alternate" hreflang="{h}" href="{BASE}{url_for(loc, key)}">')
    # x-default per ultimo
    lines.sort(key=lambda l: 'x-default' in l)
    return '\n'.join(lines) + '\n'


def lang_menu(locale, key):
    L = LOCALES[locale]
    items = []
    for loc, M in LOCALES.items():
        if not os.path.exists(path_for(loc, key)):
            continue
        cur = ' aria-current="page"' if loc == locale else ''
        hl = M['hreflang'][0]
        items.append(f'<li><a href="{url_for(loc, key)}" hreflang="{hl}" lang="{hl}"{cur}>{M["flag"]} {M["name"]}</a></li>')
    return (f'<details class="lang-menu"><summary aria-label="{L["label"]}: {L["name"]}" title="{L["label"]}">'
            f'{L["flag"]} <span>{L["short"]}</span></summary><ul>' + ''.join(items) + '</ul></details>')


RX_HREFLANG = re.compile(r'(?:[ \t]*<link rel="alternate" hreflang="[^"]+" href="[^"]+">\n)+')
RX_SWITCH = re.compile(r'<div class="lang-switch".*?</div>|<details class="lang-menu">.*?</details>', re.S)


def process(locale, key):
    p = path_for(locale, key)
    s = open(p, encoding='utf-8').read()
    s, n1 = RX_HREFLANG.subn(lambda m: hreflang_block(key), s, count=1)
    s, n2 = RX_SWITCH.subn(lambda m: lang_menu(locale, key), s, count=1)
    if '/site.js' not in s:
        s = s.replace('<link rel="stylesheet" href="/style.css">', '<link rel="stylesheet" href="/style.css">\n    <script src="/site.js" defer></script>', 1)
    if n1 != 1 or n2 != 1:
        print(f'!! {p}: hreflang={n1} switch={n2}')
    open(p, 'w', encoding='utf-8').write(s)
    return n1 == 1 and n2 == 1


def sitemap():
    old = open(os.path.join(ROOT, 'sitemap.xml'), encoding='utf-8').read()
    prev = {m.group(1): (m.group(2), m.group(3)) for m in re.finditer(r'<loc>([^<]+)</loc>\s*<lastmod>([^<]+)</lastmod>\s*<priority>([^<]+)</priority>', old)}
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">', '']
    keys = ['home'] + list(GUIDES)
    for key in keys:
        alts = [(h, BASE + url_for(loc, key)) for loc, L in LOCALES.items() if os.path.exists(path_for(loc, key)) for h in L['hreflang']]
        alts.sort(key=lambda a: a[0] == 'x-default')
        for loc in LOCALES:
            if not os.path.exists(path_for(loc, key)):
                continue
            u = BASE + url_for(loc, key)
            lastmod, prio = prev.get(u, (TODAY, '1.0' if key == 'home' else '0.8'))
            out.append('  <url>')
            out.append(f'    <loc>{u}</loc>')
            out.append(f'    <lastmod>{lastmod}</lastmod>')
            out.append(f'    <priority>{prio}</priority>')
            for h, hu in alts:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{h}" href="{hu}"/>')
            out.append('  </url>')
        out.append('')
    for u in LEGAL:
        lastmod, prio = prev.get(BASE + u, (TODAY, '0.3'))
        out += ['  <url>', f'    <loc>{BASE}{u}</loc>', f'    <lastmod>{lastmod}</lastmod>', f'    <priority>{prio}</priority>', '  </url>']
    out += ['</urlset>', '']
    open(os.path.join(ROOT, 'sitemap.xml'), 'w', encoding='utf-8').write('\n'.join(out))


def main():
    ok = True; n = 0
    for key in ['home'] + list(GUIDES):
        for loc in LOCALES:
            if os.path.exists(path_for(loc, key)):
                ok &= process(loc, key); n += 1
    sitemap()
    print(f'pagine aggiornate: {n}; sitemap rigenerata')
    sys.exit(0 if ok else 1)


if __name__ == '__main__':
    main()
