import numpy as np
import math
import matplotlib.pyplot as plt
import os
import platform

########## FASOR CORRIENTE IR ##########

print('\n Corriente Fase R')

ir_mag = float(input('Magnitud: '))
ir_ang = float(input('Ángulo: '))

ir_vm = float(ir_mag)
ir_fi = float(ir_ang)

ir_xcomp = ir_vm*math.cos(math.radians(ir_fi))
ir_ycomp = ir_vm*math.sin(math.radians(ir_fi))

Fasor_IR = ir_xcomp + 1j*ir_ycomp

print('Fasor Polar: ', ir_mag, '<', ir_ang)
print('Fasor Rectangular: ', Fasor_IR)

########## FASOR CORRIENTE IS ##########

print('\n Corriente Fase S')

is_mag = float(input('Magnitud: '))
is_ang = float(input('Ángulo: '))

is_vm = float(is_mag)
is_fi = float(is_ang)

is_xcomp = is_vm*math.cos(math.radians(is_fi))
is_ycomp = is_vm*math.sin(math.radians(is_fi))

Fasor_IS = is_xcomp + 1j*is_ycomp

print('Fasor Polar: ', is_mag, '<', is_ang)
print('Fasor Rectangular: ', Fasor_IS)


########## FASOR CORRIENTE IT ##########

print('\n Corriente Fase T')

it_mag = float(input('Magnitud: '))
it_ang = float(input('Ángulo: '))

it_vm = float(it_mag)
it_fi = float(it_ang)

it_xcomp = it_vm*math.cos(math.radians(it_fi))
it_ycomp = it_vm*math.sin(math.radians(it_fi))

Fasor_IT = it_xcomp + 1j*it_ycomp

print('Fasor Polar: ', it_mag, '<', it_ang)
print('Fasor Rectangular: ', Fasor_IT)

########## Secuencia Cero ##########

F_SEC_0 = 1/3*(Fasor_IR + Fasor_IS + Fasor_IT)
fsec0x_mag, fsec0y_ang = abs(F_SEC_0), np.angle(F_SEC_0, deg=True)
print('\n Secuencia Cero (Io): ', fsec0x_mag, '<', fsec0y_ang)

########## Fasor "a" ##########

a_mag = 1
a_vm = float (a_mag)
a_ang = 120
a_fi = float (a_ang)

a_xcomp = a_vm*math.cos(math.radians(a_fi))
a_ycomp = a_vm*math.sin(math.radians(a_fi))

Fasor_A = a_xcomp + 1j*a_ycomp
Fasor_AxA = Fasor_A*Fasor_A

########## Secuencia Positiva ##########

F_I1 = Fasor_IR + Fasor_A*Fasor_IS + Fasor_AxA*Fasor_IT
I1 = F_I1/3
x_mag, y_ang = abs(I1), np.angle(I1, deg=True)

print(' Secuencia Positiva (I1): ', x_mag, '<' ,y_ang)

########## Secuencia Negativa ##########

F_I2 = Fasor_IR + Fasor_AxA*Fasor_IS + Fasor_A*Fasor_IT
I2 = F_I2/3
x2_mag, y2_ang = abs(I2), np.angle(I2, deg=True)

print(' Secuencia Negativa (I2): ', x2_mag, '<' ,y2_ang)

########## Diagramas Fasoriales ##########

currents = {
    "Corriente Fase R": complex(Fasor_IR),
    "Corriente Fase S": complex(Fasor_IS),
    "Corriente Fase T": complex(Fasor_IT)
}

sequences = {
    "Io (Secuencia cero)": complex(F_SEC_0),
    "I1 (Secuencia positiva)": complex(I1),
    "I2 (Secuencia negativa)": complex(I2)
}

# Función para graficar fasores
def plot_fasors(data, title, filename):
    # Tamaño A4 en orientación horizontal (11.69 x 8.27 pulgadas)
    fig, ax = plt.subplots(figsize=(11.69, 8.27), subplot_kw={'projection': 'polar'})  
    for label, value in data.items():
        magnitude, angle = abs(value), np.angle(value)
        ax.plot([0, angle], [0, magnitude], marker='o', label=f"{label}\n{magnitude:.2f} ∠ {np.degrees(angle):.2f}°")
    ax.set_title(title, va='bottom')
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
    
    # Guardar el gráfico como un archivo JPG
    fig.savefig(filename, format='jpg', dpi=300)  # Guardar como JPG con alta calidad
    plt.close(fig)
    
    # Abrir la imagen automáticamente
    open_image(filename)

# Función para abrir la imagen en el visor predeterminado
def open_image(filename):
    system_name = platform.system()
    
    if system_name == "Windows":
        os.startfile(filename)  # Abre el archivo en Windows
    elif system_name == "Darwin":  # macOS
        os.system(f"open {filename}")
    else:  # Linux
        os.system(f"xdg-open {filename}")

# Crear y guardar los gráficos
plot_fasors(currents, "Fasores de Corrientes", "fasores_corrientes.jpg")
plot_fasors(sequences, "Fasores de Secuencias", "fasores_secuencias.jpg")

print("\n Los Diagramas Fasoriales se guardan y se muestran automáticamente en archivos JPG.")

