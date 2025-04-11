# Historias de Usuario

## Historia 1: Login exitoso
**Como** usuario registrado  
**Quiero** poder iniciar sesión con mis credenciales  
**Para** acceder al sistema

### Criterios de aceptación
- Al ingresar usuario y contraseña válidos, se debe redirigir al inventario.

### Criterios de rechazo
- Si las credenciales son inválidas, debe mostrarse un mensaje de error.

## Historia 2: Login fallido
**Como** usuario  
**Quiero** que el sistema rechace credenciales inválidas  
**Para** evitar accesos no autorizados

### Criterios de aceptación
- Se muestra un error cuando el login falla.

### Criterios de rechazo
- No debe permitir avanzar al inventario.

## Historia 3: Agregar producto al carrito
**Como** usuario  
**Quiero** agregar productos al carrito  
**Para** comprarlos luego

### Criterios de aceptación
- El botón cambia a "Remove" y el carrito se actualiza.

### Criterios de rechazo
- No se actualiza el carrito si falla.

## Historia 4: Eliminar producto del carrito
**Como** usuario  
**Quiero** eliminar productos del carrito  
**Para** no comprarlos

## Historia 5: Ir al checkout
**Como** usuario  
**Quiero** continuar al checkout  
**Para** finalizar mi compra
