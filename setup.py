import setuptools


setuptools.setup(
     name='mi_paquete',  #nombre del paquete
     version='0.1', #versión
     scripts=['my_ejecutable.py'] , #nombre del ejecutable
     author="Alberto Rubiales", #autor
     author_email="albertorubialest@gmail.com", #email
     description="Un paquete para traducir a números romanos", #Breve descripción
     long_description=long_description,
   long_description_content_type="text/markdown", #Incluir el README.md si lo has creado
     url="https://github.com/usuario/nombre_del_paquete", #url donde se encuentra tu paquete en Github
     packages=setuptools.find_packages(), #buscamos todas las dependecias necesarias para que tu paquete funcione (por ejemplo numpy, scipy, etc.)
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 ) #aquí añadimos información sobre el lenguaje usado, el tipo de licencia, etc.
