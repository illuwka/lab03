# Звіт з лабораторної роботи № 03

**Студент:** Прадійчук Ілля Миколайович  
**Група:** ІПЗ-22  
**Команда:** LOQ Team — Прадійчук Ілля Миколайович (Teamlead), Завиднюк Влад Володимирович (Developer), Біскій Давид Анатолійович (QA).  
**Тема:** вебсайт-каталог скінів Counter-Strike 2 на Flask.      
**Посилання на репозиторій** https://github.com/illuwka/lab03 

## Мета роботи

Створити багатосторінковий вебзастосунок на Flask, оформити сторінки відповідно до теми проєкту та забезпечити навігацію й адаптивне відображення.

## Особистий внесок

Я створив початкову структуру репозиторію та шаблони сторінок, підготував головну сторінку й README, дописував спільну навігацію та оформлення. Окремо додав скриншоти сторінок у звичайному й мобільному вигляді.

Мої коміти в [репозиторії GitHub](https://github.com/illuwka/lab03):

- Початкова структура й документація: [`32a6d34`](https://github.com/illuwka/lab03/commit/32a6d34), [`dd97c81`](https://github.com/illuwka/lab03/commit/dd97c81), [`97e118e`](https://github.com/illuwka/lab03/commit/97e118e), [`d8805ca`](https://github.com/illuwka/lab03/commit/d8805ca), [`53a22cf`](https://github.com/illuwka/lab03/commit/53a22cf).
- Створення звітів і шаблонів сторінок: [`dd7de28`](https://github.com/illuwka/lab03/commit/dd7de28), [`207c05a`](https://github.com/illuwka/lab03/commit/207c05a), [`71b7359`](https://github.com/illuwka/lab03/commit/71b7359), [`1ae644b`](https://github.com/illuwka/lab03/commit/1ae644b), [`3fe5971`](https://github.com/illuwka/lab03/commit/3fe5971), [`f362df3`](https://github.com/illuwka/lab03/commit/f362df3), [`4393bb5`](https://github.com/illuwka/lab03/commit/4393bb5).
- Узгодження шапки, сторінки й посилань: [`b4b6ee3`](https://github.com/illuwka/lab03/commit/b4b6ee3), [`693661e`](https://github.com/illuwka/lab03/commit/693661e), [`84704a9`](https://github.com/illuwka/lab03/commit/84704a9), [`03aa684`](https://github.com/illuwka/lab03/commit/03aa684), [`d526c42`](https://github.com/illuwka/lab03/commit/d526c42).
- Додавання скриншотів: [`f502730`](https://github.com/illuwka/lab03/commit/f502730).

## Сторінки проєкту

У застосунку є сторінки «Головна», «Магазин», «Про нас» і «Зворотний зв’язок». Шаблони використовують спільний `base.html`; каталог показує зображення скінів, їхній стан і демонстраційні ціни. Проєкт має адаптивне відображення.

## Скріншоти

Скріншоти збережені в `lab-reports/screenshots/`. Зображення шириною 1920 px показують звичайний вигляд, шириною 512 px — мобільний.

### Головна

| Desktop | Mobile |
|---|---|
| ![Головна сторінка — desktop](<screenshots/Screenshot 2026-11-09 at 09-58-08 Головна — LOQ Market.png>) | ![Головна сторінка — mobile](<screenshots/Screenshot 2026-11-09 at 09-59-40 Головна — LOQ Market.png>) |

### Магазин

| Desktop | Mobile |
|---|---|
| ![Магазин — desktop](<screenshots/Screenshot 2026-11-09 at 09-58-21 CS2 Skin Shop.png>) | ![Магазин — mobile](<screenshots/Screenshot 2026-11-09 at 10-01-53 CS2 Skin Shop.png>) |

### Про нас

| Desktop | Mobile |
|---|---|
| ![Про нас — desktop](<screenshots/Screenshot 2026-11-09 at 09-58-28 Про нас.png>) | ![Про нас — mobile](<screenshots/Screenshot 2026-11-09 at 10-02-21 Про нас.png>) |

### Зворотний зв’язок

| Desktop | Mobile |
|---|---|
| ![Зворотний зв’язок — desktop](<screenshots/Screenshot 2026-11-09 at 09-58-35 Зворотний зв’язок.png>) | ![Зворотний зв’язок — mobile](<screenshots/Screenshot 2026-11-09 at 10-02-32 Зворотний зв’язок.png>) |

## Труднощі та їх вирішення

 - Під час узгодження сторінок виникла потреба підтримувати спільний вигляд навігації та оформлення. Для цього шапку винесено в базовий шаблон `base.html`, який наслідують сторінки; внутрішні переходи ведуть до відповідних маршрутів Flask. Адаптивність сторінок перевірено скриншотами у звичайному та мобільному форматах.

 - У репозиторій потрапили зайві файли (кеш, локальні налаштування) - додано та оновлено .gitignore

## Висновок

Під час лабораторної роботи створено багатосторінковий вебзастосунок про каталог скінів CS2 на Flask із шаблонами Jinja та спільною навігацією. Адаптивні сторінки дають змогу переглядати каталог і контактну інформацію як на комп’ютері, так і на смартфоні. Робота допомогла закріпити маршрутизацію Flask і повторне використання шаблонів.
