# Análisis de Turismo en Canarias - TFM MVP

## Descripción del proyecto

Un proyecto de Trabajo de Fin de Máster para un IA de Generación de Informes Turísticos Inteligentes para Canarias 
El objetivo es crear una plataforma interactiva de análisis turístico para las Islas Canarias, pensada para que pequeñas empresas y entidades locales puedan acceder fácilmente a datos y análisis sobre turismo.

## Visión principal

Una aplicación interactiva hecha en React ya que se ejecuta en el navegador y permite al usuario interactuar directamente con la interfaz, obteniendo respuestas rápidas y fluidas.
1. Incluye un mapa de las Islas Canarias: pudiendo seleccionar en la isla o el filtro de isla.
2. Panel de control con KPIs: donde se visualizan las métricas turísticas principales
3. Incorpora también un Chat con IA: para preguntas y respuestas usando Claude, limitado solo a los datos del proyecto.

## Tecnologías utilizadas: 

- **Frontend**: React 18+ with TypeScript
- **Visualizaciones**: React Three Fiber (Three.js)
- **Gráficos**: Recharts
- **Estilo**: Tailwind CSS
- **AI Chat**: Anthropic Claude API 
- **Herramienta**: Vite

## Detalles del dataset

File: `canarias_turismo_2015_2025.csv` (~4K rows)

### Schema (20 columns)

| Column | Type | Description |
|--------|------|-------------|
| week_start_date | date | Start of the week (YYYY-MM-DD) |
| year | int | Year (2015-2025) |
| month | int | Month number (1-12) |
| calendar_week | int | Week of year (1-53) |
| island_code | string | Island identifier (01-07) |
| island_name | string | Island name |
| total_tourists | int | Total tourists that week |
| intl_passengers | int | International passengers |
| most_common_intl_country | string | Most common origin (ES, UK, DE, FR, IT, NL, SE, PT) |
| dom_passengers | int | Domestic passengers |
| occupancy_rate | float | Hotel occupancy (0.23-0.84) |
| avg_daily_rate_eur | float | Average daily rate in EUR (30-112€) |
| nights | int | Total nights stayed |
| guests | int | Number of guests |
| revenue | float | Hotel revenue in EUR |
| avg_spend_per_trip | float | Average spend per trip (425-1205€) |
| stay_length | float | Average stay in days (5.6-7.9) |
| total_expenditure | float | Total tourist expenditure |
| events_count | int | Number of events that week |
| event_attendance | int | Event attendance |

### Islas (por volumen de turistas)

| Code | Name | Total Tourists (2015-2025) |
|------|------|---------------------------|
| 01 | Tenerife | 10,740,750 |
| 02 | Gran Canaria | 10,322,008 |
| 03 | Lanzarote | 5,907,618 |
| 04 | Fuerteventura | 5,335,302 |
| 05 | La Palma | 1,867,756 |
| 06 | La Gomera | 964,021 |
| 07 | El Hierro | 642,514 |

### Key Metrics Ranges

- **Tourists por semana**: 332 - 34,537
- **Ocupación**: 23% - 84% (avg 55%)
- **Daily Rate**: 30€ - 112€ (avg 60€)
- **Duración dela estancia**: 5.6 - 7.9 days (avg 6.8)
- **Gastos por viaje**: 425€ - 1,205€ (avg 802€)

## Arquitectura

```
src/
├── components/
│   ├── Map3D/
│   │   ├── CanaryIslands.tsx      # Main 3D scene
│   │   ├── Island.tsx             # Individual island mesh
│   │   └── IslandGeometry.ts      # Island shape definitions
│   ├── Dashboard/
│   │   ├── KPICards.tsx           # Summary metrics
│   │   ├── TouristChart.tsx       # Time series
│   │   ├── OccupancyChart.tsx     # Occupancy trends
│   │   ├── OriginChart.tsx        # Country breakdown
│   │   └── SeasonalityChart.tsx   # Monthly patterns
│   ├── Chat/                      # (Stretch goal)
│   │   ├── ChatPanel.tsx
│   │   └── ChatMessage.tsx
│   └── Layout/
│       ├── Header.tsx
│       └── Sidebar.tsx
├── hooks/
│   ├── useTourismData.ts          # Data loading & filtering
│   └── useIslandSelection.ts      # Island state management
├── data/
│   └── tourism.json               # Transformed CSV data
├── types/
│   └── tourism.ts                 # TypeScript interfaces
├── utils/
│   ├── dataTransforms.ts          # Aggregation functions
│   └── formatters.ts              # Number/date formatting
├── App.tsx
└── main.tsx
```

