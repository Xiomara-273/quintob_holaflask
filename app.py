from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

# Definición del HTML/CSS/JS como una cadena multilínea
PAGE_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>FlaskApp | Página Bonita</title>
    <!-- Google Fonts: Poppins y Open Sans -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:opsz,wght@14..32,300;14..32,400;14..32,600;14..32,700&family=Poppins:wght@400;500;600;700&display=swap" rel="stylesheet">
    <!-- Font Awesome 6 (gratuito) -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #e9eef5 100%);
            color: #1e293b;
            line-height: 1.5;
            min-height: 100vh;
        }

        /* Contenedor principal con ancho elegante */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem 1.5rem;
        }

        /* Header con efecto glassmorphism */
        .glass-header {
            background: rgba(255, 255, 255, 0.75);
            backdrop-filter: blur(12px);
            border-radius: 2rem;
            padding: 1rem 2rem;
            margin-bottom: 2rem;
            box-shadow: 0 8px 20px rgba(0,0,0,0.05);
            border: 1px solid rgba(255,255,255,0.6);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
        }

        .logo h1 {
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            font-size: 1.8rem;
            background: linear-gradient(120deg, #3b82f6, #9333ea);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
        }

        .time-badge {
            background: rgba(0,0,0,0.05);
            padding: 0.5rem 1rem;
            border-radius: 2rem;
            font-size: 0.9rem;
            font-weight: 500;
            color: #334155;
        }

        .time-badge i {
            margin-right: 8px;
            color: #3b82f6;
        }

        /* Hero section */
        .hero {
            text-align: center;
            padding: 3rem 1rem 2rem;
            animation: fadeInUp 0.8s ease-out;
        }

        .hero h2 {
            font-size: 2.8rem;
            font-weight: 700;
            background: linear-gradient(to right, #1e293b, #3b82f6);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            margin-bottom: 1rem;
        }

        .hero p {
            font-size: 1.2rem;
            color: #475569;
            max-width: 650px;
            margin: 0 auto;
        }

        /* Tarjetas (cards) */
        .cards-section {
            margin: 3rem 0;
        }

        .section-title {
            font-size: 1.8rem;
            font-weight: 600;
            margin-bottom: 2rem;
            text-align: center;
            position: relative;
            display: inline-block;
            width: 100%;
        }
        .section-title:after {
            content: '';
            display: block;
            width: 70px;
            height: 4px;
            background: linear-gradient(90deg, #3b82f6, #a855f7);
            margin: 0.5rem auto 0;
            border-radius: 4px;
        }

        .card-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 2rem;
        }

        .card {
            background: white;
            border-radius: 1.5rem;
            padding: 1.8rem;
            box-shadow: 0 15px 30px -12px rgba(0,0,0,0.1);
            transition: all 0.3s ease;
            border: 1px solid rgba(0,0,0,0.05);
            text-align: center;
        }

        .card:hover {
            transform: translateY(-6px);
            box-shadow: 0 25px 35px -15px rgba(0,0,0,0.2);
            border-color: rgba(59,130,246,0.3);
        }

        .card-icon {
            font-size: 2.8rem;
            background: linear-gradient(135deg, #eef2ff, #e0e7ff);
            width: 70px;
            height: 70px;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 2rem;
            margin-bottom: 1.2rem;
        }

        .card h3 {
            font-size: 1.5rem;
            font-weight: 600;
            margin-bottom: 0.75rem;
        }

        .card p {
            color: #4b5563;
            margin-bottom: 1.2rem;
        }

        /* Counter interactivo */
        .interactive-box {
            background: linear-gradient(120deg, #ffffff 0%, #f8fafc 100%);
            border-radius: 2rem;
            padding: 2rem;
            text-align: center;
            margin: 2rem 0;
            box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05);
            border: 1px solid rgba(255,255,255,0.7);
        }

        .counter-display {
            font-size: 4rem;
            font-weight: 800;
            font-family: monospace;
            background: linear-gradient(135deg, #2563eb, #7c3aed);
            background-clip: text;
            -webkit-background-clip: text;
            color: transparent;
            margin: 0.5rem 0;
        }

        .btn-group button {
            background: #f1f5f9;
            border: none;
            font-size: 1.3rem;
            padding: 0.6rem 1.4rem;
            margin: 0 0.5rem;
            border-radius: 3rem;
            cursor: pointer;
            transition: all 0.2s;
            font-weight: 600;
            color: #1e293b;
        }

        .btn-group button:hover {
            background: #3b82f6;
            color: white;
            transform: scale(1.02);
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 3rem;
            padding: 1.5rem;
            border-top: 1px solid rgba(0,0,0,0.05);
            color: #5b6e8c;
            font-size: 0.9rem;
        }

        /* Animaciones */
        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @media (max-width: 700px) {
            .glass-header {
                flex-direction: column;
                gap: 0.8rem;
                text-align: center;
            }
            .hero h2 {
                font-size: 2rem;
            }
            .counter-display {
                font-size: 3rem;
            }
        }
    </style>
</head>
<body>

<div class="container">
    <!-- Barra superior glassmorph -->
    <div class="glass-header">
        <div class="logo">
            <h1><i class="fas fa-feather-alt"></i> Flask美学</h1>
        </div>
        <div class="time-badge">
            <i class="far fa-clock"></i> 
            <span id="server-time">{{ server_time }}</span> 
            <span style="font-size:0.8rem;">(servidor)</span>
        </div>
    </div>

    <!-- Hero -->
    <div class="hero">
        <h2>Bienvenido a tu página <span style="background: linear-gradient(120deg,#3b82f6,#9333ea); background-clip:text; -webkit-background-clip:text; color:transparent;">Flask con estilo</span></h2>
        <p>Diseño moderno, responsivo y completamente funcional. Un solo archivo <code>app.py</code>.</p>
    </div>

    <!-- Tarjetas de características -->
    <div class="cards-section">
        <div class="section-title">✨ Características ✨</div>
        <div class="card-grid">
            <div class="card">
                <div class="card-icon"><i class="fas fa-code"></i></div>
                <h3>Código limpio</h3>
                <p>Todo en un solo archivo Python con HTML/CSS/JS integrado. Fácil de modificar.</p>
            </div>
            <div class="card">
                <div class="card-icon"><i class="fas fa-palette"></i></div>
                <h3>UI Atractiva</h3>
                <p>Gradientes suaves, sombras elegantes, tipografía profesional y responsiva.</p>
            </div>
            <div class="card">
                <div class="card-icon"><i class="fas fa-bolt"></i></div>
                <h3>Interactivo</h3>
                <p>Contador en tiempo real con JavaScript + hora actualizada del servidor (Flask).</p>
            </div>
        </div>
    </div>

    <!-- Zona interactiva: Counter con JS -->
    <div class="interactive-box">
        <i class="fas fa-mouse-pointer" style="font-size: 2rem; color:#3b82f6;"></i>
        <h3 style="margin-top: 0.5rem;">Contador interactivo</h3>
        <p>Haz clic en los botones para cambiar el valor (JavaScript puro)</p>
        <div class="counter-display" id="counterValue">0</div>
        <div class="btn-group">
            <button onclick="changeCounter(-1)"><i class="fas fa-minus"></i> Disminuir</button>
            <button onclick="changeCounter(1)"><i class="fas fa-plus"></i> Aumentar</button>
            <button onclick="resetCounter()"><i class="fas fa-undo-alt"></i> Reiniciar</button>
        </div>
    </div>

    <!-- Mensaje de bienvenida extra -->
    <div style="text-align: center; margin: 1rem 0 0.5rem;">
        <span class="time-badge" style="background: #e2e8f0;"><i class="fas fa-heart" style="color:#ef4444;"></i> Hecho con Flask & pasión</span>
    </div>

    <div class="footer">
        <i class="far fa-copyright"></i> 2025 · App construida con Python y Flask · Hora actual del sistema: <strong id="client-time"></strong> (tu dispositivo)
    </div>
</div>

<script>
    // Counter puramente frontend
    let counter = 0;
    const counterElement = document.getElementById('counterValue');

    function updateCounterDisplay() {
        counterElement.textContent = counter;
    }

    function changeCounter(delta) {
        counter += delta;
        updateCounterDisplay();
    }

    function resetCounter() {
        counter = 0;
        updateCounterDisplay();
    }

    // Reloj en tiempo real (cliente)
    function updateClientClock() {
        const now = new Date();
        const formatted = now.toLocaleTimeString('es-ES', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
        const clientTimeSpan = document.getElementById('client-time');
        if(clientTimeSpan) clientTimeSpan.textContent = formatted;
    }
    setInterval(updateClientClock, 1000);
    updateClientClock();

    // Inicializar
    updateCounterDisplay();
</script>

</body>
</html>
"""

@app.route('/')
def home():
    # Pasar la hora del servidor al template
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template_string(PAGE_HTML, server_time=current_time)

if __name__ == '__main__':
    # Ejecutar en modo debug para desarrollo (recarga automática)
    app.run(debug=True, host='0.0.0.0', port=5000)