# 🚀 Guide de déploiement — Prince Vision sur Vercel + PostgreSQL

## Ce que contient ce dossier

Ce dossier est votre site **prêt à déployer**. Les fichiers ajoutés/modifiés :

| Fichier | Rôle |
|---|---|
| `requirements.txt` | Dépendances Python pour la production |
| `vercel.json` | Configuration Vercel |
| `build_files.sh` | Script de build (migrations + static) |
| `teopicture/settings.py` | Settings mis à jour (PostgreSQL, WhiteNoise, Cloudinary) |
| `.env.example` | Variables d'environnement à configurer |
| `.gitignore` | Fichiers à exclure de Git |

---

## Étape 1 — Créer un compte Vercel

1. Aller sur [vercel.com](https://vercel.com) → **Sign Up**
2. Se connecter avec GitHub (recommandé)

---

## Étape 2 — Créer un compte GitHub et pousser le code

```bash
# Dans le dossier prince-vision-deploy/
git init
git add .
git commit -m "Initial commit — Prince Vision"

# Créer un repo sur github.com puis :
git remote add origin https://github.com/VOTRE_USER/prince-vision.git
git push -u origin main
```

---

## Étape 3 — Créer la base de données PostgreSQL

### Option A : Vercel Postgres (le plus simple)
1. Dashboard Vercel → **Storage** → **Create Database** → **Postgres**
2. Nommer la base (ex: `prince-vision-db`)
3. Vercel génère automatiquement la variable `DATABASE_URL`

### Option B : Neon.tech (gratuit, recommandé)
1. Aller sur [neon.tech](https://neon.tech) → **Sign Up** gratuit
2. **New Project** → Région : `eu-west-1` (Europe, proche du Sénégal)
3. Copier la **Connection string** qui ressemble à :
   ```
   postgres://user:password@ep-xxx.eu-west-1.aws.neon.tech/neondb?sslmode=require
   ```

---

## Étape 4 — Déployer sur Vercel

1. Dashboard Vercel → **Add New Project** → Importer votre repo GitHub
2. **Framework Preset** : Other
3. **Root Directory** : laisser vide (ou `.`)
4. Cliquer **Deploy** (il va échouer la première fois sans les variables — c'est normal)

---

## Étape 5 — Configurer les variables d'environnement

Dans Vercel → votre projet → **Settings** → **Environment Variables**, ajouter :

| Variable | Valeur |
|---|---|
| `SECRET_KEY` | Générer sur [djecrety.ir](https://djecrety.ir) |
| `DEBUG` | `False` |
| `DATABASE_URL` | La connection string PostgreSQL (Neon ou Vercel Postgres) |
| `ALLOWED_HOSTS` | `*.vercel.app` |
| `CSRF_TRUSTED_ORIGINS` | `https://VOTRE-PROJET.vercel.app` |
| `CLOUDINARY_CLOUD_NAME` | (voir Étape 6) |
| `CLOUDINARY_API_KEY` | (voir Étape 6) |
| `CLOUDINARY_API_SECRET` | (voir Étape 6) |

Après avoir tout ajouté → **Redeploy**

---

## Étape 6 — Cloudinary pour les photos (optionnel mais recommandé)

Vercel n'a pas de stockage de fichiers persistant. Sans Cloudinary, les photos que vous uploadez via l'admin seront perdues à chaque redéploiement.

1. Créer un compte gratuit sur [cloudinary.com](https://cloudinary.com)
2. Dashboard → copier **Cloud Name**, **API Key**, **API Secret**
3. Les ajouter comme variables d'environnement sur Vercel

---

## Étape 7 — Créer le superutilisateur admin

Après le premier déploiement réussi, dans votre terminal local :

```bash
# Installer les dépendances localement
pip install -r requirements.txt

# Configurer les variables d'env localement (créer un fichier .env)
cp .env.example .env
# Éditer .env avec vos vraies valeurs

# Créer le superuser
python manage.py createsuperuser
```

Ou via Vercel CLI :
```bash
npm i -g vercel
vercel login
vercel env pull .env.local
python manage.py createsuperuser
```

---

## Accès au site déployé

| Page | URL |
|---|---|
| Site principal | `https://VOTRE-PROJET.vercel.app/` |
| Portfolio | `https://VOTRE-PROJET.vercel.app/portfolio/` |
| Réservations | `https://VOTRE-PROJET.vercel.app/reservation/` |
| Dashboard admin | `https://VOTRE-PROJET.vercel.app/admin-dashboard/` |
| Admin Django | `https://VOTRE-PROJET.vercel.app/django-admin/` |

---

## ⚠️ Points importants

- **Ne jamais committer le fichier `.env`** — il contient vos secrets
- **DEBUG doit être `False`** en production
- Les migrations sont appliquées automatiquement lors du build (`build_files.sh`)
- Si vous avez des données dans SQLite à migrer vers PostgreSQL, contactez-moi

---

## Problèmes courants

**Erreur 500 au démarrage** → Vérifier que `DATABASE_URL` est bien configurée dans Vercel

**Static files introuvables** → S'assurer que `build_files.sh` s'est bien exécuté dans les logs Vercel

**CSRF error sur les formulaires** → Ajouter votre domaine dans `CSRF_TRUSTED_ORIGINS`
