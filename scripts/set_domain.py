#!/usr/bin/env python3
"""Migra il sito a un nuovo dominio: sostituisce l'host in canonical, hreflang,
og:*, JSON-LD, robots.txt, sitemap e nel BASE di scripts/i18n.py, poi rigenera
hreflang/sitemap. Il vecchio host resta raggiungibile grazie al 301 automatico di
Netlify (NON cancellare il sito netlify.app: i link stampati nella descrizione
App Store puntano lì).

Uso:  python3 scripts/set_domain.py matttranscriber.com"""
import os, re, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import i18n  # noqa: E402

EXT = ('.html', '.xml', '.txt', '.py', '.md')
SKIP = {'GUIDA-SEO.md'}  # la guida spiega la migrazione citando il vecchio host


def main():
    if len(sys.argv) != 2 or not re.fullmatch(r'[a-z0-9.-]+\.[a-z]+', sys.argv[1]):
        print(__doc__); sys.exit(2)
    new = 'https://' + sys.argv[1]
    old = i18n.BASE
    if old == new:
        print('già su', new); return
    n_files = n_occ = 0
    for dirpath, _, files in os.walk(i18n.ROOT):
        if '.git' in dirpath:
            continue
        for f in files:
            if not f.endswith(EXT) or f in SKIP:
                continue
            p = os.path.join(dirpath, f)
            s = open(p, encoding='utf-8').read()
            if old not in s:
                continue
            n_occ += s.count(old); n_files += 1
            open(p, 'w', encoding='utf-8').write(s.replace(old, new))
    print(f'{old} -> {new}: {n_occ} occorrenze in {n_files} file')
    subprocess.run([sys.executable, os.path.join(i18n.ROOT, 'scripts', 'i18n.py')], check=True)
    print('\nDa fare a mano:\n'
          ' - Netlify: dominio aggiunto e impostato come primary (301 automatico dal netlify.app)\n'
          ' - App Store Connect: Marketing URL, Support URL, Privacy Policy URL\n'
          ' - Search Console: nuova proprietà Dominio + Cambio di indirizzo dalla vecchia\n'
          ' - Bing Webmaster: re-importa da Search Console\n'
          ' - Link nei profili social / directory / YouTube')


if __name__ == '__main__':
    main()
