from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('home.html')

@app.route('/ejercicio1',methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        resultado=''
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio =(nota1+nota2+nota3)/3

        if asistencia >= 80 and promedio >= 40:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"
        return render_template('ejercicio1.html', promedio=promedio, estado=estado,resultado='resultado')

    return render_template('ejercicio1.html')

@app.route('/ejercicio2',methods=['GET', 'POST'])
def ejercicio2():
    if request.method =='POST':
        nombre1 = len(str(request.form['nombre1']))
        nombre2 = len(str(request.form['nombre2']))
        nombre3 = len(str(request.form['nombre3']))

        if nombre1 >= nombre2 and nombre1 >= nombre3:
            return render_template('ejercicio2.html', nombre=str(request.form['nombre1']), caracteres= nombre1,resultado='resultado')
        elif nombre2 >= nombre1 and nombre2 >= nombre3:
            return render_template('ejercicio2.html', nombre=str(request.form['nombre2']),caracteres= nombre2, resultado='resultado')
        elif nombre3 >= nombre1 and nombre2 >= nombre2:
            return render_template('ejercicio2.html', nombre=str(request.form['nombre3']),caracteres= nombre3, resultado='resultado')
        else:
            return render_template('ejercicio2.html', nombre="", resultado='resultado')





    return render_template('ejercicio2.html')



if __name__ == '__main__':
    app.run(debug=True)