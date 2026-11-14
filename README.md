# 🛡️ Laboratorio de Ciberseguridad - Cristian Salcedo

Este repositorio contiene la arquitectura, el código fuente y las configuraciones de contenedores Docker para los **8 servicios** que componen el entorno de simulación y evaluación de ciberseguridad en la nube (**Render**).

---

## 👨‍💻 Datos del Estudiante
* **Nombre:** Cristian Salcedo
* **Institución:** IU Digital de Antioquia
* **Repositorio:** `laboratorio-ciberseguridad-csalcedo`
* **URL DMZ Objetivo:** `https://servidor-web-dmz-csalcedo.onrender.com`

---

## 📁 Estructura del Repositorio

```text
laboratorio-ciberseguridad/
├── README.md
├── .gitattributes
├── 00-servidor-dmz/            # Servidor objetivo DMZ (Víctima)
│   ├── app.py
│   └── Dockerfile
├── 01-ataque-dos/               # Ráfaga masiva de peticiones HTTP
│   ├── entrypoint.sh
│   └── Dockerfile
├── 02-escaneo-puertos/          # Reconocimiento y escaneo TCP con netcat
│   ├── entrypoint.sh
│   └── Dockerfile
├── 03-fuerza-bruta-rutas/       # Enumeración de directorios web
│   ├── entrypoint.sh
│   └── Dockerfile
├── 04-exfiltracion-dns/         # Exfiltración encubierta de datos vía DNS
│   ├── entrypoint.sh
│   └── Dockerfile
├── 05-cadena-suministro/        # Inyección maliciosa en build de contenedor
│   ├── entrypoint.sh
│   └── Dockerfile
├── 06-credential-stuffing/      # Relleno de credenciales / Fuerza bruta Basic Auth
│   ├── entrypoint.sh
│   └── Dockerfile
└── 07-proxy-mitm/               # Proxy interceptor Man-in-the-Middle
    ├── app.py
    └── Dockerfile
```

---

## 🔍 Resumen Técnico de los Módulos

| Módulo | Tipo | Descripción y Vector de Prueba |
| :--- | :--- | :--- |
| **`00-servidor-dmz`** | Víctima (Objetivo) | Servidor web perimetral en Python con mensaje personalizado `"Servidor DMZ Activo - Laboratorio de Cristian Salcedo"` y registro en tiempo real de peticiones en los logs. |
| **`01-ataque-dos`** | Ofensivo | Genera una ráfaga concurrente de 30 solicitudes HTTP simultáneas dirigidas a saturar el servidor objetivo. |
| **`02-escaneo-puertos`** | Reconocimiento | Escanea puertos comunes (`21`, `22`, `80`, `443`, `8080`, `3306`) sobre el host de la DMZ usando `netcat`. |
| **`03-fuerza-bruta-rutas`** | Reconocimiento | Intenta acceder a rutas administrativas críticas (`/admin`, `/config.php`, `/login`, `/secret`, `/backup.zip`) y reporta los códigos HTTP. |
| **`04-exfiltracion-dns`** | Exfiltración | Codifica datos sensibles en Base64 (`clave_secreta_banco_2026`) y realiza solicitudes de resolución DNS (`nslookup`) incrustando la información en el subdominio. |
| **`05-cadena-suministro`** | Persistencia/Compromiso | Demuestra la manipulación durante la fase de construcción de la imagen (`docker build`), ejecutando scripts no autorizados dentro del contenedor. |
| **`06-credential-stuffing`** | Autenticación | Prueba un listado de usuarios comunes (`admin`, `root`, `user`, `docente`, `gestor`) enviando combinaciones de credenciales mediante cabeceras `Authorization: Basic`. |
| **`07-proxy-mitm`** | Interceptación MITM | Proxy inverso en Flask que intercepta las peticiones dirigidas a la DMZ e inyecta código visual y comentarios HTML en la respuesta antes de devolverla al cliente. |

---

## 🚀 Guía de Despliegue en Render

### Paso 1: Crear el repositorio en GitHub
1. Crear un repositorio público en GitHub llamado `laboratorio-ciberseguridad-csalcedo`.
2. Subir este proyecto mediante Git:
   ```bash
   git init
   git add .
   git commit -m "feat: Configuración inicial de los 8 módulos del laboratorio"
   git branch -M main
   git remote add origin https://github.com/<TU_USUARIO_GITHUB>/laboratorio-ciberseguridad-csalcedo.git
   git push -u origin main
   ```

### Paso 2: Desplegar el Servidor DMZ (Primero)
1. En [Render.com](https://render.com/), ir a **New +** > **Web Service**.
2. Conectar el repositorio `laboratorio-ciberseguridad-csalcedo`.
3. Parámetros de configuración:
   * **Name:** `servidor-web-dmz-csalcedo`
   * **Region:** Oregon (US West) o la de preferencia.
   * **Branch:** `main`
   * **Root Directory:** `00-servidor-dmz`
   * **Runtime:** `Docker`
   * **Instance Type:** `Free`
4. Clic en **Create Web Service**.
5. Esperar a que el estado sea **Live**. La URL asignada será: `https://servidor-web-dmz-csalcedo.onrender.com`.

### Paso 3: Desplegar los Módulos 01 al 07
Para cada módulo atacante, repetir el proceso en Render creando un nuevo **Web Service**:

| Servicio | Nombre en Render | Root Directory | Runtime |
| :--- | :--- | :--- | :--- |
| **Módulo 01** | `modulo-01-dos-csalcedo` | `01-ataque-dos` | Docker |
| **Módulo 02** | `modulo-02-escaneo-csalcedo` | `02-escaneo-puertos` | Docker |
| **Módulo 03** | `modulo-03-fuerza-bruta-csalcedo` | `03-fuerza-bruta-rutas` | Docker |
| **Módulo 04** | `modulo-04-exfiltracion-csalcedo` | `04-exfiltracion-dns` | Docker |
| **Módulo 05** | `modulo-05-suministro-csalcedo` | `05-cadena-suministro` | Docker |
| **Módulo 06** | `modulo-06-credenciales-csalcedo` | `06-credential-stuffing` | Docker |
| **Módulo 07** | `modulo-07-mitm-csalcedo` | `07-proxy-mitm` | Docker |

> **Nota:** Todos los módulos vienen preconfigurados por defecto con la URL objetivo `https://servidor-web-dmz-csalcedo.onrender.com`. Si tu URL de DMZ tiene una variación, puedes pasar la variable de entorno `TARGET` (o `DMZ_URL`) en la pestaña **Environment** de Render.

---

## 📹 Requisitos para la Grabación del Video (Máximo 7 minutos)

Para cumplir con la rúbrica del laboratorio:
1. **Identificador personal en las URLs:** Mostrar que todos los servicios en Render llevan `csalcedo` o `cristian-salcedo`.
2. **Mensaje personalizado en la DMZ:** Abrir la URL pública de la DMZ (`00-servidor-dmz`) en el navegador y mostrar:
   * *"Servidor DMZ Activo - Laboratorio de Cristian Salcedo"*.
3. **Pestaña Logs de cada servicio:** Mostrar los logs de compilación y ejecución de los módulos 01 al 06 evidenciando las ráfagas DoS, el escaneo de puertos, las rutas probadas, la consulta DNS con payload y la detección en cadena de suministro.
4. **Verificación de Inyección MITM:** Abrir la URL del Módulo 07 (`modulo-07-mitm-csalcedo`) en el navegador para evidenciar el banner de alerta y la inyección en la respuesta HTTP recibida de la DMZ.
