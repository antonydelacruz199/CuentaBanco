## 📌 Consigna: Implementación de la clase `CuentaBanco` en Python (POO)

### 🎯 Objetivo

Desarrollar una aplicación en **Python utilizando Programación Orientada a Objetos (POO)** que modele el comportamiento básico de una **cuenta bancaria**, aplicando buenas prácticas de desarrollo de software, control de versiones con Git y el estándar de codificación **PEP-8**.

---

### 🧩 Descripción de la actividad

El docente proporcionará un repositorio base en GitHub llamado **`CuentaBanco`**.
Cada estudiante deberá **realizar un fork del repositorio** y completar la implementación solicitada siguiendo estrictamente las indicaciones de esta consigna.

---

### 🏗️ Requisitos de implementación

#### 1. Clase `CuentaBanco`

Implementar la clase `CuentaBanco` en Python, considerando encapsulamiento y validación de datos.

La clase debe incluir los siguientes métodos:

* **`deposito_cuenta(monto)`**

  * Permite depositar un monto a la cuenta.
  * El monto debe ser un valor numérico positivo.

* **`retiro_cuenta(monto)`**

  * Permite retirar un monto de la cuenta.
  * El monto debe ser positivo y no debe superar el saldo disponible.

* **`transferencia_cuenta(monto, cuenta_destino)`**

  * Permite transferir un monto desde una cuenta origen hacia otra cuenta bancaria.
  * Se debe validar el monto y la cuenta destino.

* **`saldo_cuenta()`**

  * Retorna o muestra el saldo actual de la cuenta.

📌 **Validaciones obligatorias**

* Validar tipos de datos y valores inválidos.
* No permitir montos negativos o cero.
* Manejar errores mediante excepciones (`ValueError`, `TypeError`, u otras según corresponda).

---

#### 2. Aplicación `app.py`

* Implementar un archivo `app.py` que permita interactuar con la clase `CuentaBanco` mediante un **menú desde la línea de comandos**.
* El menú debe permitir ejecutar todas las operaciones disponibles:

  1. Depósito
  2. Retiro
  3. Transferencia
  4. Consulta de saldo
  5. Salir

---

### 📁 Repositorio base (proporcionado por el docente)

El repositorio inicial contiene:

* La clase `CuentaBanco` **con el constructor ya implementado**.
* El archivo `app.py` que **únicamente crea el objeto**, sin lógica adicional.

⚠️ **No se debe modificar la estructura inicial del proyecto**, salvo para completar la funcionalidad solicitada.

---

### 🌿 Control de versiones (Git/GitHub)

* Cada funcionalidad debe desarrollarse en una **rama independiente**:

  * `feature/deposito`
  * `feature/retiro`
  * `feature/transferencia`
  * `feature/saldo`
* Una vez finalizada cada funcionalidad, debe **fusionarse con la rama `main`**.
* El historial de commits debe ser claro y descriptivo.

---

### 📐 Buenas prácticas

* El código debe cumplir estrictamente con el estándar **PEP-8**.
* Usar nombres de variables y métodos claros y representativos.
* Mantener métodos cortos, cohesionados y bien estructurados.

---

### ✅ Entregable

* Enlace al repositorio GitHub del estudiante (fork del repositorio `CuentaBanco`).
* El repositorio debe ejecutarse correctamente desde la línea de comandos.

---

### 📌 Criterios de evaluación (referencial)

* Correcta implementación de POO
* Validación y manejo de errores
* Funcionamiento del menú en `app.py`
* Uso adecuado de Git y ramas
* Cumplimiento del estándar PEP-8