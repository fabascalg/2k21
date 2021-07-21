var nombre = "Víctor Robles";
var altura = 169;

/*var concatenacion = nombre + " " + altura;

var datos = document.getElementById("datos");

var mensaje = "<h1>Soy una caja de datos</h1>" 
mensaje += "<h2>Mi nombre es: " + nombre + "</h2>"
mensaje += "<h2>Mido: " + altura + "</h2>"


datos.innerHTML = mensaje




if (altura >= 175)
	datos.innerHTML += `<h2>¡eres una persona alta!</h2>`;
else
	datos.innerHTML += `<h2>¡eres una persona bajita!</h2>`;

for (var i = 0; i <= 10; i++)
	datos.innerHTML += `contador: ${i}<br />`;

*/

function MuestraMiNombre(nombre, altura) {
	var datos = `
		<h1>Soy una caja de texto</h1>
		<h2>Mi nombre es: ${nombre}</h2>
		<h2>Mido: ${altura}</h2>
	`;
	return datos;
}

function imprimir() {
	var datos = document.getElementById("datos");
	datos.innerHTML = MuestraMiNombre("Víctor Robles WEB", 169);
}

imprimir();

var nombres = ['Víctor', 'Antonio', 'Joaquín'];
/*
document.write("<strong>Listado de nombres:</strong><br /><ul>")
for (var n = 0; n<=2; n++){
	//alert(nombres[n]);
	document.write("<li>" + nombres[n] + "</blockqoute></li>");
}
document.write("</ul>")

nombres.forEach(element => {
	document.write("<strong style='color:red'>" +element + "</strong><br />");
});
*/
nombres.forEach(function(element) {
	document.write("<strong style='color:green;'>" +element + "</strong><br />");
});
