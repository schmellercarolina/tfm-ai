# Análisis de Turismo en Canarias - TFM MVP

> Plataforma interactiva de análisis turístico para las Islas Canarias
>
> Proyecto TFM - Máster en IA Generativa 2025

## Inicio

```bash
# Install dependencies (already done!)
npm install

# Start development server
npm run dev
```

Haz click aqui para ver la applicación http://localhost:3000

## Funciones

-  Mapa 3D Interactivo – Islas Canarias seleccionable, React Three Fiber
-  Panel de Métricas y KPIs turísticos
-  Visualización de Datos – Series temporales, estacionalidad, países de origen
-  Interfaz Moderna – Tailwind CSS
-  Diseño Responsivo – Funciona en escritorio y móvil
-  Más de 10 Años de Datos – Estadísticas turísticas reales (2015-2025)

##  Documentación

- **[README.md](./README.md)** - Ejecuta la app y prueba las funciones!
- **[CLAUDE.md](./CLAUDE.md)** - Especificaciones completas del proyecto y arquitectura

## Tecnologíask

- **React 18** + TypeScript
- **Vite** - Herramienta de construcción
- **React Three Fiber** - 3 Gráficos 3D
- **Recharts** - Visualización de datos
- **Tailwind CSS** - Estilo general de la aplicación

## Las 7 islas Canarias

1. **Tenerife** (10.7M turistas) – Azul
2. **Gran Canaria** (10.3M turistas) – Azul Claro
3. **Lanzarote** (5.9M turistas) – Amarillo
4. **Fuerteventura** (5.3M turistas) – Arena
5. **La Palma** (1.9M turistas) – Azul Grisáceo
6. **La Gomera** (1.0M turistas) – Gris Oscuroy
7. **El Hierro** (0.6M turistas) – Gris Muy Oscuro

## Flujo del usuario

1. **Vista de inicio** - Ver las 7 islas con datos agregados
2. **Seleccionar Isla** - Filtrar datos de una isla específica
3. **Explorar Métrica** - Ver KPIs y gráficos
4. **Compare Islands** - Cambiar entre islas
5. **Volver a vsiata general** - Seleccionar “Ver Todas las Islas”

## Vista de datos

- **20 metricas** por punto de datos
- **~4,000 registros**  (datos semanales de 2015 a 2025)
- **Principales países de origen**: España, Reino Unido, Alemania, Francia
- **Temporada alta**: julio-agosto
- **Estancia promedio**: 6 - 8 días
- **Gasto promedio**: 802 €/viaje

## Presentacion

- ✅ Visualización de datos interactiva
- ✅ Gráficos web 
- ✅ Análisis de datos reales
- ✅ Desarrollo web moderno
- ✅ Diseño de experiencia de usuario

## Estructura del Proyecto

```
src/
├── components/       # React components
│   ├── Map3D/       # 3D visualization
│   ├── Dashboard/   # Charts and KPIs
│   └── Layout/      # Header and Sidebar
├── hooks/           # Custom React hooks
├── data/            # Tourism JSON data
├── types/           # TypeScript definitions
└── utils/           # Helper functions
```

## Solución de Problemas

### ¿La app no inicia?
```bash
rm -rf node_modules
npm install
npm run dev
```

### ¿Los datos no se cargan?
- Verifica que `src/data/tourism_data.json` exista
- Revisa la consola del navegador para ver errores

## Licencia

Licencia MIT – Ver [LICENSE](./LICENSE)

## Autores

**TFM* - Master en desarollo de IA Generativa 2025

