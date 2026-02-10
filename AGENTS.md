---
tags:
  - agents
area: data-master
owner: Vlad Kamensky
status: active
last_updated: 2026-02-08
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

**GitHub Pages:**
1. Редактировать файлы в `docs/` (index.html, assets/)
2. Закоммитить: `git add docs/` → `git commit` → `git push`
3. GitHub Pages автоматически обновится через 1-2 минуты

**REG.ru (дублирование на хостинг):** см. раздел [Выкладка на REG.ru](#выкладка-на-regru-sftp) ниже.

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

## Выкладка на REG.ru (SFTP)

Сайт дублируется на хостинг REG.ru через SFTP (доступ: панель ISPmanager, SSH, SFTP).

**Данные:**
- **Хост:** `server15.hosting.reg.ru`
- **Логин:** `u3408190`
- **Путь на сервере:** `www/data-master.pro/` (относительно домашней папки, без ведущего слеша)
- **Пароль:** не хранить в репозитории; вводить по запросу при выполнении команд.

**Порядок действий:**

1. Перейти в папку проекта:
   ```bash
   cd "/Users/vladkamensky/Yandex.Disk.localized/Obsidian Vault/40 project/DataMaster.PRO main landing page {data-master}"
   ```

2. Если каталог на сервере ещё не создан — создать по SSH:
   ```bash
   ssh u3408190@server15.hosting.reg.ru "mkdir -p www/data-master.pro"
   ```

3. Загрузить содержимое `docs/` (index.html, CNAME, assets/):
   ```bash
   scp -r docs/* u3408190@server15.hosting.reg.ru:www/data-master.pro/
   ```
   По запросу ввести пароль от учётки.

**Важно:** использовать путь `www/data-master.pro/` без ведущего слеша — при SFTP домашняя директория пользователя является корнем, полный путь `/www/data-master.pro/` приведёт к ошибке «No such file or directory».

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
