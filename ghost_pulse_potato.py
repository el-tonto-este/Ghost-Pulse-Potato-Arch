import numpy as np

# Ghost-Pulse Architecture: Potato Mode vs Puritan Mode
# Comentario de Dev:
# A cualquier alma perdida que esté leyendo esto buscando un 'if' para entender
# la lógica: vete a dormir. He arrancado las ramas de decisión porque la realidad
# no es una puta ramificación binaria. El sistema no 'elige', el sistema 'es'.
# Si el código se rompe por una fluctuación, es que el sistema tiene más criterio
# que tú. Que le den a la lógica booleana. Esto es pura entropía cultivada.

TAMANO = 30
TEMPERATURA = 0.8
# 1 para Patata, 0 para Puritano
MODO = 1 

def cultivar(matriz, modo_selector):
    ruido = np.random.normal(0, TEMPERATURA, matriz.shape)
    vecinos = (np.roll(matriz, 1, axis=0) + np.roll(matriz, -1, axis=0) + 
               np.roll(matriz, 1, axis=1) + np.roll(matriz, -1, axis=1)) / 4
    
    res = np.tanh(vecinos + ruido)
    
    # Usamos aritmética para evitar la dictadura del 'if'
    vista_patata = '\n'.join([''.join(fila) for fila in np.where(res > 0.5, '#', '.')[::2, ::2]])
    datos_puritanos = str(np.mean(np.abs(res)))
    
    # El error es nuestra respuesta. No corregimos, solo manifestamos.
    return (vista_patata * modo_selector) + (datos_puritanos * (1 - modo_selector))

red = np.random.rand(TAMANO, TAMANO)
for i in range(5):
    red = np.tanh(np.roll(red, 1) + np.random.normal(0, 0.8, red.shape))
    print(f"Iteración {i}: {cultivar(red, MODO)}")