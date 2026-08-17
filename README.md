
# Gerardo's Italian Bakery — Full Stack Website

A full Django e-commerce website for **Gerardo's Italian Bakery**. The content, products,
history and locations belong to Gerardo's Italian Bakery; the information architecture,
navigation and editorial visual direction are inspired by premium artisan-bakery digital
experiences (large photography, generous white space, editorial typography) — reinterpreted
here for Gerardo's own identity.

---

## Stack

- Python 3.12+ / Django 5+
- Django ORM, Django Templates, Django Admin, Django Forms, Django Messages
- SQLite for local development (PostgreSQL-ready)
- HTML5, CSS3 (Grid + Flexbox + CSS Variables), vanilla JavaScript ES6+
- No frontend frameworks (no React/Vue/Angular), no Bootstrap/Tailwind/jQuery

## Project structure

```text
gerardos_bakery/
├── manage.py
├── requirements.txt
├── .env.example
├── config/            # Django project settings, urls, wsgi/asgi
├── core/              # Story, locations, contact, cake tastings, recipes, search, newsletter
├── shop/              # Categories, products, product images
├── cart/              # Session-based cart + checkout
├── templates/         # base.html, components/, core/, shop/, cart/
├── static/             # css/, js/, images/
└── media/products/    # Uploaded product images (created by Django Admin)
```

---

## 1. Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Copy the environment file and adjust as needed (the defaults work out of the box for local
development with SQLite):

```bash
cp .env.example .env
```

## 2. Database setup

```bash
python manage.py migrate
```

Load starter content (the three Gerardo's locations, shop categories, cake flavors, a small
set of sample products and a few kitchen stories) so the site isn't empty on first run:

```bash
python manage.py seed_data
```

Create an admin user:

```bash
python manage.py createsuperuser
```

## 3. Run the site

```bash
python manage.py runserver
```

- Site: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 4. Run tests

```bash
python manage.py test
```

---

## Using the Django Admin

Log in at `/admin/` with the superuser account you created.

### Add or edit a product
`Shop → Products → Add product`. Set name, category, price, stock, and upload an image.
Toggle **Featured** or **Best seller** to control where it appears on the homepage. Uncheck
**Active** to hide a product without deleting it.

### Change a price or photo
Open the product in `Shop → Products`, update the **Price** field or replace the **Image**,
then save. Changes appear immediately on the site — no restart required.

### Add a store location
`Bakery Content → Locations → Add location`. Fill in the address, phone number and opening
hours (one line per day range, e.g. `Sunday-Wednesday: 8:00 am - 8:00 pm`). Add a Grubhub (or
other) link in **Order online url** to have it appear on the Order Online page.

### Add a cake flavor
`Bakery Content → Cake flavors → Add cake flavor`. Check **Is tasting option** to have it show
up on the Cake Tastings page as well as the general Wedding Cakes flavor list.

### Add a recipe / kitchen story
`Bakery Content → Recipes → Add recipe`. The **Description** field is the short teaser shown
on cards; **Content** is the full article body. Check **Featured** to promote it on the homepage.

### Update contact information
Store phone numbers, addresses and hours all live on the **Location** model — update them
there rather than in the templates, so the same information stays in sync everywhere it's
displayed on the site.

### Review form submissions
- `Bakery Content → Cake Tasting Requests` — tasting requests from the Cake Tastings page.
- `Bakery Content → Contact Messages` — messages from the Contact page.
- `Bakery Content → Newsletter Subscribers` — newsletter sign-ups.

Mark items **Handled** once you've followed up.

---

## Switching to PostgreSQL

1. Install the PostgreSQL driver:
   ```bash
   pip install psycopg2-binary
   ```
2. In `.env`, set:
   ```env
   DB_ENGINE=django.db.backends.postgresql
   DB_NAME=gerardos_bakery
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
   ```
3. Re-run migrations against the new database:
   ```bash
   python manage.py migrate
   python manage.py seed_data
   ```

## Configuring `.env`

All environment-specific values (secret key, debug flag, allowed hosts, database credentials,
email settings) are read from a `.env` file via `python-decouple`. Never commit your real
`.env` file — `.env.example` documents every variable it needs.

For production, at minimum:
- Set `DEBUG=False`
- Set a strong, unique `SECRET_KEY`
- Set `ALLOWED_HOSTS` to your real domain(s)
- Point `DB_ENGINE`/`DB_*` at PostgreSQL
- Configure real `EMAIL_*` settings if you want contact-form/newsletter notifications

## Payments

Checkout currently records the order and clears the cart without processing a real payment.
The `cart/views.py:checkout` view and `cart/forms.py:CheckoutForm` are the place to wire in
Stripe, PayPal or Mercado Pago when you're ready to accept real payments.

## Notes on content

Business details (locations, phone numbers, hours, cake flavors, founding story) reflect
Gerardo's Italian Bakery's own public information and are stored as data in the `core` app
models — not hard-coded in templates — so they can be updated at any time from the Django
Admin without touching code.
=======
# padaria-front
 b7fe708b4c4a1399b614eabb5acae3c4dbe5d226
