#!/bin/bash
# Script exécuté par Vercel lors du build

echo "==> Installation des dépendances..."
pip install -r requirements.txt

echo "==> Collecte des fichiers statiques..."
python manage.py collectstatic --noinput

echo "==> Application des migrations..."
python manage.py migrate --noinput

echo "==> Build terminé ✓"
