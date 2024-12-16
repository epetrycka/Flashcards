# Flashcards
I am developing a web application designed for playing and studing with flashcards. This application is aim to provide an engaging and interactive experience as they learn and review various subjects.

In the future, I plan to expand this project by creating a Windows application that will seamlessly integrate with the web application, allowing users to access their flashcards and progress across different platforms.

Files structure
project-root/

├── client/                  # Frontend (React + TypeScript)

│   ├── public/              # Statyczne pliki dostępne publicznie

│   │   ├── index.html       # Główny plik HTML

│   │   └── assets/          # Ikony, obrazy itp.

│   ├── src/                 # Źródła frontendowe

│   │   ├── assets/          # Obrazy, czcionki i inne statyczne zasoby

│   │   ├── components/      # Reużywalne komponenty React

│   │   │   ├── ui/          # Komponenty UI, np. Button, Modal

│   │   │   └── pages/       # Komponenty odpowiadające za strony (React Router)

│   │   ├── hooks/           # Custom Hooks (np. useAuth, useFetch)

│   │   ├── services/        # Obsługa komunikacji z API (np. axios)

│   │   ├── types/           # Typy TypeScript (np. User, APIResponse)

│   │   ├── utils/           # Funkcje pomocnicze

│   │   ├── App.tsx          # Główny komponent aplikacji

│   │   ├── main.tsx         # Punkt wejściowy (React DOM)

│   │   └── index.css        # Główne style

│   ├── package.json         # Konfiguracja npm

│   ├── tsconfig.json        # Konfiguracja TypeScript

│   └── vite.config.ts       # Konfiguracja Vite (jeśli korzystasz z Vite)

│

├── server/                  # Backend (Python + FastAPI)

│   ├── app/                 # Źródła aplikacji

│   │   ├── api/             # Endpointy REST API

│   │   │   ├── v1/          # Wersjonowanie API (v1, v2 itd.)

│   │   │   │   ├── auth.py  # Logowanie/rejestracja użytkownika

│   │   │   │   ├── lessons.py # Endpointy dla lekcji

│   │   │   │   └── progress.py # Endpointy dla śledzenia postępów

│   │   ├── core/            # Logika aplikacji i konfiguracja

│   │   │   ├── config.py    # Konfiguracja aplikacji (np. baza danych)

│   │   │   ├── auth.py      # Obsługa JWT, szyfrowania haseł

│   │   │   └── database.py  # Obsługa MySQL (SQLAlchemy)

│   │   ├── models/          # Modele danych (SQLAlchemy)

│   │   │   ├── user.py      # Model użytkownika

│   │   │   └── lesson.py    # Model lekcji

│   │   ├── schemas/         # Schematy (Pydantic)

│   │   │   ├── user.py      # Schemat użytkownika

│   │   │   └── lesson.py    # Schemat lekcji

│   │   ├── services/        # Logika biznesowa (np. obliczanie wyników testów)

│   │   ├── main.py          # Główny plik aplikacji FastAPI

│   │   └── tests/           # Testy API

│   ├── requirements.txt     # Zależności Python (FastAPI, SQLAlchemy itp.)

│   └── Dockerfile           # Konfiguracja Docker dla backendu

│

├── database/                # Konfiguracja bazy danych

│   ├── migrations/          # Pliki migracji (np. Alembic)

│   └── init.sql             # Skrypty inicjalizujące bazę

│

├── azure/                   # Konfiguracja Azure

│   ├── azure-pipelines.yml  # Konfiguracja CI/CD (Azure DevOps)

│   ├── app-service/         # Skrypty do wdrożenia aplikacji w Azure App Service

│   └── storage/             # Skrypty do konfiguracji Azure Blob Storage

│

├── .env                     # Zmienne środowiskowe (trzymane lokalnie)

├── .gitignore               # Ignorowane pliki przez Git

└── README.md                # Dokumentacja projektu
