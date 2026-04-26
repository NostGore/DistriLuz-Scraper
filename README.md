# Consulta de Recibos de Luz - Distriluz Perú

**Autor:** zDxniel  
**TikTok:** [@DevBujito](https://tiktok.com/@DevBujito)

---

## Descripción

Este script automatiza la consulta de recibos de luz del servicio de Distriluz Perú mediante web scraping. Utiliza Selenium para interactuar con la oficina virtual de la empresa, permitiendo consultar recibos por número de suministro o DNI, y descarga la imagen del recibo directamente a tu computadora.

---

## URL de Consulta

```
https://servicios.distriluz.com.pe/OficinaVirtualConsulta/Consultas/Consultas/ConsultaMiRecibo
```

Este es el portal oficial de consulta de recibos de la empresa Distriluz, que opera en la región de Lambayeque, Perú.

---

## Funcionamiento

### Flujo del programa

1. **Selección de tipo de consulta:** El script te pregunta si deseas buscar por número de suministro (opción 1) o por DNI (opción 2).

2. **Ingreso de datos:** Solicita el número correspondiente según la opción seleccionada.

3. **Automatización del navegador:** Abre Chrome en modo headless (sin interfaz visible) y navega a la URL de Distriluz.

4. **Interacción con el formulario:**
   - Selecciona el tipo de búsqueda en el dropdown (`cmbType`)
   - Ingresa el número en el campo de texto (`txtIdNroServicio`)
   - Presiona el botón de búsqueda (`btnSearch`)

5. **Extracción de datos:** Espera a que cargue la imagen del recibo (`imgRecibo`), la cual viene codificada en base64.

6. **Descarga del recibo:** Decodifica la imagen base64 y la guarda como archivo PNG local.

---

## Datos Extraídos

- **Imagen del recibo de luz:** El script descarga la imagen completa del recibo que muestra el portal de Distriluz.
- **Nombre del archivo generado:** `recibo-de-luz-{valor}.png` (donde `{valor}` es el número de suministro o DNI ingresado).

---

## Tecnologías Utilizadas

- **Python 3**
- **Selenium WebDriver:** Para automatización de navegador
- **Google Chrome:** Navegador utilizado (en modo headless)
- **Base64:** Decodificación de la imagen del recibo

---

## Requisitos

```
pip install selenium
```

Además, necesitas tener instalado **Google Chrome** en tu sistema.

---

## Estructura del Código

| Elemento | Descripción |
|----------|-------------|
| `URL` | Constante con la dirección del portal de Distriluz |
| `tipo` | Variable que almacena el tipo de consulta (1: Suministro, 2: DNI) |
| `valor` | Número ingresado por el usuario para la consulta |
| `options` | Configuración de Chrome en modo headless con resolución 1920x1080 |
| `wait` | WebDriverWait con timeout de 20 segundos para esperar elementos |

### Selectores utilizados

- `#cmbType` - Dropdown de selección de tipo de consulta
- `#txtIdNroServicio` - Campo de texto para ingresar número
- `#btnSearch` - Botón de búsqueda
- `#imgRecibo` - Elemento imagen que contiene el recibo en base64

---

## Uso

1. Ejecuta el script:
   ```bash
   python main.py
   ```

2. Selecciona el tipo de consulta:
   ```
   1: Suministro | 2: DNI -> 
   ```

3. Ingresa el número cuando se solicite:
   ```
   Número: 
   ```

4. El script procesará la consulta y guardará el recibo como imagen PNG en la carpeta del proyecto.

---

## Manejo de Errores

El script incluye manejo de excepciones que:
- Valida que se ingrese una opción correcta (1 o 2)
- Captura errores durante la ejecución de Selenium
- Verifica si el recibo fue encontrado antes de intentar descargarlo
- Cierra el navegador automáticamente al finalizar (incluso si hay errores)

---

## Notas Importantes

- El script espera máximo 20 segundos a que los elementos de la página carguen.
- El modo headless permite ejecutar el script sin que se abra una ventana de Chrome visible.
- La resolución de 1920x1080 asegura que la página se renderice correctamente para la extracción de datos.
