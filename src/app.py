from pickle import load
import streamlit as st

model = load(open("../models/modelo_estefanico_4geeks.sav", "rb"))
