# DataMaster.PRO — лендинг

Лендинг консалтинга по автоматизации и управлению данными для enterprise.

## Структура

- **`website_output/`** — внутренняя рабочая папка (не в git). Редактируем тут `index.html` и `assets/`.
- **`docs/`** — выкладка для GitHub Pages (в git). Содержимое копируется из `website_output/` скриптом.
- Дизайн и идея сборки: см. `{data-master} {note} Дизайн лендинга и сборка – 2026-01-27 – Cursor.md`

## Локальный просмотр

Откройте в браузере: `website_output/index.html` или после генерации — `docs/index.html`

## Публикация на GitHub Pages

1. Сгенерировать `docs/` из `website_output/`:
   ```bash
   python3 generate_landing_for_pages.py
   ```
2. Закоммитить и запушить:
   ```bash
   git add docs/
   git commit -m "Обновлен лендинг"
   git push
   ```
3. В Settings → Pages: Source = Deploy from a branch, Branch = main, **Folder = `/docs`**.
4. Сайт: `https://<user>.github.io/landing/` (или как назван репозиторий).

## Идея сборки

Заимствована из [DataMaster.PRO AI course](../DataMaster.PRO%20AI%20course%20%7Bai-course%7D): один HTML, CSS-переменные, vanilla JS. Работаем в `website_output/`; скрипт копирует в `docs/`; в git и на GitHub Pages — только `docs/`.
