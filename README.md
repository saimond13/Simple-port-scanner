# Escáner TCP simple

> Script Python minimal para comprobar si puertos comunes están abiertos en una IP o dominio.

---

## Índice

* [Qué hace](#qué-hace)
* [Requisitos](#requisitos)
* [Cómo ejecutarlo](#cómo-ejecutarlo)
* [Ejemplo de uso](#ejemplo-de-uso)
* [Limitaciones importantes](#limitaciones-importantes)
* [Mejoras sugeridas](#mejoras-sugeridas)
* [Aviso legal y ético](#aviso-legal-y-ético)
* [Licencia](#licencia)

---

## Qué hace

Este script realiza un **escaneo TCP muy básico (connect scan)** contra una lista fija de puertos (`21, 22, 80, 443, 8080`).
Pide al usuario la IP o dominio, intenta conectarse a cada puerto y muestra en consola los puertos que respondieron (abiertos).

---

## Requisitos

* Python 3.6 o superior.
* No necesita librerías externas (usa la librería estándar `socket`).

---

## Cómo ejecutarlo

1. Copia el script en un archivo llamado, por ejemplo, `port_scanner.py`.
2. Ejecuta desde la terminal:

```bash
python3 port_scanner.py
```

3. Ingresa la IP o dominio cuando se solicite:

```
🔍 Ingrese la IP o dominio a escanear: example.com
```

---

---

## Ejemplo de salida

```
Escaneando example.com...

✅ Puerto 80 abierto
✅ Puerto 443 abierto
```

---

## Limitaciones importantes

* Escanea **solo** los puertos listados en `ports`.
* Usa `socket.AF_INET` → **no compatible con IPv6**.
* Sin concurrencia: los puertos se prueban uno a uno (puede ser lento si amplías la lista).
* Timeout fijo de 1 segundo: en redes lentas puede dar falsos negativos.
* No cierra explícitamente los sockets ni maneja todas las excepciones (mejorable).

---

## Aviso legal y ético ⚖️

Solo escanear hosts y redes **cuando tengas permiso explícito**. El escaneo no autorizado puede ser ilegal y/o violar políticas de uso. Usa este script únicamente en entornos de prueba o con autorización del propietario del sistema.

---

## Licencia

Usalo libremente para aprendizaje y pruebas. Si querés, puedo añadir una cabecera de licencia (p. ej. MIT) — indicame cuál prefieres.
