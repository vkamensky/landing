#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Копирует содержимое website_output/ в docs/ для GitHub Pages.
website_output/ — внутренняя рабочая папка (не в git).
docs/ — то, что коммитим и откуда раздаёт GitHub Pages.
"""

import shutil
from pathlib import Path


def main():
    script_dir = Path(__file__).parent
    source = script_dir / "website_output"
    docs_dir = script_dir / "docs"

    print("🎯 ВЫКЛАДКА ЛЕНДИНГА: website_output → docs")
    print("=" * 50)
    print(f"📁 Источник: {source}")
    print(f"📁 Приёмник: {docs_dir}")

    if not source.exists():
        print(f"\n❌ Папка {source} не найдена.")
        return

    index_src = source / "index.html"
    if not index_src.exists():
        print(f"\n❌ {index_src} не найден.")
        return

    docs_dir.mkdir(exist_ok=True)

    # index.html
    shutil.copy2(index_src, docs_dir / "index.html")
    print(f"\n✅ index.html → docs/index.html")

    # assets/
    assets_src = source / "assets"
    if assets_src.exists() and assets_src.is_dir():
        assets_dest = docs_dir / "assets"
        if assets_dest.exists():
            shutil.rmtree(assets_dest)
        shutil.copytree(assets_src, assets_dest, ignore=shutil.ignore_patterns(".DS_Store", ".gitkeep"))
        print(f"✅ assets/ → docs/assets/")

    print(f"\n✅ Готово. Дальше:")
    print(f"   git add docs/")
    print(f"   git commit -m 'Обновлен лендинг'")
    print(f"   git push")
