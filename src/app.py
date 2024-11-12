from pickle import load
import streamlit as st

model = load(open("/workspaces/4geeks_proyect_estefanico/models/modelo_estefanico_4geeks.sav", "rb"))

st.title('Cambio de domicilio')

region =  st.radio(
    "Región a la que pertenece", 
    ['Región de ñuble',
 'Region del biobio',
 'Region metropolitana',
 'Region de tarapaca',
 'Region de los rios',
 'Region del libertador gral bernardo ohiggins',
 'Region de la araucania',
 'Region de valparaiso',
 'Region de los lagos'
 'Region de coquimbo',
 'Region del maule',
 'Region de arica y parinacota',
 'Region de antofagasta',
 'Region de atacama',
 'Region de magallanes y de la antartica chilena',
 'Region de aysen del gral carlos ibañez del campo'],
    index=None)

nivel_socioeconomico = st.radio(
    "Nivel socioeconómico",
    ['Bajo-medio', 'Bajo-medio-alto', 'Medio', 'Bajo', 'Alto', 'Medio-alto', 'Bajo-alto'],
     index= None)

edad = st.slider('Edad', min_value=15, max_value=100, step=1)

nivel_educacional = st.radio(
    "Nivel educacional",
    ['Básica', 'Técnica nivel superior', 'Media científico humanista', 'Técnica comercial industrial normalista', 'Media técnica profesional', 'Profesional', 'Diferencial', 'Ninguno', 'Magister', 'Doctorado', 'Prekinder-kinder', 'Jardin infantil', 'Sala cuna'],
     index= None)

trabajo_semana_pasada = st.radio(
    "Trabajé la semana pasada",
    ['Si', 'No'],
    index= None)

nacionalidad = st.radio(
    "Nacionalidad",
    ['Chile', 'Extranjero', 'Binacionalidad'],
     index= None)

participacion_organizacion = st.radio(
    "Participo en una organización",
    ['Si', 'No'],
    index= None)


tipo_vivienda= st.radio(
    "Tipo de vivienda",
    ['Casa no pareada', 'Casa pareada', 'Departamento', 'Pieza', 'Mediagua', 'Vivienda precaria', 'Vivienda tradicional indigena', 'Rancho-choza'],
    index= None)


propiedad = st.radio(
    "Vivienda",
    ['Propia', 'Cedida', 'Arrendada', 'Usufructo', 'Ocupacion irregular'],
    index= None)
    
region_dic = {'Región de ñuble': 0,
 'Region del biobio' : 1,
 'Region metropolitana' : 2,
 'Region de tarapaca' : 3,
 'Region de los rios': 4,
 'Region del libertador gral bernardo ohiggins': 5,
 'Region de la araucania': 6,
 'Region de valparaiso': 7,
 'Region de los lagos': 8,
 'Region de coquimbo':9,
 'Region del maule':10,
 'Region de arica y parinacota': 11,
 'Region de antofagasta': 12,
 'Region de atacama':13,
 'Region de magallanes y de la antartica chilena': 14,
 'Region de aysen del gral carlos ibañez del campo': 15}
nivel_socioeconomico_dic = {
'Bajo-medio': 0,
 'Bajo-medio-alto': 1,
 'Medio': 2,
 'Bajo': 3,
 'Alto': 4,
 'Medio-alto': 4,
 'Bajo-alto': 6}
nivel_educacional_dic= {'Básica': 0,
'Técnica nivel superior': 1,
'Media científico humanista': 2,
'Técnica comercial industrial normalista': 3,
'Media técnica profesional': 4,
'Profesional': 5,
'Diferencial': 6,
'Ninguno': 7,
'Magister': 8,
'Doctorado': 9,
'Prekinder-kinder':10,
'Jardin infantil': 11,
'Sala cuna': 12}
trabajo_semana_pasada_dic = {'No' : 0,
                             'Si': 1}
nacionalidad_dic = {'Chile': 0, 'Extranjero': 1, 'Binacionalidad':2}
participacion_organizacion_dic = {'No' : 0,
                             'Si': 1}
tipo_vivienda_dic = {'Casa no pareada': 0,
 'Casa pareada': 1,
 'Departamento': 2,
 'Pieza': 3,
 'Mediagua': 4,
 'Vivienda precaria': 5,
 'Vivienda tradicional indigena': 6,
 'Rancho-choza': 7}
propiedad_dic = {'Propia': 0,
'Cedida': 1,
'Arrendada': 2,
'Usufructo': 3,
'Ocupacion irregular': 4}


if st.button('Predecir'):
    prediccion = model.predict([[region_dic[region], nivel_socioeconomico_dic[nivel_socioeconomico], edad, nivel_educacional_dic[nivel_educacional], trabajo_semana_pasada_dic[trabajo_semana_pasada_dic], nacionalidad_dic[nacionalidad_dic], participacion_organizacion_dic[participacion_organizacion], tipo_vivienda_dic[tipo_vivienda], propiedad_dic[propiedad_dic]]])
    st.write('Cambio de hogar', prediccion)


