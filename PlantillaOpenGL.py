from OpenGL.GL import *
from glew_wish import *
import glfw
from math import *

def dibujarCasa():
    glBegin(GL_QUADS)
    glColor3f(.9, .9, .6)
    glVertex3f(-0.5, 0.3, 0.0)
    glVertex3f(0.5, 0.3, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(-0.5, -0.5, 0.0)

    glEnd()


def dibujarTecho():

 #rutinas de dibujo
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0, 0)
    glVertex3f(0.0, 0.8, 0.0)
    #glColor3f(1.0, 0.8, 0)
    glVertex3f(-.6, 0.3, 0.0)
    #glColor3f(1.0, 0, 1.0)
    glVertex3f(.6,.3,0)



    glEnd()

def dibujarPasto():
    glBegin(GL_QUADS)
    glColor3f(0, .9, 0.0)
    glVertex3f(1, -.5, 0.0)
    glVertex3f(-1, -.5, 0.0)
    glVertex3f(-1, -1, 0.0)
    glVertex3f(1, -1, 0.0)

    glEnd()

def dibujarPuerta():
    glBegin(GL_QUADS)
    
    glColor3f(0.4, 0.2, 0.1)

    glVertex3f(0.1, 0.0, 0.0)
    glVertex3f(0.4, .0, 0.0)
    glVertex3f(0.4, -.5, 0.0)
    glVertex3f(0.1, -.5, 0.0)
    
    

    glEnd()

def dibujarManija():
    glBegin(GL_QUADS)

    glColor3f(0.9, 1, 0)

    glVertex3f(0.37, -0.3, 0.0)
    glVertex3f(0.37, -0.28, 0.0)
    glVertex3f(0.3, -0.28, 0.0)
    glVertex3f(0.3, -0.3, 0.0)
    



    glEnd()    

def dibujarVentana():
    glBegin(GL_QUADS)

    glColor3f(0.,0.8,0.9)

    glVertex3f(-0.4, .2, 0.0)
    glVertex3f(-0.4, -.1, 0.0)
    glVertex3f(-0.1, -.1, 0.0)
    glVertex3f(-0.1, 0.2, 0.0)

    glEnd()

def dibujarSol():
    glColor3f(.9,1, .1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.2 - 0.7 ,sin (angulo) * 0.2 + .75 ,0.0)
    glEnd()

def dibujarRayo1():
    glBegin(GL_QUADS)

    glColor3f(.9,1, .1)

    glVertex3f(-0.5, .7, 0.0)
    glVertex3f(-0.4, .7, 0.0)
    glVertex3f(-0.4, .72, 0.0)
    glVertex3f(-0.5, 0.72, 0.0)
    

    glEnd()

def dibujarRayo2():
    glBegin(GL_QUADS)

    glColor3f(.9,1, .1)

    glVertex3f(-0.55, .6, 0.0)
    glVertex3f(-0.48, .6, 0.0)
    glVertex3f(-0.48, .62, 0.0)
    glVertex3f(-0.55, 0.62, 0.0)
    

    glEnd()

def dibujarRayo3():
    glBegin(GL_QUADS)

    glColor3f(.9,1, .1)

    glVertex3f(-0.5, .8, 0.0)
    glVertex3f(-0.43, .8, 0.0)
    glVertex3f(-0.43, .82, 0.0)
    glVertex3f(-0.5, 0.82, 0.0)
    

    glEnd()
    
def dibujarTronco():
    glBegin(GL_QUADS)
    
    glColor3f(0.4, 0.2, 0.1)

    glVertex3f(-0.61, 0.0, 0.0)
    glVertex3f(-0.8, .0, 0.0)
    glVertex3f(-0.8, -.5, 0.0)
    glVertex3f(-0.61, -.5, 0.0)
    
    

    glEnd()

def dibujarRama():
    glColor3f(.2,.4,.2)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.2 - 0.7 ,sin (angulo) * 0.2 + .1 ,0.0)
    glEnd()

def dibujarNube1():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.2 + .5 ,sin (angulo) * 0.1 + .7 ,0.0)
    glEnd()

def dibujarNube2():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.2 + .7 ,sin (angulo) * 0.1 + .7 ,0.0)
    glEnd()

def dibujarNube3():
    glColor3f(1,1,1)
    glBegin(GL_POLYGON)
    for x in range(360):
        angulo = x * 3.14159 / 180.0
        glVertex3f(cos (angulo) * 0.2 + .6 ,sin (angulo) * 0.1 + .55 ,0.0)
    glEnd()






def dibujar():
    dibujarCasa()
    dibujarTecho()
    dibujarPasto()
    dibujarPuerta()
    dibujarVentana()
    dibujarManija()
    dibujarSol()
    dibujarRayo1()
    dibujarRayo2()
    dibujarRayo3()
    dibujarTronco()
    dibujarRama()
    dibujarNube1()
    dibujarNube2()
    dibujarNube3()
    


def main():
    #inicia glfw
    ancho= 800
    alto = 800
    if not glfw.init():
        return
    
    #crea la ventana, 
    # independientemente del SO que usemos
    window = glfw.create_window(ancho,alto,"Mi ventana", None, None)

    #Configuramos OpenGL
    glfw.window_hint(glfw.SAMPLES, 4)
    glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
    glfw.window_hint(glfw.CONTEXT_VERSION_MINOR,3)
    glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL_TRUE)
    glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)

    #Validamos que se cree la ventana
    if not window:
        glfw.terminate()
        return
    #Establecemos el contexto
    glfw.make_context_current(window)

    #Activamos la validación de 
    # funciones modernas de OpenGL
    glewExperimental = True

    #Inicializar GLEW
    if glewInit() != GLEW_OK:
        print("No se pudo inicializar GLEW")
        return

    #Obtenemos versiones de OpenGL y Shaders
    version = glGetString(GL_VERSION)
    print(version)

    version_shaders = glGetString(GL_SHADING_LANGUAGE_VERSION)
    print(version_shaders)

    while not glfw.window_should_close(window):
        #Establece regiond e dibujo
        glViewport(0,0, ancho, alto)
        #Establece color de borrado
        glClearColor(0.,0.8,0.9,1)
        #Borra el contenido de la ventana
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #Dibujar
        dibujar()

        #Preguntar si hubo entradas de perifericos
        #(Teclado, mouse, game pad, etc.)
        glfw.poll_events()
        #Intercambia los buffers
        glfw.swap_buffers(window)

    #Se destruye la ventana para liberar memoria
    glfw.destroy_window(window)
    #Termina los procesos que inició glfw.init
    glfw.terminate()

if __name__ == "__main__":
    main()