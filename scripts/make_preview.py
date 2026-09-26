#!/usr/bin/env python3
"""Wrap a content-region HTML fragment in a Notre Dame Web Theme v4 page shell
so it can be previewed in a browser before pasting into Conductor.

Usage:
    python3 make_preview.py fragment.html -o preview.html \
        [--title "Page Title"] [--site "Site Name"] [--full-width]

The preview loads the production theme CSS/JS from conductor.nd.edu and inlines
the icon/sticker sprites, so components render exactly as they will on a live
Conductor site (needs network access when opened in a browser).
"""
import argparse, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, '..', 'assets')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('fragment', help='HTML fragment file (content-region markup)')
    ap.add_argument('-o', '--output', default='preview.html')
    ap.add_argument('--title', default='Page Title')
    ap.add_argument('--site', default='Notre Dame Site')
    ap.add_argument('--full-width', action='store_true',
                    help='render as a full-width page (for pages using full-bleed sections)')
    args = ap.parse_args()

    fragment = open(args.fragment).read()
    template = open(os.path.join(ASSETS, 'preview-template.html')).read()
    sprites = ''
    for name in ('icons-nd-base.svg', 'stickers-nd-base.svg'):
        path = os.path.join(ASSETS, name)
        if os.path.exists(path):
            sprites += '<div hidden>' + open(path).read() + '</div>\n'

    page_class = 'page--full-width' if args.full_width else ''
    html = (template
            .replace('{{TITLE_LENGTH}}', str(len(args.title)))
            .replace('{{TITLE}}', args.title)
            .replace('{{SITE_TITLE}}', args.site)
            .replace('{{PAGE_CLASS}}', page_class)
            .replace('{{SPRITES}}', sprites)
            .replace('{{CONTENT}}', fragment))
    open(args.output, 'w').write(html)
    print(f'wrote {args.output}')

if __name__ == '__main__':
    main()
