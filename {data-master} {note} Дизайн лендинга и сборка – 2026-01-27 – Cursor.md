---
tags:
  - design
  - landing
  - data-master
date: 2026-01-27
refs:
  - "[[{data-master} {note} Интро – 2026-01-18 – Cursor]]"
  - "[[{data-master}{note} Кейсы автоматизации DataMaster.PRO 2026-01-27]]"
  - "[[skills/frontend-design]]"
area: DataMaster.PRO main landing page
---

# Дизайн лендинга DataMaster.PRO и идея сборки

Идея сборки веб-страницы заимствована из [[40 project/DataMaster.PRO AI course {ai-course}|ai-course]].

---

## 1. Идея сборки (из ai-course)

### Структура проекта

```
DataMaster.PRO main landing page {data-master}/
├── website_output/          ← откуда выкладываем в git (публикуем)
│   ├── index.html          ← единая страница, встроенные CSS + JS
│   └── assets/              ← логотип, изображения
│       ├── logo.png
│       └── logo-big.png
├── generate_landing_for_pages.py   ← опционально: копирование версии в website_output/
├── README.md
└── ... (заметки, кейсы, интро)
```

### Принципы

| Элемент | Реализация |
|--------|------------|
| **HTML** | Один `index.html` со встроенными `<style>` и `<script>`. Без сборщиков (Vite/Webpack). |
| **Стили** | CSS-переменные в `:root` (цвета, тени, spacing, `--container-max-width`). |
| **Скрипты** | Vanilla JS: навигация при скролле, мобильное меню, плавная прокрутка, IntersectionObserver для анимаций. |
| **Ассеты** | `website_output/assets/` — только необходимые изображения. |
| **Публикация** | Коммитим `website_output/` в git. GitHub Pages: Source = branch `main`, **Folder = `/website_output`**. |

### Опциональный скрипт генерации

Если появятся версионированные исходники (например `data-master-v1.html` в отдельной папке), скрипт по аналогии с ai-course может:

- искать последнюю версию `data-master-v*.html`;
- копировать её в `website_output/index.html`;
- копировать `assets/` в `website_output/assets/`.

Пока можно обходиться прямой правкой `website_output/index.html`.

### GitHub Pages

- Репозиторий, например: `datamaster-pro` или `datamaster-landing`.
- URL: `https://vkamensky.github.io/datamaster-pro/` (или аналог).

---

## 2. Дизайн-концепция

Руководствуюсь [[skills/frontend-design]]: избегать «AI slop», выбрать смелое, узнаваемое направление.

### Контекст

- **Продукт:** DataMaster.PRO — консалтинг по автоматизации и управлению данными для enterprise.
- **Аудитория:** первые лица, руководители, ИТ-директора. B2B.
- **Контент:** интро (Владислав Каменский, Юниверс Дата), 10 кейсов с метриками, акцент на измеримых результатах.

### Выбранное направление: Editorial + Industrial

- **Editorial:** чёткая иерархия, много «воздуха», опора на заголовки и структуру. Текст и цифры — главные.
- **Industrial:** ощущение «инженерии», системности, без лишнего декора. Сетка, чёткие блоки, сдержанная палитра.

Итого: серьёзный, корпоративный, но не скучный. Запоминается за счёт типографики и одного яркого акцента.

### Типографика

- **Заголовки:** шрифт с характером, не Inter/Roboto. Варианты:
  - **Manrope** (geometric, современный) или **Plus Jakarta Sans**.
  - Для более «документального» тона: **Literata** или **Source Serif 4**.
- **Основной текст:** нейтральный sans, хорошо читаемый: **DM Sans**, **Source Sans 3**.
- **Кириллица:** все шрифты — с поддержкой кириллицы (Google Fonts / local).

Предпочтение: **Plus Jakarta Sans** (заголовки) + **Source Sans 3** (текст) — контраст и читаемость.

### Цвета

Избегать: фиолетовые градиенты, типичные «AI»-схемы.

| Роль | Вариант A (холодный) | Вариант B (тёплый акцент) |
|------|----------------------|----------------------------|
| **Фон** | `#fafbfc` / `#ffffff` | `#fafbfc` / `#ffffff` |
| **Текст** | `#0f172a`, `#334155`, `#64748b` | то же |
| **Акцент** | `#0d9488` (teal), `#06b6d4` (cyan) | `#ea580c` (оранжевый), `#dc2626` (красный) |
| **Hero / акцентный блок** | `#0f172a` → `#1e293b` | `#1c1917` → `#292524` |
| **Границы** | `#e2e8f0`, `#cbd5e1` | то же |

Рекомендация: **вариант A** — teal/cyan ассоциируется с данными, потоками, «цифрой». Один акцент (`--accent: #0d9488`), остальное — нейтральные.

### Компоненты и секции

