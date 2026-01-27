# DataMaster.PRO — лендинг

Лендинг консалтинга по автоматизации и управлению данными для enterprise.

## Структура

- `website_output/` — **исходник для выкладки в git** (отсюда публикуем)
  - `index.html` — главная страница (встроенные CSS и JS)
  - `assets/` — логотип, изображения
- Дизайн и идея сборки: см. `{data-master} {note} Дизайн лендинга и сборка – 2026-01-27 – Cursor.md`

## Локальный просмотр

Откройте в браузере: `website_output/index.html`

## Публикация на GitHub Pages

1. Создайте репозиторий (например `datamaster-pro`).
2. В Settings → Pages: Source = Deploy from a branch, Branch = main, **Folder = `/website_output`**.
3. Коммитьте и пушьте папку `website_output/` в репозиторий.
4. Сайт будет доступен: `https://<user>.github.io/datamaster-pro/` (GitHub отдаёт `index.html` из корня выбранной папки).

## Идея сборки

Заимствована из проекта [DataMaster.PRO AI course](../DataMaster.PRO%20AI%20course%20%7Bai-course%7D): один HTML без сборщиков, CSS-переменные, vanilla JS. Работаем напрямую в `website_output/`; при необходимости можно добавить скрипт, который копирует в `website_output/` выбранную версию из отдельных файлов (например `data-master-v1.html`).
