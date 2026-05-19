Create database zimbra_db;
Use zimbra_db;

-- 1. Tabla de Colaboradores (Representantes de Ventas)
CREATE TABLE colaboradores (
    colaborador_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    especialidad ENUM('General', 'Soporte Técnico', 'Cierre Comercial') DEFAULT 'General',
    activo BOOLEAN DEFAULT TRUE
);

-- 2. Tabla de Prospectos (Leads captados por el marketing viral)
CREATE TABLE prospectos (
    prospecto_id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_empresa VARCHAR(150) NOT NULL,
    email_contacto VARCHAR(100) UNIQUE NOT NULL,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    version_prueba_vence DATE NOT NULL,
    estado_prospecto ENUM('Frio', 'Tibio', 'Caliente', 'Convertido', 'Perdido') DEFAULT 'Frio'
);

-- 3. Tabla de Actividades Web (Registro masivo de eventos para tracking)
-- Aquí se registrarían los clics y descargas mencionadas en el caso
CREATE TABLE actividades_web (
    actividad_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    prospecto_id INT,
    tipo_evento VARCHAR(50) NOT NULL, -- Ejemplo: 'Descarga', 'Visita Precios', 'Login'
    url_visitada VARCHAR(255),
    timestamp_evento TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (prospecto_id) REFERENCES prospectos(prospecto_id) ON DELETE CASCADE
);

-- 4. Tabla de Puntajes Scoring (Lógica de automatización OneView)
CREATE TABLE puntajes_scoring (
    scoring_id INT AUTO_INCREMENT PRIMARY KEY,
    prospecto_id INT UNIQUE,
    puntos_acumulados INT DEFAULT 0,
    ultima_actualizacion DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (prospecto_id) REFERENCES prospectos(prospecto_id) ON DELETE CASCADE,
    CONSTRAINT chk_puntos CHECK (puntos_acumulados >= 0)
);

-- 5. Tabla de Interacciones de Ventas (CRM - Salesforce Integration)
CREATE TABLE interacciones_ventas (
    interaccion_id INT AUTO_INCREMENT PRIMARY KEY,
    colaborador_id INT,
    prospecto_id INT,
    fecha_contacto TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    medio ENUM('Telefono', 'Email', 'Chat') NOT NULL,
    notas TEXT,
    FOREIGN KEY (colaborador_id) REFERENCES colaboradores(colaborador_id),
    FOREIGN KEY (prospecto_id) REFERENCES prospectos(prospecto_id)
);

-- 6. Tabla de Contratos Comerciales (Cierre de Ventas)
-- Esta es la tabla más crítica para el manejo de transacciones monetarias
CREATE TABLE contratos_comerciales (
    contrato_id INT AUTO_INCREMENT PRIMARY KEY,
    prospecto_id INT UNIQUE, -- Un contrato por prospecto convertido
    monto_total DECIMAL(12, 2) NOT NULL,
    fecha_cierre DATE NOT NULL,
    metodo_pago VARCHAR(50),
    plan_adquirido VARCHAR(50) NOT NULL, -- Ejemplo: 'Standard ZCS', 'Professional ZCS'
    FOREIGN KEY (prospecto_id) REFERENCES prospectos(prospecto_id),
    CONSTRAINT chk_monto CHECK (monto_total > 0)
);

INSERT INTO prospectos (prospecto_id, nombre_empresa, email_contacto, version_prueba_vence, estado_prospecto)
VALUES (1, 'Empresa de Prueba JML', 'contacto@jmlprueba.com', '2026-12-31', 'Frio');