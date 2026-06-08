# SYNTHETIC NATION

> Autonomous policy simulation engine with 100,000+ AI citizens.  
> Test policies before testing on real people.

![React](https://img.shields.io/badge/React-18-61DAFB?logo=react&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&logoColor=white)
![Tailwind](https://img.shields.io/badge/Tailwind_CSS-4-06B6D4?logo=tailwindcss&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-8-646CFF?logo=vite&logoColor=white)

---

## Overview

Synthetic Nation is a policy simulation platform that models the behavior of autonomous AI citizens across Indian metropolitan cities. It enables policymakers to stress-test infrastructure, economic, and social policies in a risk-free synthetic environment before real-world deployment.

### Key Features

- **Mission Control** — Real-time dashboard with global sensor grid, agent metrics, decision logs, and threat monitoring
- **Geo-Synthesis** — Interactive city node explorer with live telemetry feeds and dark-tiled maps
- **Policy Simulation** — Configure temporal resolution, vector variance, and natural language policy directives against target cities
- **Hindcast Validation** — Empirical divergence analysis with historical accuracy benchmarking (94.2% global accuracy)

### Cities Monitored

| City | Population | Status | Threat Level |
|------|-----------|--------|-------------|
| Delhi | 32.9M | `SECURE` | LOW |
| Mumbai | 21.3M | `MONITORING` | ELEVATED |
| Kolkata | 15.1M | `COMPROMISED` | CRITICAL |
| Bengaluru | 13.2M | `SECURE` | LOW |
| Chennai | 11.2M | `MONITORING` | ELEVATED |
| Hyderabad | 10.5M | `SECURE` | LOW |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Framework | React 18 + TypeScript |
| Build Tool | Vite 8 |
| Styling | Tailwind CSS 4 + CSS Custom Properties |
| Charts | Recharts |
| Maps | React Leaflet + Stadia Dark Tiles |
| Animations | Framer Motion |
| Routing | React Router v6 |
| Typography | DM Serif Display, PT Serif, Bitcount Single |

---

## Getting Started

### Prerequisites

- Node.js 18+
- npm 9+

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/SyntheticNation.git
cd SyntheticNation

# Install frontend dependencies
cd frontend
npm install

# Start the development server
npm run dev
```

The app will be available at `http://localhost:5173/`.

### Build for Production

```bash
cd frontend
npm run build
```

Output will be in `frontend/dist/`.

---

## Project Structure

```
SyntheticNation/
├── docs/                       # Project documentation
│   ├── AGENT_SPEC.md           # AI agent architecture spec
│   ├── ARCHITECTURE.md         # System architecture overview
│   ├── CITY_PROFILES.md        # Indian city data profiles
│   ├── CREDIBILITY_SHIELD.md   # Validation methodology
│   ├── DATA_SOURCES.md         # Data source references
│   ├── MVP_SCOPE.md            # MVP scope definition
│   ├── PROJECT_BRIEF.md        # Project brief
│   └── VALIDATION.md           # Validation framework
├── frontend/                   # React frontend application
│   ├── src/
│   │   ├── components/
│   │   │   ├── layout/         # AppShell, TopNav, SideNav, StatusBar
│   │   │   └── ui/             # GlassPanel, DataChip, TerminalInput, etc.
│   │   ├── data/               # Mock data (cities, agents, validation)
│   │   ├── hooks/              # Custom hooks (typewriter, countUp, etc.)
│   │   ├── pages/              # Page components (4 screens)
│   │   └── styles/             # Global CSS + font declarations
│   ├── package.json
│   └── vite.config.ts
├── backend/                    # Backend API (Python)
├── .gitignore
└── README.md
```

---

## Design System

The UI follows a **terminal surveillance aesthetic** with sharp corners, glass panels, and a dark void background.

### Color Palette

| Token | Value | Usage |
|-------|-------|-------|
| `--color-void` | `#0a0c10` | Page background |
| `--color-primary` | `#00e5ff` | Accent, active states, data highlights |
| `--color-alert` | `#ff0055` | Critical threats, errors |
| `--color-warn` | `#ffb347` | Warnings, elevated states |
| `--color-success` | `#1aad6e` | Stable, online, positive deltas |

### Typography

| Font | Usage |
|------|-------|
| DM Serif Display | Headlines, section titles |
| PT Serif | Body text, descriptions |
| Bitcount Single / Courier New | Numbers, labels, metrics, terminal text |

### Key Design Rules

- `border-radius: 0` on everything (sharp corners)
- Glass panels: `backdrop-filter: blur(20px)` with primary border glow
- `cursor: crosshair` on all interactive elements
- All status text in `[BRACKETS]` format
- Chamfered corners (clip-path) on CTA buttons only

---

## Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start Vite dev server with HMR |
| `npm run build` | TypeScript check + production build |
| `npm run lint` | Run ESLint |
| `npm run preview` | Preview production build locally |

---

## License

This project is proprietary. All rights reserved.
