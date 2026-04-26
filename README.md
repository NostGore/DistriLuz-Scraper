# Consulta de Recibo de Luz (Scraping con Selenium)

Este script en Python automatiza la consulta de recibos de luz desde la página de Distriluz y guarda el resultado como una imagen en tu computadora.

La idea es simple: el programa simula lo que harías manualmente en el navegador (elegir tipo de búsqueda, ingresar el número y hacer clic en consultar), pero lo hace de forma automática. Luego toma el resultado, que viene como una imagen codificada en base64, la decodifica y la guarda como archivo `.png`.

---

## ¿Qué hace exactamente?

1. Te pide por consola si quieres buscar por:
   - Suministro
   - DNI

2. Te solicita el número correspondiente.

3. Abre la página de consulta en segundo plano (sin mostrar el navegador).

4. Completa el formulario automáticamente.

5. Espera a que el sistema genere el recibo.

6. Extrae la imagen del recibo (que viene en base64).

7. La convierte en una imagen real y la guarda en tu equipo.

---

## Requisitos

- Python 3
- Google Chrome instalado
- ChromeDriver compatible con tu versión de Chrome

Instalar dependencias:

```bash
pip install selenium