| Секция | Описание | Компоненты из ai-course |
|--------|----------|--------------------------|
| **Navbar** | Логотип, якорные ссылки (О нас, Кейсы, Услуги, Контакт), CTA. | `navbar`, `nav-links`, `cta-button`, `mobile-menu-toggle` |
| **Hero** | Сильный заголовок, подзаголовок, один CTA. Без перегруза. | `hero`, `hero-content`, `btn-primary` |
| **О компании / Эксперт** | Краткий блок про Владислава Каменского и Юниверс Дату. | `section`, `two-columns` или `section-description` |
| **Кейсы** | 3–6 карточек с «Проблема → Решение → Результат» и метриками. Остальное — по ссылке «все кейсы» или раскрытие. | `cards-grid`, `card` |
| **Направления / Услуги** | 3–4 блока: автоматизация, данные, ИИ, аналитика. | `cards-grid`, `card` или `weeks-grid` |
| **Почему мы / Цифры** | 2–4 ключевые метрики (годы на рынке, проекты, отрасли). | `highlight-box` или компактная сетка |
| **CTA** | Одна кнопка/форма: «Обсудить проект», «Связаться». | `footer` или отдельный блок `highlight-box` |
| **Footer** | Контакты, соцсети (TG), копирайт. | `footer` |

### Сетка и отступы

- Базовая единица: **8px**. Шкала: `--space-xs: 8px` … `--space-4xl: 96px`.
- Контейнер: `--container-max-width: 1200px`, `--container-padding: var(--space-lg)`.
- Секции: `padding: var(--space-3xl) var(--container-padding)`.

### Анимации

- Лёгкие: появление при скролле (`fade-in`, `slide-in-left/right`), `transition` для hover.
- Без тяжёлых анимаций на первом экране — быстрая загрузка и фокус на контенте.

### Фоны и детали

- Hero: тёмный градиент + тонкий grid/pattern (как в ai-course) или минимальный шум.
- Карточки: белый фон, тень, при hover — лёгкий `translateY` и `box-shadow`.
- `section-alt` с `--light-bg` для чередования.

---

## 3. Заимствованные блоки из ai-course

Переиспользуем структуру и классы (названия можно слегка поменять под контент):

- `:root` — переменные цветов, теней, spacing, `--transition`, `--container-*`.
- `navbar`, `nav-container`, `logo`, `nav-links`, `mobile-menu-toggle`, `mobile-menu`.
- `hero`, `hero-content`, `btn-primary`, `btn-secondary`.
- `section`, `section-alt`, `section-title`, `section-subtitle`, `section-description`.
- `cards-grid`, `card`.
- `features-list`, `numbered-list`.
- `two-columns`, `highlight-box`.
- `footer`, `footer-content`.
- `scroll-top`, `fade-in`, `slide-in-*`, `scale-in`.
- JS: скролл navbar, мобильное меню, плавные якоря, IntersectionObserver для анимаций.

---

## 4. Отличия от ai-course (чтобы не копировать 1:1)

| Аспект | ai-course | DataMaster.PRO |
|--------|-----------|----------------|
| **Тема** | Курс, продуктивность, ИИ, «от хаоса к системе» | Консалтинг, автоматизация, данные, enterprise |
| **Цвета** | Purple–blue–teal градиенты | Уголь + teal/cyan, без purple |
| **Шрифты** | Inter | Plus Jakarta Sans + Source Sans 3 |
| **Hero** | «Прокачай продуктивность», два подзаголовка с цветовыми акцентами | Один сильный заголовок про данные/автоматизацию, один CTA |
| **Карточки** | Недели, инструменты, форматы | Кейсы (проблема–решение–результат), направления услуг |
| **Цены** | Есть (Интенсив/Лайт) | Нет на лендинге или «по запросу» |
| **Футер** | «От хаоса к системе», призыв | Контакты, TG, «Обсудить проект» |

---

## 5. Следующие шаги

1. ~~Создать `website_output/` и `website_output/assets/`~~ — сделано. Черновой `website_output/index.html` и `README.md` созданы.
2. ~~Перенести в `website_output/index.html` скелет~~ — сделано: `:root` (палитра уголь + teal), Plus Jakarta Sans + Source Sans 3, navbar, hero, «О нас», «Кейсы» (3 карточки + highlight), footer, мобильное меню, scroll-top, IntersectionObserver.
3. ~~Подключить шрифты и палитру~~ — в скелете уже есть.
4. Заполнить контент: интро из [[{data-master} {note} Интро – 2026-01-18 – Cursor]], 3–6 кейсов из [[{data-master}{note} Кейсы автоматизации DataMaster.PRO 2026-01-27]].
5. Добавить логотип/бренд в `website_output/assets/` (при наличии).
6. При необходимости — `generate_landing_for_pages.py` (копирование версии в `website_output/`).
7. Настроить репозиторий и GitHub Pages (Folder = `/website_output`).

---

## 6. Ссылки

- [[40 project/DataMaster.PRO AI course {ai-course}/docs/index.html]] — эталон вёрстки (у ai-course вывод в `docs/`; у нас — в `website_output/`).
- [[40 project/DataMaster.PRO AI course {ai-course}/README.md]] — описание генерации и GitHub Pages.
- [[40 project/DataMaster.PRO AI course {ai-course}/SETUP.md]] — настройка Git и Pages. Для DataMaster.PRO: Folder = `/website_output`.
