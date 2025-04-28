import streamlit as st
import base64
from PIL import Image
import io
import os

# Configuración de la página
st.set_page_config(
    page_title="Bucaros Madrid Lorenzo",
    page_icon="📱",
    layout="centered"
)

# Título y descripción
st.markdown("<h1 style='text-align: center;'>Bucaros Madrid Lorenzo</h1>", unsafe_allow_html=True)
#st.title("Bucaros Madrid Lorenzo")
st.write("¡Conéctate conmigo en mis redes sociales!")

# Estilo CSS personalizado
st.markdown("""
<style>
    .social-button {
        display: block;
        margin: 10px 0;
        padding: 12px 20px;
        text-align: center;
        text-decoration: none;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        transition: transform 0.3s ease;
    }
    .social-button:hover {
        transform: scale(1.03);
    }
    .facebook {background-color: #1877F2;}
    .instagram {background-color: #E4405F;}
    .tiktok {background-color: #000000;}
    .whatsapp {background-color: #25D366;}
    .contact {background-color: #4CAF50;}
    
    .profile-pic {
        display: block;
        margin-left: auto;
        margin-right: auto;
        border-radius: 50%;
        width: 150px;
        height: 150px;
        object-fit: cover;
        border: 3px solid #f0f0f0;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)


# Opción para imagen local
profile_image_path = "Imagenes/Bucaroslorenzo.jpg"  # Ruta relativa al directorio del script

# Usamos columnas para centrar la imagen

col1, col2, col3 = st.columns(3)  # Tres columnas de igual tamaño

with col2:
    if os.path.exists(profile_image_path):
        # Leemos la imagen y la codificamos para que funcione en HTML
        import base64
        from pathlib import Path

        def get_base64(file_path):
            with open(file_path, "rb") as f:
                data = f.read()
            return base64.b64encode(data).decode()

        img_base64 = get_base64(profile_image_path)

        st.markdown(
            f"""
            <div style="display: flex; justify-content: center; align-items: center;">
                <img src="data:image/jpeg;base64,{img_base64}" 
                     style="width: 150px; height: 150px; object-fit: cover;
                            border-radius: 50%;
                            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.25);">
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.error(f"No se pudo encontrar la imagen en {profile_image_path}")
        st.markdown('<div style="text-align: center;">👤</div>', unsafe_allow_html=True)



# Enlaces a redes sociales (reemplaza con tus propios enlaces)
whatsapp_url = "https://wa.me/034613394587"  # Cambia a tu número de WhatsApp (formato: https://wa.me/NUMEROCOMPLETO)
facebook_url = "https://www.facebook.com/profile.php?id=61575046444513"  # Cambia a tu perfil de Facebook
instagram_url = "https://www.instagram.com/lorenzobucaros/"  # Cambia a tu perfil de Instagram
tiktok_url = "https://www.tiktok.com/@bucaros_madrid_lorenzo?lang=es"  # Cambia a tu perfil de TikTok

# Función para generar archivo CSV de contacto
def get_contact_csv():
    # Personaliza esta información con tus datos
    nombre = "Bucaros Madrid Lorenzo"
    telefono = "+34613394587"
    email = "bucaroslorenzo@gmail.com"
    empresa = "Bucaros Madrid"
    cargo = "Distribuidor Productos Colombianos"
    
    csv_content = f"""BEGIN:VCARD
VERSION:3.0
N:Bucaros
FN:Madrid Lorenzo
ORG:Bucaros Madrid
TITLE:Distribuidor Productos Colombianos
TEL;TYPE=CELL:613394587
EMAIL:bucaroslorenzo@gmail.com
END:VCARD"""
    
    return csv_content

# Función para crear un link de descarga
def get_download_link(content, filename, link_text):
    """Genera un link para descargar un archivo con el contenido dado"""
    b64 = base64.b64encode(content.encode()).decode()
    href = f'<a href="data:text/plain;base64,{b64}" download="{filename}" class="social-button contact">{link_text}</a>'
    return href

# Mostrar botones de redes sociales
st.markdown(f'<a href="{whatsapp_url}" target="_blank" class="social-button whatsapp">WhatsApp</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{facebook_url}" target="_blank" class="social-button facebook">Facebook</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{instagram_url}" target="_blank" class="social-button instagram">Instagram</a>', unsafe_allow_html=True)
st.markdown(f'<a href="{tiktok_url}" target="_blank" class="social-button tiktok">TikTok</a>', unsafe_allow_html=True)

# Link para descargar contacto CSV
contact_csv = get_contact_csv()
st.markdown(get_download_link(contact_csv, "contacto.vcf", "Añadir a contactos"), unsafe_allow_html=True)

# Pie de página
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>© 2025 - Bucaros Madrid Digital</p>", unsafe_allow_html=True)
        
