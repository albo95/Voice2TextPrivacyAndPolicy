#!/usr/bin/env python3
"""Aggiunge (o rimuove) i parametri di campagna App Store Connect a tutti i link
apps.apple.com del sito, così App Analytics attribuisce i download al sito, per
lingua e per pagina. Idempotente.

Uso:
  python3 scripts/campaign_links.py <PROVIDER_TOKEN>   # pt= dal link creato in App Store Connect
  python3 scripts/campaign_links.py --remove

Il "provider token" (pt) si ottiene in App Store Connect → App Analytics →
Campagne (Campaign links) → crea link: nell'URL generato c'è ?pt=XXXXXX&ct=...&mt=8.
Il campaign token (ct) lo assegna questo script: site-<lingua>-<pagina>, es.
site-it-home, site-de-transcribe-whatsapp, site-en-legal."""
import os, re, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from i18n import ROOT, LOCALES, GUIDES  # noqa: E402

RX = re.compile(r'(href="https://apps\.apple\.com/[^"?]*id6618147237)(\?[^"]*)?"')


def page_ident(rel):
    """(locale, page) da un percorso relativo tipo 'de/anleitungen/<slug>/index.html'."""
    parts = rel.split(os.sep)
    locale = 'it'
    for loc, L in LOCALES.items():
        if L['dir'] and parts[0] == L['dir']:
            locale = loc
            parts = parts[1:]
            break
    if parts == ['index.html']:
        return locale, 'home'
    if parts[0] in ('privacy-policy', 'terms-of-use'):
        return 'en', 'legal'
    if parts[0] == '404.html':
        return 'en', '404'
    if len(parts) == 3 and parts[0] == LOCALES[locale]['guides']:
        for key, slugs in GUIDES.items():
            if slugs.get(locale) == parts[1]:
                return locale, key
    return locale, parts[0]


def main():
    if len(sys.argv) != 2:
        print(__doc__); sys.exit(2)
    remove = sys.argv[1] == '--remove'
    pt = sys.argv[1]
    if not remove and not re.fullmatch(r'[0-9]+', pt):
        print('Il provider token (pt) è numerico, es. 123456789'); sys.exit(2)
    n_files = n_links = 0
    for dirpath, _, files in os.walk(ROOT):
        if '.git' in dirpath:
            continue
        for f in files:
            if not f.endswith('.html'):
                continue
            p = os.path.join(dirpath, f)
            rel = os.path.relpath(p, ROOT)
            locale, page = page_ident(rel)
            ct = f'site-{locale}-{page}'
            s = open(p, encoding='utf-8').read()

            def repl(m):
                if remove:
                    return m.group(1) + '"'
                return f'{m.group(1)}?pt={pt}&ct={ct}&mt=8"'
            s2, n = RX.subn(repl, s)
            if s2 != s:
                open(p, 'w', encoding='utf-8').write(s2)
                n_files += 1
            n_links += n
    print(f'{"rimossi" if remove else "aggiornati"} {n_links} link in {n_files} file')


if __name__ == '__main__':
    main()
