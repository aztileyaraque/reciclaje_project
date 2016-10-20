#!/usr/bin/env python
# -*- coding: 850 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'reciclaje_project.settings')

import django
django.setup()

from reciclaje.models import Pregunta, Equipo, UserProfile, Caneca, Residuo, PregRespuesta, User

def populate():
    print "####---- Comienza Populate ----####"
    print "####---- Equipo ----####"
    equipoUno = add_equipo(nombre="Uno",numero=1)
    equipoDos = add_equipo(nombre="Dos",numero=2)
    equipoTres = add_equipo(nombre="Tres",numero=3)
    equipoCuatro = add_equipo(nombre="Cuatro",numero=4)
    equipoCinco = add_equipo(nombre="Cinco",numero=5)
    equipoSeis = add_equipo(nombre="Seis",numero=6)
    equipoSiete = add_equipo(nombre="Siete",numero=7)
    equipoOcho = add_equipo(nombre="Ocho",numero=8)
    equipoNueve = add_equipo(nombre="Nueve",numero=9)
    print "####---- Usuarios ----####"
    usuarioUno = add_usuario(username="jhenao", password="3158649287", first_name="JORGE", last_name="HENAO", equipo=equipoUno)
    usuarioDos = add_usuario(username="mruiza", password="3157972169", first_name="MERLY", last_name="RUIZ ARDILA", equipo=equipoUno)
    usuarioTres = add_usuario(username="zsanchez", password="3165263029", first_name="ZAIDA", last_name="SANCHEZ", equipo=equipoUno)
    usuarioCuatro = add_usuario(username="nmejia", password="3176470752", first_name="NANCY", last_name="MEJIA", equipo=equipoUno)
    usuarioCinco = add_usuario(username="arubiano", password="3176379332", first_name="ALEXANDRA", last_name="RUBIANO", equipo=equipoUno)
    usuarioSeis = add_usuario(username="hgonzalez", password="3176427161", first_name="HERLIX", last_name="GONZALEZ", equipo=equipoUno)
    usuarioSiete = add_usuario(username="nlopez", password="3104451799", first_name="NELLY", last_name="LOPEZ", equipo=equipoUno)
    usuarioOcho = add_usuario(username="npalacios", password="3114667227", first_name="NATALIA", last_name="PALACIOS", equipo=equipoUno)
    usuarioNueve = add_usuario(username="scuervo", password="3152574033", first_name="SANDRA", last_name="CUERVO", equipo=equipoUno)
    usuarioDiez = add_usuario(username="agonzalez", password="3152574041", first_name="ANYELA", last_name="GONZALEZ", equipo=equipoUno)
    usuarioOnce = add_usuario(username="druiz", password="3152573864", first_name="DIANA", last_name="RUIZ", equipo=equipoUno)
    usuarioDoce = add_usuario(username="eochoa", password="3183701745", first_name="ERROL", last_name="OCHOA", equipo=equipoUno)
    usuarioTrece = add_usuario(username="alopez", password="3158957827", first_name="ANDERSON", last_name="LOPEZ", equipo=equipoDos)
    usuariCatorce = add_usuario(username="wguiral", password="3165235358", first_name="WILSON", last_name="GUIRAL", equipo=equipoDos)
    usuarioQuince = add_usuario(username="ivillada", password="3183902240", first_name="IVAN", last_name="VILLADA", equipo=equipoDos)
    usuarioDieciseis = add_usuario(username="ccortes", password="3152573848", first_name="CARLOS", last_name="CORTES", equipo=equipoDos)
    usuarioDiecisiete = add_usuario(username="opena", password="3175169683", first_name="OMAIRA", last_name="PEÑA", equipo=equipoDos)
    usuarioDieciocho = add_usuario(username="ccontreras", password="3156125796", first_name="CARLOS", last_name="CONTRERAS", equipo=equipoDos)
    usuarioDiecinueve = add_usuario(username="egarzon", password="3118578619", first_name="ELIANA", last_name="GARZON", equipo=equipoDos)
    usuarioVeinte = add_usuario(username="mchurtado", password="3183545280", first_name="MARIA DEL CARMEN", last_name="HURTADO", equipo=equipoDos)
    usuarioVeintiuno = add_usuario(username="maraujo", password="3124595688", first_name="MARIO", last_name="ARAUJO", equipo=equipoDos)
    usuarioVeintidos = add_usuario(username="jlaverde", password="3174031826", first_name="JHON", last_name="LAVERDE", equipo=equipoDos)
    usuarioVeintitres = add_usuario(username="rhernandez", password="3152123568", first_name="RAMIRO", last_name="HERNANDEZ", equipo=equipoDos)
    usuarioVeinticuatro = add_usuario(username="msusa", password="3165275039", first_name="MAYRA", last_name="SUSA", equipo=equipoDos)
    usuarioVeinticinco = add_usuario(username="omoreno", password="3174039041", first_name="OSCAR", last_name="MORENO", equipo=equipoTres)
    usuarioVeintiseis = add_usuario(username="gmora", password="3164653359", first_name="GERMAN", last_name="MORA", equipo=equipoTres)
    usuarioVeintisiete = add_usuario(username="jcuervo", password="3164741504", first_name="JUAN", last_name="CUERVO", equipo=equipoTres)
    usuarioVeintiocho = add_usuario(username="jbeltran", password="3108113560", first_name="JENNY", last_name="BELTRAN", equipo=equipoTres)
    usuarioVeintinueve = add_usuario(username="epulido", password="3153440200", first_name="ERIKA", last_name="PULIDO", equipo=equipoTres)
    usuarioTreinta = add_usuario(username="macuervo", password="3176671701", first_name="MARIA ALEJANDRA", last_name="CUERVO", equipo=equipoTres)
    usuarioTreintaiuno = add_usuario(username="legarcia", password="3158536576", first_name="LUIS EDUARDO", last_name="GARCIA", equipo=equipoTres)
    usuarioTreintaidos = add_usuario(username="lcastaneda", password="3124353461", first_name="LILIANA", last_name="CASTAÑEDA", equipo=equipoTres)
    usuarioTreintaitres = add_usuario(username="jmcalderon", password="3156125805", first_name="JOSE MIGUEL", last_name="CALDERON", equipo=equipoTres)
    usuarioTreintaicuatro = add_usuario(username="nperalta", password="3156471116", first_name="NILTON", last_name="PERALTA", equipo=equipoTres)
    usuarioTreintaicinco = add_usuario(username="jdgalvis", password="3176550141", first_name="JULIAN DAVID", last_name="GALVIS", equipo=equipoTres)
    usuarioTreintaiseis = add_usuario(username="aguarin", password="3152573846", first_name="ARMANDO", last_name="GUARIN", equipo=equipoTres)
    usuarioTreintaisiete = add_usuario(username="apatarroyo", password="3158590447", first_name="ALBERTO", last_name="PATARROYO", equipo=equipoCuatro)
    usuarioTreintaiocho = add_usuario(username="mmoreno", password="3152573859", first_name="MIGUEL", last_name="MORENO", equipo=equipoCuatro)
    usuarioTreintainueve = add_usuario(username="lblanco", password="3184094996", first_name="LUDY", last_name="BLANCO", equipo=equipoCuatro)
    usuarioCuarenta = add_usuario(username="oguzman", password="3158510478", first_name="ORLANDO", last_name="GUZMAN", equipo=equipoCuatro)
    usuarioCuarentaiuno = add_usuario(username="slclavijo", password="3176458498", first_name="SANDRA LORENA", last_name="CLAVIJO", equipo=equipoCuatro)
    usuarioCuarentaidos = add_usuario(username="gavila", password="3112704971", first_name="GLADYS", last_name="AVILA", equipo=equipoCuatro)
    usuarioCuarentaitres = add_usuario(username="ngarzon", password="3164647562", first_name="NICOLAS", last_name="GARZON", equipo=equipoCuatro)
    usuarioCuarentaicuatro = add_usuario(username="mbenavides", password="3152578858", first_name="MARIA", last_name="BENAVIDES", equipo=equipoCuatro)
    usuarioCuarentaicinco = add_usuario(username="lvcastilla", password="3173712876", first_name="LUZ VICTORIA", last_name="CASTILLA", equipo=equipoCuatro)
    usuarioCuarentaiseis = add_usuario(username="mpena", password="3152953452", first_name="MARCO", last_name="PEÑA", equipo=equipoCuatro)
    usuarioCuarentaisiete = add_usuario(username="hpatino", password="3158980276", first_name="HAROLD", last_name="PATIÑO", equipo=equipoCuatro)
    usuarioCuarentaiocho = add_usuario(username="oorozco", password="3158747735", first_name="OLGA", last_name="OROZCO", equipo=equipoCuatro)
    usuarioCuarentainueve = add_usuario(username="bguerrero", password="3112002741", first_name="BERTHA", last_name="GUERRERO", equipo=equipoCinco)
    usuarioCincuenta = add_usuario(username="jwduque", password="3182617780", first_name="JHON WILSON", last_name="DUQUE", equipo=equipoCinco)
    usuarioCincuentaiuno = add_usuario(username="jarozo", password="3158317839", first_name="JAIR ALBEIRO", last_name="ROZO", equipo=equipoCinco)
    usuarioCincuentaidos = add_usuario(username="omogollon", password="3158747747", first_name="OLGA", last_name="MOGOLLON", equipo=equipoCinco)
    usuarioCincuentaitres = add_usuario(username="npadilla", password="3214661556", first_name="NARDA", last_name="PADILLA", equipo=equipoCinco)
    usuarioCincuentaicuatro = add_usuario(username="svargas", password="3155602605", first_name="SERGIO", last_name="VARGAS", equipo=equipoCinco)
    usuarioCincuentaicinco = add_usuario(username="lduque", password="3164724737", first_name="LINCONL", last_name="DUQUE", equipo=equipoCinco)
    usuarioCincuentaiseis = add_usuario(username="miotalvaro", password="3174322031", first_name="MARIA IDALBA", last_name="OTALVARO", equipo=equipoCinco)
    usuarioCincuentaisiete = add_usuario(username="clvelasquez", password="3134224685", first_name="CARMEN LILIANA", last_name="VELASQUEZ", equipo=equipoCinco)
    usuarioCincuentaiocho = add_usuario(username="apastrana", password="3168785697", first_name="ALEXANDER", last_name="PASTRANA", equipo=equipoCinco)
    usuarioCincuentainueve = add_usuario(username="mhiguera", password="3174278283", first_name="MARTHA", last_name="HIGUERA", equipo=equipoCinco)
    usuarioSesenta = add_usuario(username="srincon", password="3173833191", first_name="SANDRA", last_name="RINCON", equipo=equipoCinco)
    usuarioSesentaiuno = add_usuario(username="cherrera", password="3158551947", first_name="CESAR", last_name="HERRERA", equipo=equipoSeis)
    usuarioSesentaidos = add_usuario(username="jarboleda", password="3168785697", first_name="JAIME", last_name="ARBOLEDA", equipo=equipoSeis)
    usuarioSesentaitres = add_usuario(username="ptaborda", password="3137835804", first_name="PATRICIA", last_name="TABORDA", equipo=equipoSeis)
    usuarioSesentaicuatro = add_usuario(username="ghernandez", password="3158317844", first_name="GUIDO", last_name="HERNANDEZ", equipo=equipoSeis)
    usuarioSesentaicinco = add_usuario(username="abeltran", password="3188370842", first_name="ADRIANA", last_name="BELTRAN", equipo=equipoSeis)
    usuarioSesentaiseis = add_usuario(username="jmchica", password="3163028775", first_name="JOSE MARIA", last_name="CHICA", equipo=equipoSeis)
    usuarioSesentaisiete = add_usuario(username="esampedro", password="3152574022", first_name="ENRIQUE", last_name="SAMPEDRO", equipo=equipoSeis)
    usuarioSesentaiocho = add_usuario(username="rdavila", password="3158395146", first_name="RUBIELA", last_name="DAVILA", equipo=equipoSeis)
    usuarioSesentainueve = add_usuario(username="lsgodoy", password="3164346774", first_name="LUZ STELLA", last_name="GODOY", equipo=equipoSeis)
    usuarioSetenta = add_usuario(username="ddiaz", password="3172670254", first_name="DORALBA", last_name="DIAZ", equipo=equipoSeis)
    usuarioSetentaiuno = add_usuario(username="lmlinares", password="3152603227", first_name="LUZ MARINA", last_name="LINARES", equipo=equipoSeis)
    usuarioSetentaidos = add_usuario(username="vrubiano", password="3152574038", first_name="VICTOR", last_name="RUBIANO", equipo=equipoSeis)
    usuarioSetentaitres = add_usuario(username="jctorres", password="3152573860", first_name="JUAN CARLOS", last_name="TORRES", equipo=equipoSiete)
    usuarioSetentaicuatro = add_usuario(username="jforero", password="3152574030", first_name="JULIETH", last_name="FORERO", equipo=equipoSiete)
    usuarioSetentaicinco = add_usuario(username="jhacevedo", password="3164740795", first_name="JHON HEVER", last_name="ACEVEDO", equipo=equipoSiete)
    usuarioSetentaiseis = add_usuario(username="uruiz", password="3164690398", first_name="URIEL", last_name="RUIZ", equipo=equipoSiete)
    usuarioSetentaisiete = add_usuario(username="mgomez", password="3182575278", first_name="MAURICIO", last_name="GOMEZ", equipo=equipoSiete)
    usuarioSetentaiocho = add_usuario(username="lescorcia", password="3174313272", first_name="LISETH", last_name="ESCORCIA", equipo=equipoSiete)
    usuarioSetentainueve = add_usuario(username="mhruiz", password="3212512005", first_name="MARIA HELENA", last_name="RUIZ", equipo=equipoSiete)
    usuarioOchenta = add_usuario(username="wsanchez", password="3153311847", first_name="WILMAN", last_name="SANCHEZ", equipo=equipoSiete)
    usuarioOchentaiuno = add_usuario(username="rrivera", password="3183544807", first_name="ROGER", last_name="RIVERA", equipo=equipoSiete)
    usuarioOchentaidos = add_usuario(username="mmaldonado", password="3183585001", first_name="MAURICIO", last_name="MALDONADO", equipo=equipoSiete)
    usuarioOchentaitres = add_usuario(username="ysanchez", password="3164721656", first_name="YAMILE", last_name="SANCHEZ", equipo=equipoSiete)
    usuarioOchentaicuatro = add_usuario(username="yracines", password="3156437238", first_name="YOLIMA", last_name="RACINES", equipo=equipoSiete)
    usuarioOchentaicinco = add_usuario(username="bmaldonado", password="3156471117", first_name="BROVIN", last_name="MALDONADO", equipo=equipoOcho)
    usuarioOchentaiseis = add_usuario(username="jjimenez", password="3168785670", first_name="JAVIER", last_name="JIMENEZ", equipo=equipoOcho)
    usuarioOchentaisiete = add_usuario(username="lmmurillo", password="3153385820", first_name="LINA MARIA", last_name="MURILLO", equipo=equipoOcho)
    usuarioOchentaiocho = add_usuario(username="ylozano", password="3168033284", first_name="YADY", last_name="LOZANO", equipo=equipoOcho)
    usuarioOchentainueve = add_usuario(username="gjburgos", password="3173364677", first_name="GONZALO JAVIER", last_name="BURGOS", equipo=equipoOcho)
    usuarioNoventa = add_usuario(username="sposso", password="3183569535", first_name="SANDRA", last_name="POSSO", equipo=equipoOcho)
    usuarioNoventaiuno = add_usuario(username="mvgranados", password="3165235209", first_name="MARIA VICTORIA", last_name="GRANADOS", equipo=equipoOcho)
    usuarioNoventaidos = add_usuario(username="brincon", password="3156298280", first_name="BETHY", last_name="RINCON", equipo=equipoOcho)
    usuarioNoventaitres = add_usuario(username="ltovar", password="3183701743", first_name="LUIS", last_name="TOVAR", equipo=equipoOcho)
    usuarioNoventaicuatro = add_usuario(username="jmperalta", password="3165276893", first_name="JOSE MAURICIO", last_name="PERALTA", equipo=equipoOcho)
    usuarioNoventaicinco = add_usuario(username="jmmartinez", password="3164482826", first_name="JUAN MANUEL", last_name="MARTINEZ", equipo=equipoOcho)
    usuarioNoventaiseis = add_usuario(username="jjfernandez", password="3153872662", first_name="JHON JAIRO", last_name="FERNANDEZ", equipo=equipoNueve)
    usuarioNoventaisiete = add_usuario(username="fapolinar", password="3173660345", first_name="FABIAN", last_name="APOLINAR", equipo=equipoNueve)
    usuarioNoventaiocho = add_usuario(username="jmaldonado", password="3164721611", first_name="JAIME", last_name="MALDONADO", equipo=equipoNueve)
    usuarioNoventainueve = add_usuario(username="jevelasquez", password="3165235364", first_name="JUAN ESTEBAN", last_name="VELASQUEZ", equipo=equipoNueve)
    usuarioCien = add_usuario(username="mordonez", password="3152573843", first_name="MARCELA", last_name="ORDOÑEZ", equipo=equipoNueve)
    usuarioCientouno = add_usuario(username="gjmendoza", password="3164540418", first_name="GUSTAVO DE JESUS", last_name="MENDOZA", equipo=equipoNueve)
    usuarioCientodos = add_usuario(username="rabondano", password="3152574035", first_name="RODRIGO", last_name="ABONDANO", equipo=equipoNueve)
    usuarioCientotres = add_usuario(username="emera", password="3153464615", first_name="EDGAR", last_name="MERA PATIÑO", equipo=equipoNueve)
    usuarioCientocuatro = add_usuario(username="apguio", password="3152573845", first_name="ADRIANA PAOLA", last_name="GUIO", equipo=equipoNueve)
    usuarioCientocinco = add_usuario(username="jcruz", password="3152123568", first_name="JOHAN", last_name="CRUZ", equipo=equipoNueve)
    usuarioCientoseis = add_usuario(username="aguerra", password="3165250155", first_name="AIDA", last_name="GUERRA", equipo=equipoNueve)
    usuarioCientosiete = add_usuario(username="baltamar", password="3174280837", first_name="BREITNER", last_name="ALTAMAR", equipo=equipoNueve)
    print "####---- Preguntas ----####"
    pregUno = add_pregunta(enunciado="Cualquier persona cuya actividad produzca residuos, se denomina:", respuestaCorrecta="a. Generador de residuos.")
    pregDos = add_pregunta(enunciado="Persona natural o jurídica que presta los servicios de recolección, transporte, tratamiento, aprovechamiento o disposición final de residuos peligrosos, se denomina:", respuestaCorrecta="b.Gestor o receptor de residuos.")
    pregTres = add_pregunta(enunciado="Qué deberías hacer con las bolsas plásticas que se generan cuando compras mercado, ropa, utensilios, etc:", respuestaCorrecta="d. b y c")
    pregCuatro = add_pregunta(enunciado="Qué tipo de producto es recomendable comprar:", respuestaCorrecta="a. Uno con poco embalaje, o en el caso de algunos alimentos, comprarlos al peso en lugar de envasados.")
    pregCinco = add_pregunta(enunciado="Responda Falso o Verdadero: \n Un residuo o desecho peligroso es aquel que por sus características corrosivas, reactivas, explosivas, tóxicas, inflamables, infecciosas o radiactivas puede causar riesgo o daño para la salud humana y el ambiente.", respuestaCorrecta="Verdadero")
    pregSeis = add_pregunta(enunciado="Responda Falso o Verdadero: \n El Reciclaje consiste en disponer los residuos en un relleno sanitario.", respuestaCorrecta="Falso")
    pregSiete = add_pregunta(enunciado="Responda Falso o Verdadero: \n Los residuos no tienen ningún valor, por lo que siempre deben ir al basurero.", respuestaCorrecta="Falso")
    pregOcho = add_pregunta(enunciado="Responda Falso o Verdadero: \n El compost (restos de frutas, verduras, hojas, etc) es un fertilizante natural usado para abonar el campo.", respuestaCorrecta="Verdadero")
    pregNueve = add_pregunta(enunciado="Responda Falso o Verdadero: \n Las envolturas o envase de comida, aluminio con restos de comida, las servilletas usadas deben ir al contenedor verde.", respuestaCorrecta="Verdadero")
    pregDiez = add_pregunta(enunciado="Dónde se deben depositar los cartones usados:", respuestaCorrecta="c. Contenedor azul o gris.")
    pregOnce = add_pregunta(enunciado="¿De dónde procede el papel?", respuestaCorrecta="a. De los árboles.")
    pregDoce = add_pregunta(enunciado="Reducir significa:", respuestaCorrecta="a. Evitar que se genere la basura comprando más sabiamente y utilizando los productos de la manera correcta.")
    pregTrece = add_pregunta(enunciado="Reutilizar significa:", respuestaCorrecta="c. a y b.")
    pregCatorce = add_pregunta(enunciado="El papel de aluminio con residuos de comida se deposita en:", respuestaCorrecta="Contenedor verde.")
    pregQuince = add_pregunta(enunciado="Son todos aquellos residuos que pueden volver a ser aprovechados, recuperados y utilizados en procesos productivos como materia prima:", respuestaCorrecta="c. Residuos reciclables.")
    pregDieciseis = add_pregunta(enunciado="Son aquellos generados en el desempeño normal de las actividades que por su naturaleza, composición, volumen es recolectado, tratado o dispuesto por la prestadora del servicio público de aseo y es llevado a un relleno sanitario:", respuestaCorrecta="a. Residuos ordinarios.")
    pregDiecisiete = add_pregunta(enunciado="Son aquellos residuos infecciosos, combustibles, inflamables, explosivos, reactivos, radiactivos, volátiles, corrosivos y/o tóxicos; las cuales pueden causar daño a la salud humana y/o al medio ambiente:", respuestaCorrecta="b. Residuos peligrosos.")
    pregDieciocho = add_pregunta(enunciado="Son los restos de sustancias químicas y sus empaques o cualquier otro residuo contaminado con éstos:", respuestaCorrecta="d. Residuos peligrosos - químicos.")
    pregDiecinueve = add_pregunta(enunciado="Son aquellos medicamentos vencidos, deteriorados y/o excedentes de sustancias que han sido empleadas en cualquier tipo de procedimiento, dentro de los cuales se incluyen los fraudulentos, alterados y sus empaques:", respuestaCorrecta="a. Fármacos parcialmente consumidos, vencidos y/o deteriorados.")
    pregVeinte = add_pregunta(enunciado="Responda Falso o Verdadero: \n Dentro de las oficinas si se tiene caneca, ésta debe estar con bolsa blanca para los residuos que se pueden reciclar como papel, cartón, etc.", respuestaCorrecta="Verdadero")
    pregVeintiuno = add_pregunta(enunciado="Los residuos generados en la empresa pueden ser entregados a:", respuestaCorrecta="c. Persona o empresa autorizada legalmente.")
    pregVeintidos = add_pregunta(enunciado="Son ejemplos de disposición final de residuos:", respuestaCorrecta="e. a y b.")
    pregVeintitres = add_pregunta(enunciado="Los residuos ordinarios deben ser dispuestos en:", respuestaCorrecta="a. Relleno sanitario.")
    pregVeinticuatro = add_pregunta(enunciado="¿Qué puedo hacer como ciudadano responsable de los residuos que genero?", respuestaCorrecta="e. b y c.")
    pregVeinticinco = add_pregunta(enunciado="¿Qué debo hacer con residuos como pilas, tóner, baterías?", respuestaCorrecta="b. Separarlos y entregarlos a un gestor autorizado.")
    pregVeintiseis = add_pregunta(enunciado="Es el depósito temporal de residuos, en un espacio físico definido y por un tiempo determinado previo a su aprovechamiento, tratamiento y/o disposición final:", respuestaCorrecta="b. Almacenamiento")
    pregVeintisiete = add_pregunta(enunciado="La disposición final consiste en:", respuestaCorrecta="a. Depositar temporalmente los residuos, en un espacio físico definido y por un tiempo determinado.")
    pregVeintiocho = add_pregunta(enunciado="El reciclaje consiste en:", respuestaCorrecta="d. a y c")
    pregVeintinueve = add_pregunta(enunciado="El reciclaje puede constar de:", respuestaCorrecta="d. a y b")
    pregTreinta = add_pregunta(enunciado="Qué es un residuo:", respuestaCorrecta="a. Cualquier objeto, material, sustancia, producto cuyo generador descarta, rechaza o entrega porque sus propiedades no permiten usarlo nuevamente en la actividad que lo generó.")
    pregTreintaiuno = add_pregunta(enunciado="Responda Falso o Verdadero: \n Las latas y envases de plástico deben ir al contenedor azul o gris.", respuestaCorrecta="Verdadero")
    pregTreintaidos = add_pregunta(enunciado="Responda Falso o Verdadero: \n El contenedor verde es sólo para envases de vidrio.", respuestaCorrecta="Falso")
    pregTreintaitres = add_pregunta(enunciado="Responda Falso o Verdadero: \n Las servilletas usadas deben ir al contenedor azul.", respuestaCorrecta="Falso")
    pregTreintaicuatro = add_pregunta(enunciado="Se relaciona con el término Reciclar:", respuestaCorrecta="d. a y c")
    pregTreintaicinco = add_pregunta(enunciado="¿Dónde arrojo un vaso de cristal?", respuestaCorrecta="d. Contenedor azul o gris")
    pregTreintaiseis = add_pregunta(enunciado="Son aquellos residuos que se descomponen fácilmente en el ambiente:", respuestaCorrecta="d. Residuos biodegradables.")
    pregTreintaisiete = add_pregunta(enunciado="Son todos aquellos elementos utilizados durante la ejecución de los procedimientos asistenciales que tienen contacto con materia orgánica, sangre o fluidos corporales del paciente humano o animal tales como: gasas, apósitos, aplicadores, algodones, drenes, vendajes:", respuestaCorrecta="c. Residuos peligrosos - biosanitarios.")
    pregTreintaiocho = add_pregunta(enunciado="Son considerados residuos peligrosos:", respuestaCorrecta="Pilas y bombillos.")
    pregTreintainueve = add_pregunta(enunciado="El relleno sanitario es:", respuestaCorrecta="b. El relleno sanitario consiste en depositar en un sitio controlado en el que se esparcen los residuos y se compactan reduciéndolos al menor volumen posible para que así ocupen un área pequeña. Luego se cubren con una capa de tierra y se compactan nuevamente al terminar el día.")
    pregCuarenta = add_pregunta(enunciado="Son ejemplos de disposición final de residuos peligrosos:", respuestaCorrecta="d. a y b")
    pregCuarentaiuno = add_pregunta(enunciado="Responda Falso o Verdadero: \n Manejo Integral de Residuos es la adopción de medidas para la prevención, reducción y separación en la fuente, almacenamiento, transporte, aprovechamiento, tratamiento y/o disposición final, para proteger la salud humana y el ambiente contra los efectos nocivos que puedan derivarse de tales residuos.", respuestaCorrecta="Verdadero")
    pregCuarentaidos = add_pregunta(enunciado="Un recurso energético no renovable es:", respuestaCorrecta="d. Gas natural.")
    pregCuarentaitres = add_pregunta(enunciado="¿Cuál es el material que más tarda en degradarse?", respuestaCorrecta="d. Plástico.")
    pregCuarentaicuatro = add_pregunta(enunciado="¿De dónde procede el plástico?", respuestaCorrecta="b. Del petróleo.")
    pregCuarentaicinco = add_pregunta(enunciado="La Regla de las tres “R” en su orden consiste en:", respuestaCorrecta="c. Reducir, reutilizar, reciclar")
    pregCuarentaiseis = add_pregunta(enunciado="¿De dónde procede el cristal?", respuestaCorrecta="b. De la arena.")
    pregCuarentaisiete = add_pregunta(enunciado="Los recursos que se regeneran después de su uso se llaman:", respuestaCorrecta="c. Recursos renovables.")
    pregCuarentaiocho = add_pregunta(enunciado="Los recursos que no se regeneran después de su uso se llaman:", respuestaCorrecta="a. Recursos no renovables.")
    pregCuarentainueve = add_pregunta(enunciado="Un recurso renovable es:", respuestaCorrecta="b. Recurso natural que se puede restaurar o regenerar por procesos naturales a una velocidad superior a la del consumo por los seres humanos.")
    pregCincuenta = add_pregunta(enunciado="Representa un recurso renovable:", respuestaCorrecta="d. Agua.")
    pregCincuentaiuno = add_pregunta(enunciado="Representa un recurso no renovable:", respuestaCorrecta="c. Petróleo.")
    pregCincuentaidos = add_pregunta(enunciado="Para la disposición final de los residuos peligrosos generados se tendrá en cuenta lo siguiente:", respuestaCorrecta="d. a y b")
    pregCincuentaitres = add_pregunta(enunciado="Responda falso o verdadero \n En Colombia aún no existe legislación que regule el manejo de los residuos peligrosos.", respuestaCorrecta="Falso")
    pregCincuentaicuatro = add_pregunta(enunciado="Responda falso o verdadero \n En Colombia existen normas y legislación sobre sistema de recolección selectiva y gestión ambiental de residuos como pilas y/o acumuladores, computadores.", respuestaCorrecta="Verdadero")
    pregCincuentaicinco = add_pregunta(enunciado="Responda falso o verdadero \n El Plan de gestión de devolución de productos pos consumo consiste en el conjunto de acciones para facilitar la devolución y acopio de productos pos consumo que al desecharse se convierten en residuos peligrosos, con el fin que sean enviados a instalaciones que permitirán su aprovechamiento, tratamiento y/o disposición final controlada.", respuestaCorrecta="Verdadero")
    print "####---- PregRespuestas ----####"
    respUno = add_preResp(nombre="Uno", pregunta=pregUno, 
            respuestaA="a. Generador de residuos.", respuestaB="b. Gestor de residuos.", 
            respuestaC="c. Receptor de residuos.", respuestaD="a. Transportador de residuos.",
            respuestaE=None, respuestaF=None)
    respDos = add_preResp(nombre="Dos", pregunta=pregDos, 
            respuestaA="a. Generador de residuos.", respuestaB="b. Gestor o receptor de residuos.", 
            respuestaC="c. Transportador de residuos.",respuestaD=None,
            respuestaE=None, respuestaF=None)
    respTres = add_preResp(nombre="Tres", pregunta=pregTres, 
            respuestaA="a. Botarlas a la basura directamente.", respuestaB="b. Reutilizarlas varias veces para ir a comprar o almacenar lo que necesites.", 
            respuestaC="c. Usarlas como bolsas de basura en lugar de comprar bolsas para ello.", respuestaD="d. b y c", 
            respuestaE="e. Ninguna",respuestaF=None)
    respCuatro = add_preResp(nombre="Cuatro", pregunta=pregCuatro, 
            respuestaA="a. Uno con poco embalaje, o en el caso de algunos alimentos, comprarlos al peso en lugar de envasados.", respuestaB="b. El que tenga más envases, ya que así estará más fresco y protegido.", 
            respuestaC="c. El que más me guste, sin tener en cuenta el envase.",respuestaD=None,
            respuestaE=None,respuestaF=None)
    respCinco = add_preResp(nombre="Cinco", pregunta=pregCinco, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None, 
            respuestaE=None, respuestaF=None)
    respSeis = add_preResp(nombre="Seis", pregunta=pregSeis, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None, 
            respuestaE=None, respuestaF=None)
    respSiete = add_preResp(nombre="Siete", pregunta=pregSiete, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None, 
            respuestaE=None, respuestaF=None)
    respOcho = add_preResp(nombre="Ocho", pregunta=pregOcho, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None, 
            respuestaE=None, respuestaF=None)
    respNueve = add_preResp(nombre="Nueve", pregunta=pregNueve, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None, 
            respuestaE=None, respuestaF=None)
    respDiez = add_preResp(nombre="Diez", pregunta=pregDiez, 
            respuestaA="a. Contenedor verde.", respuestaB="b. Contenedor rojo.", 
            respuestaC="c. Contenedor azul o gris.",respuestaD=None,
            respuestaE=None, respuestaF=None)
    respOnce = add_preResp(nombre="Once", pregunta=pregOnce, 
            respuestaA="a. De los árboles.", respuestaB="b. De un animal.", 
            respuestaC="c. De los arbustos.", respuestaD="d. Del plástico.", 
            respuestaE=None, respuestaF=None)
    respDoce = add_preResp(nombre="Doce", pregunta=pregDoce, 
            respuestaA="a. Evitar que se genere la basura comprando más sabiamente y utilizando los productos de la manera correcta.", respuestaB="b. Comprar siempre productos con la mayor cantidad de envase.", 
            respuestaC="c. Comprar productos que contaminan el medio ambiente.",respuestaD=None,
            respuestaE=None, respuestaF=None)
    respTrece = add_preResp(nombre="Trece", pregunta=pregTrece, 
            respuestaA="a. Es tratar de darle algún uso o utilidad al residuo antes de tirarlo, por ejemplo, forrar las cajas, frascos o latas y usarlas para guardar cosas.", respuestaB="b. Es usar un producto nuevamente, ya sea para lo mismo o no.", 
            respuestaC="c. a y b.",respuestaD=None,
            respuestaE=None, respuestaF=None)
    respCatorce = add_preResp(nombre="Catorce", pregunta=pregCatorce, 
            respuestaA="a. Contenedor verde.", respuestaB="b. Contenedor rojo.", 
            respuestaC="c. Contenedor azul.", respuestaD="d. Ninguno de los anteriores.", 
            respuestaE=None, respuestaF=None)
    respQuince = add_preResp(nombre="Quince", pregunta=pregQuince, 
            respuestaA="a. Residuos ordinarios.", respuestaB="b. Residuos peligrosos.", 
            respuestaC="c. Residuos reciclables.", respuestaD="d. Residuos orgánicos.",
            respuestaE=None, respuestaF=None)
    respDieciseis = add_preResp(nombre="Dieciseis", pregunta=pregDieciseis, 
            respuestaA="a. Residuos ordinarios.", respuestaB="b. Residuos peligrosos.", 
            respuestaC="c. Residuos reciclables.", respuestaD="d. Residuos biodegradables.", 
            respuestaE=None, respuestaF=None)
    respDiecisiete = add_preResp(nombre="Diecisiete", pregunta=pregDiecisiete, 
            respuestaA="a. Residuos ordinarios.", respuestaB="b. Residuos peligrosos.", 
            respuestaC="c. Residuos reciclables.", respuestaD="d. Residuos biodegradables.",
            respuestaE=None, respuestaF=None)
    respDieciocho = add_preResp(nombre="Dieciocho", pregunta=pregDieciocho, 
            respuestaA="a. Residuos ordinarios.", respuestaB="b. Residuos reciclables.", 
            respuestaC="c. Residuos peligrosos - biosanitarios.", respuestaD="d. Residuos peligrosos - químicos.",
            respuestaE=None, respuestaF=None)
    respDiecinueve = add_preResp(nombre="Diecinueve", pregunta=pregDiecinueve, 
            respuestaA="a. Fármacos parcialmente consumidos, vencidos y/o deteriorados.", respuestaB="b. Residuos reciclables.", 
            respuestaC="c. Residuos peligrosos - biosanitarios.", respuestaD="d. Residuos ordinarios.",
            respuestaE=None, respuestaF=None)
    respVeinte = add_preResp(nombre="Veinte", pregunta=pregVeinte, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respVeintiuno = add_preResp(nombre="Veintiuno", pregunta=pregVeintiuno, 
            respuestaA="a. Cualquier persona.", respuestaB="b. Al vecino.", 
            respuestaC="c. Persona o empresa autorizada legalmente.", respuestaD="d. Al vigilante.", 
            respuestaE=None, respuestaF=None)
    respVeintidos = add_preResp(nombre="Veintidos", pregunta=pregVeintidos, 
            respuestaA="a. Relleno sanitario.", respuestaB="b. Incineración.", 
            respuestaC="c. Disposición en el río.", respuestaD="d. Disposición en la calle.", 
            respuestaE="e. a y b.", respuestaF="f. c y d.")
    respVeintitres = add_preResp(nombre="Veintitres", pregunta=pregVeintitres, 
            respuestaA="a. Relleno sanitario.", respuestaB="b. La calle.", 
            respuestaC="c. Enterrarlos en el patio de la casa.", respuestaD="d. Arrojarlos al río.",
            respuestaE=None, respuestaF=None)
    respVeinticuatro = add_preResp(nombre="Veinticuatro", pregunta=pregVeinticuatro, 
            respuestaA="a. Botarlos a la basura.", respuestaB="b. Separar los residuos.", 
            respuestaC="c. Reutilizar los residuos.", respuestaD="d. Comprar productos que tenga varias envolturas.", 
            respuestaE="e. b y c.", respuestaF=None)
    respVeinticinco = add_preResp(nombre="Veinticinco", pregunta=pregVeinticinco, 
            respuestaA="a. Botarlos a la basura.", respuestaB="b. Separarlos y entregarlos a un gestor autorizado.", 
            respuestaC="c. Tirarlos en la calle.",respuestaD=None,
            respuestaE=None, respuestaF=None)
    respVeintiseis = add_preResp(nombre="Veintiseis", pregunta=pregVeintiseis, 
            respuestaA="a. Disposición final", respuestaB="b. Almacenamiento", 
            respuestaC="c. Reciclaje",respuestaD=None,
            respuestaE=None, respuestaF=None)
    respVeintisiete = add_preResp(nombre="Veintisiete", pregunta=pregVeintisiete, 
            respuestaA="a. Depositar temporalmente los residuos, en un espacio físico definido y por un tiempo determinado.", respuestaB="b. Operación de eliminación de los residuos. Es el proceso de aislar y confinar los residuos, en lugares especialmente seleccionados, diseñados y debidamente autorizados, para evitar la contaminación y los daños o riesgos a la salud humana y al ambiente.", 
            respuestaC="c. Botar los residuos en la calle o en los ríos.",respuestaD=None,
            respuestaE=None, respuestaF=None)
    respVeintiocho = add_preResp(nombre="Veintiocho", pregunta=pregVeintiocho, 
            respuestaA="a. Devolver a los materiales su potencialidad de reincorporación como materia prima para la fabricación de nuevos productos.", respuestaB="b. Disponer los residuos en un relleno sanitario.", 
            respuestaC="c. Aprovechar y transformar los residuos recuperados.", respuestaD="d. a y c",
            respuestaE=None, respuestaF=None)
    respVeintinueve = add_preResp(nombre="Veintinueve", pregunta=pregVeintinueve, 
            respuestaA="a. Reutilización.", respuestaB="b. Reconversión industrial.", 
            respuestaC="c. Incineración", respuestaD="d. a y b", 
            respuestaE="e. Ninguna", respuestaF=None)
    respTreinta = add_preResp(nombre="Treinta", pregunta=pregTreinta, 
            respuestaA="Cualquier objeto, material, sustancia, producto cuyo generador descarta, rechaza o entrega porque sus propiedades no permiten usarlo nuevamente en la actividad que lo generó.", respuestaB="b. Cualquier objeto, material, sustancia, producto que se está utilizando para alguna actividad específica.",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respTreintaiuno = add_preResp(nombre="Treintaiuno", pregunta=pregTreintaiuno, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respTreintaidos = add_preResp(nombre="Treintaidos", pregunta=pregTreintaidos, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respTreintaitres = add_preResp(nombre="Treintaitres", pregunta=pregTreintaitres, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respTreintaicuatro = add_preResp(nombre="Treintaicuatro", pregunta=pregTreintaicuatro, 
            respuestaA="a. Aprovechar el material del que está hecho un producto determinado para convertirlo en otra cosa (botellas de cristal convertidas en vasos) o, de nuevo, en la misma (papel usado transformado en papel nuevo).", respuestaB="b. No ayuda a reducir el volumen de los desechos ni a reducir el coste de producción.", 
            respuestaC="c. Puede requerir un tratamiento o proceso que partirá del material inicial para obtenerse aquello que se pretendía.", respuestaD="d. a y c",
            respuestaE=None, respuestaF=None)
    respTreintaicinco = add_preResp(nombre="Treintaicinco", pregunta=pregTreintaicinco, 
            respuestaA="a. A la basura.", respuestaB="b. Contenedor verde.", 
            respuestaC="c. En la playa.", respuestaD="d. Contenedor azul o gris",
            respuestaE=None, respuestaF=None)
    respTreintaiseis = add_preResp(nombre="Treintaiseis", pregunta=pregTreintaiseis, 
            respuestaA="a. Residuos ordinarios.", respuestaB="b. Residuos peligrosos.", 
            respuestaC="c. Residuos reciclables.", respuestaD="d. Residuos biodegradables.",
            respuestaE=None, respuestaF=None)
    respTreintaisiete = add_preResp(nombre="Treintaisiete", pregunta=pregTreintaisiete, 
            respuestaA="a. Residuos ordinarios.", respuestaB="b. Residuos reciclables.", 
            respuestaC="c. Residuos peligrosos - biosanitarios.", respuestaD="d. Ninguno de los anteriores.",
            respuestaE=None, respuestaF=None)
    respTreintaiocho = add_preResp(nombre="Treintaiocho", pregunta=pregTreintaiocho, 
            respuestaA="a. Tóner y botellas.", respuestaB="b. Plástico y cajas.", 
            respuestaC="c. Pilas y bombillos.", respuestaD="d. Pilas y papel.",
            respuestaE=None, respuestaF=None)
    respTreintainueve = add_preResp(nombre="Treintainueve", pregunta=pregTreintainueve, 
            respuestaA="a. El relleno sanitario es una disposición final de los residuos que consiste en arrojarlos en la calle.", respuestaB="b. El relleno sanitario consiste en depositar en un sitio controlado en el que se esparcen los residuos y se compactan reduciéndolos al menor volumen posible para que así ocupen un área pequeña. Luego se cubren con una capa de tierra y se compactan nuevamente al terminar el día.", 
            respuestaC="c. Ninguna de las anteriores", respuestaD=None,
            respuestaE=None, respuestaF=None)
    respCuarenta = add_preResp(nombre="Cuarenta", pregunta=pregCuarenta, 
            respuestaA="a. Incineración y celda de seguridad.", respuestaB="b. Neutralización química.", 
            respuestaC="c. Disposición en el río o en la calle.", respuestaD="d. a y b",
            respuestaE=None, respuestaF=None)
    respCuarentaiuno = add_preResp(nombre="Cuarentaiuno", pregunta=pregCuarentaiuno, 
            respuestaA="Verdadero", respuestaB="False",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respCuarentaidos = add_preResp(nombre="Cuarentaidos", pregunta=pregCuarentaidos, 
            respuestaA="a. Biomasa (origen vegetal y animal).", respuestaB="b. Energía eólica.", 
            respuestaC="c. Energía hidroeléctrica.", respuestaD="d. Gas natural.",
            respuestaE=None, respuestaF=None)
    respCuarentaitres = add_preResp(nombre="Cuarentaitres", pregunta=pregCuarentaitres, 
            respuestaA="a. Aluminio.", respuestaB="b. Papel.", 
            respuestaC="c. Chicle.", respuestaD="d. Plástico.",
            respuestaE=None, respuestaF=None)
    respCuarentaicuatro = add_preResp(nombre="Cuarentaicuatro", pregunta=pregCuarentaicuatro, 
            respuestaA="a. De las plantas.", respuestaB="b. Del petróleo.", 
            respuestaC="c. Del papel.", respuestaD="d. De un animal.",
            respuestaE=None, respuestaF=None)
    respCuarentaicinco = add_preResp(nombre="Cuarentaicinco", pregunta=pregCuarentaicinco, 
            respuestaA="a. Reciclar, reutilizar, reducir", respuestaB="b. Reducir, reciclar, reutilizar", 
            respuestaC="c. Reducir, reutilizar, reciclar", respuestaD="d. Reutilizar, reciclar, reducir",
            respuestaE=None, respuestaF=None)
    respCuarentaiseis = add_preResp(nombre="Cuarentaiseis", pregunta=pregCuarentaiseis, 
            respuestaA="a. Del plástico.", respuestaB="b. De la arena.", 
            respuestaC="c. Del papel.", respuestaD="d. De un animal.",
            respuestaE=None, respuestaF=None)
    respCuarentaisiete = add_preResp(nombre="Cuarentaisiete", pregunta=pregCuarentaisiete, 
            respuestaA="a. Recursos no renovables.", respuestaB="b. Recursos irrenovables.", 
            respuestaC="c. Recursos renovables.", respuestaD="d. Ninguna de las anteriores.",
            respuestaE=None, respuestaF=None)
    respCuarentaiocho = add_preResp(nombre="Cuarentaiocho", pregunta=pregCuarentaiocho, 
            respuestaA="a. Recursos no renovables.", respuestaB="b. Recursos irrenovables.", 
            respuestaC="c. Recursos renovables.", respuestaD="d. Ninguna de las anteriores.",
            respuestaE=None, respuestaF=None)
    respCuarentainueve = add_preResp(nombre="Cuarentainueve", pregunta=pregCuarentainueve, 
            respuestaA="a. Recurso natural que no puede ser producido, regenerado o reutilizado a una escala tal que pueda sostener su tasa de consumo.", respuestaB="Recurso natural que se puede restaurar o regenerar por procesos naturales a una velocidad superior a la del consumo por los seres humanos.",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respCincuenta = add_preResp(nombre="Cincuenta", pregunta=pregCincuenta, 
            respuestaA="a. Petróleo.", respuestaB="b. Carbón.", 
            respuestaC="c. Gas natural.", respuestaD="d. Agua.",
            respuestaE=None, respuestaF=None)
    respCincuentaiuno = add_preResp(nombre="Cincuentaiuno", pregunta=pregCincuentaiuno, 
            respuestaA="a. Agua.", respuestaB="b. Viento.", 
            respuestaC="c. Petróleo.", respuestaD="d. Radiación solar.",
            respuestaE=None, respuestaF=None)
    respCincuentaidos = add_preResp(nombre="Cincuentaidos", pregunta=pregCincuentaidos, 
            respuestaA="a. Se debe solicitar al gestor el certificado de disposición final de los residuos entregados para verificar que éstos hayan sido dispuestos adecuadamente.", respuestaB="b. Se debe conservar registros de entrega y de disposición final por un periodo no menor a 5 años.", 
            respuestaC="c. No se debe solicitar al gestor el certificado de disposición final de los residuos entregados.", respuestaD="d. a y b", 
            respuestaE="e. Ninguna de las anteriores", respuestaF=None)
    respCincuentaitres = add_preResp(nombre="Cincuentaitres", pregunta=pregCincuentaitres, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respCincuentaicuatro = add_preResp(nombre="Cincuentaicuatro", pregunta=pregCincuentaicuatro, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    respCincuentaicinco = add_preResp(nombre="Cincuentaicinco", pregunta=pregCincuentaicinco, 
            respuestaA="Verdadero", respuestaB="Falso",
            respuestaC=None, respuestaD=None,
            respuestaE=None, respuestaF=None)
    print "####---- Canecas ----####"
    canUno = add_caneca(nombre="Roja", descripcion="Desechos clínicos, objetos punzocortantes", imagen="/media/images/roja.png")
    canDos = add_caneca(nombre="Gris/Azul", descripcion="Papel, cartón, vidrio, metal (aluminio)", imagen="/media/images/grisAzul.png")
    canTres = add_caneca(nombre="Verde", descripcion="Desechos de comida, envases con desechos de comida, servilletas", imagen="/media/images/verde.png")
    print "####---- Residuos ----####"
    resiUno = add_residuo(nombre="Aguja hipodérmica", imagen="/media/images/aguja.png", caneca=canUno)
    resiDos = add_residuo(nombre="Algodones", imagen="/media/images/algodon.png", caneca=canUno)
    resiTres = add_residuo(nombre="Papel aluminio con restos de comida", imagen="/media/images/alum.png", caneca=canTres)
    resiCuatro = add_residuo(nombre="Lata de atún limpia", imagen="/media/images/atunlimp.png", caneca=canDos)
    resiCinco = add_residuo(nombre="Bajalenguas", imagen="/media/images/bajaleng.png", caneca=canUno)
    resiSeis = add_residuo(nombre="Baldes Viejos", imagen="/media/images/balde.png", caneca=canDos)
    resiSiete = add_residuo(nombre="Bolsa de Papel", imagen="/media/images/bolsapapel.png", caneca=canDos)
    resiOcho = add_residuo(nombre="Bolsa Plástica", imagen="/media/images/bolsplast.png", caneca=canDos)
    resiNueve = add_residuo(nombre="Botella Plástica", imagen="/media/images/botagua.png", caneca=canDos)
    resiDiez = add_residuo(nombre="Botella Plástica de Coca Cola", imagen="/media/images/botagua.png", caneca=canDos)
    resiOnce = add_residuo(nombre="Botellas de vidrio", imagen="/media/images/botvidr.png", caneca=canDos)
    resiDoce = add_residuo(nombre="Cables", imagen="/media/images/cable.png", caneca=canDos)
    resiTrece = add_residuo(nombre="Caja de Cartón", imagen="/media/images/cajacart.png", caneca=canDos)
    resiCatorce = add_residuo(nombre="Caja de huevos", imagen="/media/images/cajahuev.png", caneca=canDos)
    resiQuince = add_residuo(nombre="Caja de pizza", imagen="/media/images/cajapizza.png", caneca=canDos)
    resiDieciseis = add_residuo(nombre="Carpetas viejas", imagen="/media/images/carpetas.png", caneca=canDos)
    resiDiecisiete = add_residuo(nombre="Cartones", imagen="/media/images/carton.png", caneca=canDos)
    resiDieciocho = add_residuo(nombre="Cáscara de banano", imagen="/media/images/cascban.png", caneca=canTres)
    resiDiecinueve = add_residuo(nombre="Cepillo de dientes", imagen="/media/images/cepdie.png", caneca=canUno)
    resiVeinte = add_residuo(nombre="Chicle", imagen="/media/images/chicle.png", caneca=canTres)
    resiVeintiuno = add_residuo(nombre="Cinta adhesiva", imagen="/media/images/cintadh.png", caneca=canTres)
    resiVeintidos = add_residuo(nombre="Cinta de enmascarar", imagen="/media/images/cintaenm.png", caneca=canTres)
    resiVeintitres = add_residuo(nombre="Cinta aislante", imagen="/media/images/cintaisla.png", caneca=canTres)
    resiVeinticuatro = add_residuo(nombre="Clips", imagen="/media/images/clips.png", caneca=canDos)
    resiVeinticinco = add_residuo(nombre="Contenedores de metal", imagen="/media/images/contmetal.png", caneca=canDos)
    resiVeintiseis = add_residuo(nombre="Corazón de manzana", imagen="/media/images/corazmanz.png", caneca=canTres)
    resiVeintisiete = add_residuo(nombre="Cuadernos", imagen="/media/images/cuadernos.png", caneca=canDos)
    resiVeintiocho = add_residuo(nombre="Cuchilla de afeitar", imagen="/media/images/cuchill.png", caneca=canUno)
    resiVeintinueve = add_residuo(nombre="Cuchara de palo", imagen="/media/images/cuchpalo.png", caneca=canDos)
    resiTreinta = add_residuo(nombre="Cura usada", imagen="/media/images/cura.png", caneca=canUno)
    resiTreintaiuno = add_residuo(nombre="Bolsa de drenaje", imagen="/media/images/drenaje.png", caneca=canUno)
    resiTreintaidos = add_residuo(nombre="Empaque desechable", imagen="/media/images/emp2des.png", caneca=canTres)
    resiTreintaitres = add_residuo(nombre="Empaque de comida", imagen="/media/images/empcom.png", caneca=canTres)
    resiTreintaicuatro = add_residuo(nombre="Envoltura de hamburguesa", imagen="/media/images/envhamb.png", caneca=canTres)
    resiTreintaicinco = add_residuo(nombre="Envase de vidrio", imagen="/media/images/envidrio.png", caneca=canDos)
    resiTreintaiseis = add_residuo(nombre="Espuma", imagen="/media/images/espuma.png", caneca=canTres)
    resiTreintaisiete = add_residuo(nombre="Factura de datáfono", imagen="/media/images/factdatf.png", caneca=canTres)
    resiTreintaiocho = add_residuo(nombre="Filtro de café", imagen="/media/images/filtcafe.png", caneca=canTres)
    resiTreintainueve = add_residuo(nombre="Gancho para folder", imagen="/media/images/gancho.png", caneca=canDos)
    resiCuarenta = add_residuo(nombre="Gasa usada", imagen="/media/images/gasa.png", caneca=canUno)
    resiCuarentaiuno = add_residuo(nombre="Grapas", imagen="/media/images/grapas.png", caneca=canDos)
    resiCuarentaidos = add_residuo(nombre="Guantes quirúrgicos", imagen="/media/images/guantes.png", caneca=canUno)
    resiCuarentaitres = add_residuo(nombre="Hisopos", imagen="/media/images/hisopo.png", caneca=canUno)
    resiCuarentaicuatro = add_residuo(nombre="Icopor", imagen="/media/images/icopor.png", caneca=canTres)
    resiCuarentaicinco = add_residuo(nombre="Jeringa", imagen="/media/images/jeringa.png", caneca=canUno)
    resiCuarentaiseis = add_residuo(nombre="Pañuelo de papel", imagen="/media/images/klee.png", caneca=canTres)
    resiCuarentaisiete = add_residuo(nombre="Lata de atún sucia", imagen="/media/images/latatunsuc.png", caneca=canTres)
    resiCuarentaiocho = add_residuo(nombre="Libros", imagen="/media/images/libros.png", caneca=canDos)
    resiCuarentainueve = add_residuo(nombre="Olla vieja", imagen="/media/images/olla.png", caneca=canDos)
    resiCincuenta = add_residuo(nombre="Papel carbón", imagen="/media/images/papc.png", caneca=canTres)
    resiCincuentaiuno = add_residuo(nombre="Papel Craft", imagen="/media/images/papcraft.png", caneca=canDos)
    resiCincuentaidos = add_residuo(nombre="Papel de un dulce", imagen="/media/images/papdulc.png", caneca=canDos)
    resiCincuentaitres = add_residuo(nombre="Papel", imagen="/media/images/papel.png", caneca=canDos)
    resiCincuentaicuatro = add_residuo(nombre="Papel Usado", imagen="/media/images/papelusado.png", caneca=canDos)
    resiCincuentaicinco = add_residuo(nombre="Papel higiénico", imagen="/media/images/paphig.png", caneca=canTres)
    resiCincuentaiseis = add_residuo(nombre="Periódicos", imagen="/media/images/periodic.png", caneca=canDos)
    resiCincuentaisiete = add_residuo(nombre="Pipetas", imagen="/media/images/pipeta.png", caneca=canUno)
    resiCincuentaiocho = add_residuo(nombre="Pitillos", imagen="/media/images/pitillo.png", caneca=canDos)
    resiCincuentainueve = add_residuo(nombre="Polvo al barrer", imagen="/media/images/polvo.png", caneca=canTres)
    resiSesenta = add_residuo(nombre="Revistas", imagen="/media/images/revistas.png", caneca=canDos)
    resiSesentaiuno = add_residuo(nombre="Tela con sangre", imagen="/media/images/sangre.png", caneca=canUno)
    resiSesentaidos = add_residuo(nombre="Servilletas de papel", imagen="/media/images/serv.png", caneca=canTres)
    resiSesentaitres = add_residuo(nombre="Sobres", imagen="/media/images/sobre.png", caneca=canDos)
    resiSesentaicuatro = add_residuo(nombre="Tapabocas usado", imagen="/media/images/tapabo.png", caneca=canUno)
    resiSesentaicinco = add_residuo(nombre="Tapa de Café", imagen="/media/images/tapacafe.png", caneca=canDos)
    resiSesentaiseis = add_residuo(nombre="Tapas", imagen="/media/images/tapas.png", caneca=canDos)
    resiSesentaisiete = add_residuo(nombre="Tela", imagen="/media/images/tela.png", caneca=canDos)
    resiSesentaiocho = add_residuo(nombre="Tetra Pak", imagen="/media/images/tetra.png", caneca=canDos)
    resiSesentainueve = add_residuo(nombre="Tubo usado", imagen="/media/images/tubo.png", caneca=canUno)
    resiSetenta = add_residuo(nombre="Venda Usada", imagen="/media/images/venda.png", caneca=canDos)
    resiSetentaiuno = add_residuo(nombre="Vaso de papel", imagen="/media/images/vasopapel.png", caneca=canDos)
    resiSetentaidos = add_residuo(nombre="Vaso plástico", imagen="/media/images/vasopla.png", caneca=canDos)
    resiTreintaidos = add_residuo(nombre="Empaque desechable negro", imagen="/media/images/empdes.png", caneca=canTres)
    print "####---- Termino la carga del Script Populate----####"

def add_equipo(nombre, numero):
    equ = Equipo.objects.get_or_create(nombre=nombre, numero=numero)[0]
    return equ

def add_usuario(username, password, first_name, last_name, equipo):
    usuario = User.objects.get_or_create(username=username, password=password, first_name=first_name, last_name=last_name)[0]
    UserProfile.objects.get_or_create(user=usuario,equipo=equipo)
    return usuario
    
def add_pregunta(enunciado, respuestaCorrecta):
    pre = Pregunta.objects.get_or_create(enunciado=enunciado, respuestaCorrecta=respuestaCorrecta)[0]
    return pre

def add_preResp(nombre, pregunta, respuestaA, respuestaB, respuestaC, respuestaD, respuestaE, respuestaF):
    preResp = PregRespuesta.objects.get_or_create(nombre=nombre, pregunta=pregunta, respuestaA=respuestaA, respuestaB=respuestaB, respuestaC=respuestaC, respuestaD=respuestaD, respuestaE=respuestaE, respuestaF=respuestaF)[0]
    return preResp

def add_caneca(nombre, descripcion, imagen):
    can = Caneca.objects.get_or_create(nombre=nombre, descripcion=descripcion, imagen=imagen)[0]
    return can

def add_residuo(nombre, imagen, caneca):
    resi = Residuo.objects.get_or_create(nombre=nombre, imagen=imagen, caneca=caneca)[0]
    return resi

# Start execution here!
if __name__ == '__main__':
    print "Comienza Carga del Populate !"
    populate()