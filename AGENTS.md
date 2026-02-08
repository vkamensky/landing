---
tags:
  - agents
area: data-master
owner: Vlad Kamensky
status: active
last_updated: 2026-01-27
refs:
  - "[[file naming convention]]"
---
# DataMaster.PRO — Landing Page / Agents

## Обзор

Лендинг DataMaster.PRO (data-master) — главная страница для персонального бренда и консалтинга по управлению данными и ИИ. Один HTML, CSS-переменные, vanilla JS. Публикуется на GitHub Pages через папку `docs/`.

---

## Для агентов: ключевые правила

### 1. Работаем напрямую с docs/

**Упрощённая структура** — редактируем файлы прямо в `docs/`, которая публикуется на GitHub Pages.

- **`docs/`** — единственная рабочая папка с `index.html`, `assets/`, `CNAME`
- Коммитим изменения в git сразу после редактирования
- Никаких промежуточных скриптов или папок

### 2. Workflow обновления

1. Редактировать файлы в `docs/` (index.html, assets/)
2. Закоммитить: `git add docs/` → `git commit` → `git push`
3. GitHub Pages автоматически обновится через 1-2 минуты

### 3. Hero-блок: утверждённый контент и стили

**Текст (не менять без согласования):**

- **h1:** «Помогаю людям и командам стать эффективней»
- **CTA блоки:** «ВНЕДРЯЮ ИИ», «ОБУЧАЮ РАБОТЕ С ИИ», «ЭФФЕКТИВНОСТЬ 2.0»

**Стили и цвета:**

- Тёмный фон: `#0A0A12`
- Акцентный цвет: `#1D7A74` (teal)
- Светлая схема для остальных секций: `#F5F5F7`, `#F0F0F5`

**Лейаут hero:** фото слева (flex: 1), контент справа (width: 700px) с тёмным фоном

---

## Локальный просмотр

Открыть в браузере: `docs/index.html`

---

## Структура репозитория

```
DataMaster.PRO main landing page {data-master}/
├── AGENTS.md
├── .gitignore
└── docs/                    # Рабочая папка (коммитим). GitHub Pages → /docs
    ├── index.html           # Главная страница
    ├── assets/              # Изображения, стили
    │   ├── vlad-photo.jpeg
    │   ├── master-logo-white2.jpg
    │   ├── master-logo-dark.jpg
    │   ├── logo-big.jpg
    │   ├── second-brain.jpg
    │   ├── shiva.jpg
    │   └── ai-acceleration.jpg
    └── CNAME                # Домен (если есть)
```

---

## Troubleshooting

**Сайт не обновляется:** подождать 1–2 минуты (кеш GitHub Pages); проверить, что закоммичена папка `docs/`; убедиться, что Settings → Pages → Folder = `/docs`.

**Изображения не загружаются:** проверить пути в HTML (`assets/имя-файла.jpg`); убедиться, что файлы закоммичены в `docs/assets/`.

---

## Полезные команды

```bash
# Проверить статус
git status

# Посмотреть изменения
git diff docs/

# Добавить все изменения в docs
git add docs/

# Закоммитить
git commit -m "Обновлен дизайн лендинга"

# Отправить на GitHub
git push
```
