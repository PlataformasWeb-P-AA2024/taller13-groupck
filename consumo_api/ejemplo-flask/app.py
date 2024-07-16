from flask import Flask, flash, jsonify, redirect, render_template, request, url_for
import requests
import json
import config
app = Flask(__name__)

# Configuración
API_BASE_URL = 'http://localhost:8000/api/'
USUARIO = config.usuario
CLAVE = config.clave

@app.route('/')
def index():
    r = requests.get(f"{API_BASE_URL}edificios/", auth=(USUARIO, CLAVE))
    if r.status_code == 200:
        edificios = json.loads(r.content)
        return render_template('index.html', edificios=edificios)
    else:
        flash("No se pudieron obtener los edificios")
        return render_template('index.html', edificios=[])

@app.route('/crear_edificio', methods=['GET', 'POST'])
def crear_edificio():
    if request.method == 'POST':
        datos_edificio = {
            "nombre": request.form['nombre'],
            "direccion": request.form['direccion'],
            "ciudad": request.form['ciudad'],
            "tipo": request.form['tipo']
        }
        r = requests.post(f"{API_BASE_URL}edificios/",
                          auth=(USUARIO, CLAVE),
                          json=datos_edificio)
        if r.status_code == 201:
            flash("Edificio creado con éxito")
            return redirect(url_for('index'))
        else:
            flash("No se pudo crear el edificio")
    return render_template('crear_edificio.html')

@app.route('/editar_edificio/<int:edificio_id>', methods=['GET', 'POST'])
def editar_edificio(edificio_id):
    if request.method == 'POST':
        datos_edificio = {
            "nombre": request.form['nombre'],
            "direccion": request.form['direccion'],
            "ciudad": request.form['ciudad'],
            "tipo": request.form['tipo']
        }
        r = requests.put(f"{API_BASE_URL}edificios/{edificio_id}/",
                         auth=(USUARIO, CLAVE),
                         json=datos_edificio)
        if r.status_code == 200:
            flash("Edificio actualizado con éxito")
            return redirect(url_for('index'))
        else:
            flash("No se pudo actualizar el edificio")
    
    r = requests.get(f"{API_BASE_URL}edificios/{edificio_id}/", auth=(USUARIO, CLAVE))
    if r.status_code == 200:
        edificio = json.loads(r.content)
        return render_template('editar_edificio.html', edificio=edificio)
    else:
        flash("No se pudo obtener el edificio")
        return redirect(url_for('index'))

@app.route('/eliminar_edificio/<int:edificio_id>')
def eliminar_edificio(edificio_id):
    r = requests.delete(f"{API_BASE_URL}edificios/{edificio_id}/", auth=(USUARIO, CLAVE))
    if r.status_code == 204:
        flash("Edificio eliminado con éxito")
    else:
        flash("No se pudo eliminar el edificio")
    return redirect(url_for('index'))

@app.route('/crear_departamento', methods=['GET', 'POST'])
def crear_departamento():
    if request.method == 'POST':
        datos_departamento = {
            "nombre_propietario": request.form['nombre_propietario'],
            "costo": float(request.form['costo']),
            "numero_cuartos": int(request.form['numero_cuartos']),
            "edificio": int(request.form['edificio'])
        }
        r = requests.post(f"{API_BASE_URL}departamentos/",
                          auth=(USUARIO, CLAVE),
                          json=datos_departamento)
        if r.status_code == 201:
            flash("Departamento creado con éxito")
            return redirect(url_for('index'))
        else:
            flash("No se pudo crear el departamento")
    
    r = requests.get(f"{API_BASE_URL}edificios/", auth=(USUARIO, CLAVE))
    edificios = json.loads(r.content) if r.status_code == 200 else []
    return render_template('crear_departamento.html', edificios=edificios)

@app.route('/editar_departamento/<int:departamento_id>', methods=['GET', 'POST'])
def editar_departamento(departamento_id):
    if request.method == 'POST':
        datos_departamento = {
            "nombre_propietario": request.form['nombre_propietario'],
            "costo": float(request.form['costo']),
            "numero_cuartos": int(request.form['numero_cuartos']),
            "edificio": int(request.form['edificio'])
        }
        r = requests.put(f"{API_BASE_URL}departamentos/{departamento_id}/",
                         auth=(USUARIO, CLAVE),
                         json=datos_departamento)
        if r.status_code == 200:
            flash("Departamento actualizado con éxito")
            return redirect(url_for('index'))
        else:
            flash("No se pudo actualizar el departamento")
    
    r = requests.get(f"{API_BASE_URL}departamentos/{departamento_id}/", auth=(USUARIO, CLAVE))
    r_edificios = requests.get(f"{API_BASE_URL}edificios/", auth=(USUARIO, CLAVE))
    if r.status_code == 200 and r_edificios.status_code == 200:
        departamento = json.loads(r.content)
        edificios = json.loads(r_edificios.content)
        return render_template('editar_departamento.html', departamento=departamento, edificios=edificios)
    else:
        flash("No se pudieron obtener los datos")
        return redirect(url_for('index'))

@app.route('/eliminar_departamento/<int:departamento_id>')
def eliminar_departamento(departamento_id):
    r = requests.delete(f"{API_BASE_URL}departamentos/{departamento_id}/", auth=(USUARIO, CLAVE))
    if r.status_code == 204:
        flash("Departamento eliminado con éxito")
    else:
        flash("No se pudo eliminar el departamento")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=5000)