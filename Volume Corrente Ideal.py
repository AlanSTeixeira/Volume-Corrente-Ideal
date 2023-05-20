#!/usr/bin/env python
# coding: utf-8

# In[6]:


# Recebendo as informações do usuário
peso = float(input("Digite o peso do paciente em kg: "))
altura = float(input("Digite a altura do paciente em metros: "))
ml_kg = float(input("Digite quantos ml/kg de ar deseja oferecer ao paciente: "))

# Cálculo do IMC e do peso ideal
imc = peso / altura ** 2
peso_ideal = 24.9 * altura ** 2

# Cálculo do volume corrente ideal
volume_corrente = peso_ideal * ml_kg

# Imprimindo os resultados com duas casas decimais
print(30*"=")
print("O IMC do paciente é de {:.2f}".format(imc))
print(30*"=")
print("O peso ideal do paciente é de {:.2f} kg".format(peso_ideal))
print(30*"=")
print("O volume corrente ideal para o paciente é de {:.2f} ml por ciclo respiratório.".format(volume_corrente))
print(30*"=")