## User Flow

1. **vista inicial**: Un mapa de todas las Islas Canarias, Filtros, KPIs y Gráficos
2. **Seleccion de isla**: El usuario hace clic en una isla → el panel de datos se filtra solo para esa isla.
3. **Volver atrás**: Un botón “Todas las islas” devuelve a la vista general con todos los datos.
4. **Filtro por tiempo**: Selectores de año y mes para acotar el período de análisis.
5. **Chat**: El usuario puede hacer preguntas sobre los datos usando lenguaje natural.

## Fases de implementación

### Fase 1: Configuración del proyecto y datos
- [ ] Initialize Vite + React + TypeScript
- [ ] Configurar Tailwind CSS
- [ ] Transformar archivos CSV a una estructura JSON optimizada
- [ ] Crear interfaces en TypeScript
- [ ] Implementar un hook para cargar los datos

### Fase 2: Mapa 3D
- [ ] Configurar la escena con React Three Fiber
- [ ] Crear geometrías simplificadas de las islas (polígonos extruidos)
- [ ] Implementar detección de clic en cada isla
- [ ] Añadir efectos al pasar el ratón y resaltado de selección

### Fase 3: Panel de control (Dashboard)
- [ ] Paneles de KPIs (total de turistas, ocupación media, ingresos, etc.)
- [ ] Gráfico de series temporales (turistas a lo largo del tiempo)
- [ ] Gráfico de barras (turistas por país de origen)
- [ ] Mapa de calor estacional o gráfico de líneas
- [ ] Todos los gráficos responden a la isla seleccionada

### Fase 4: Pulido final
- [ ] Transiciones suaves entre vistas
- [ ] Estados de carga
- [ ] Diseño adaptable a distintos tamaños de pantalla
- [ ] Manejo de errores

### Fase 5: Chat con IA 
- [ ] Componente de interfaz de chat
- [ ] Integración con la API de Claude
- [ ] Prompt del sistema que limite las respuestas solo al contexto de los datos
- [ ] Mostrar respuestas basadas en datos reales del archivo JSON

## Guías de diseño

- **Paleta de colores**:  azules oceánicos, amarillos arena y grises volcánicos
- **Tipografía**: sans-serif limpia y moderna
- **Isla**: cada isla debe tener un color distinto pero armonioso
- **Interacciones**: respuestas suaves al pasar el ratón y hacer clic, transiciones de unos 300 ms
- **Móvil**: diseño adaptable al móvil pero pensado principalmente para escritorio

## Comandos clave

```bash
# Install dependencies
npm install

# Development
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## NOTAS

1. Los datos son reales: provienen de estadísticas oficiales del Gobierno de Canarias, AENA, etc.
2. No se necesita backend: todos los datos pueden incluirse directamente en el frontend ya que no hay operaciones dinámicas ni datos que cambien en tiempo real incluidos de momento.


## posición aproximada de las islas (para map)

Posiciones relativas (coordenadas normalizadas, Tenerife como referencia central):

| Island | X | Y | Relative Size |
|--------|---|---|---------------|
| El Hierro | -2.0 | -0.5 | 0.3 |
| La Palma | -1.5 | 0.8 | 0.4 |
| La Gomera | -1.0 | 0.0 | 0.3 |
| Tenerife | 0.0 | 0.0 | 1.0 |
| Gran Canaria | 1.2 | -0.3 | 0.9 |
| Fuerteventura | 2.2 | -0.2 | 0.7 |
| Lanzarote | 2.5 | 0.6 | 0.5 |

## Criterios de éxito

1. El usuario puede ver un mapa de las 7 Islas Canarias.
2. Al hacer clic en una isla, se filtran todos los datos del panel a esa isla.
3. El filtrado por tiempo funciona (año/mes).
4. El usuario puede descargar los Datos en formato PDF o JSON para futuro procesamiento.
5. El chat de IA responde preguntas sobre los datos.

