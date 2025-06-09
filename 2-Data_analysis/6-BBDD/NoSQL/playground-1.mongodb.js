use('taller_mongo')

// modifica la colleccion
db.employees.aggregate([
    { $addFields: { bonus: { $multiply: ["$salary", 0.1] } } }
]);


// // db.clientes.find()
// db.employees.aggregate([
//     { $group: { _id: "$department.name",
//                 totalSalaries: { $sum: "$salary" } } }
// ]);

// db.employees.insertMany([
//     { 
//         _id:1,
//         firstName: "Muchelle",
//         lastName: "Wallys",
//         gender:'female',
//         email: "muchelle@thebridgeschool.es",
//         salary: 5000,
//         department: { 
//                     "name":"HR" 
//                 }
//     },
//     { 
//         _id:2,
//         firstName: "Marta",
//         lastName: "Perez",
//         gender:'female',
//         email: "marta@demo.com",
//         salary: 8000,
//         department: { 
//                     "name":"Finance" 
//                 }
//     },
//     { 
//         _id:3,
//         firstName: "Birja",
//         lastName: "Rybera",
//         gender:'male',
//         email: "birja@thebridgeschool.es",
//         salary: 7500,
//         department: { 
//                     "name":"Marketing" 
//                 }
//     },
//     { 
//         _id:4,
//         firstName: "Rosa",
//         lastName: "Sanchez",
//         gender:'female',
//         email: "rosa@demo.com",
//         salary: 5000, 
//         department: { 
//                     "name":"HR" 
//                 }

//     },
//     { 
//         _id:5,
//         firstName: "Alvaru",
//         lastName: "Aryas",
//         gender:'male',
//         email: "alvaru@thebridgeschool.es",
//         salary: 4500,
//         department: { 
//                     "name":"Finance" 
//                 }

//     },
//     { 
//         _id:6,
//         firstName: "Anita",
//         lastName: "Rodrigues",
//         gender:'female',
//         email: "anita@demo.com",
//         salary: 7000,
//         department: { 
//                     "name":"Marketing" 
//                 }
//     },
//         { 
//         _id:7,
//         firstName: "Alejandru",
//         lastName: "Regex",
//         gender:'male',
//         email: "alejandru@thebridgeschool.es",
//         salary: 7000,
//         department: { 
//                     "name":"Marketing" 
//                 }
//     }
// ])


// lookup


// // unwind: manteniene el mismo id pero es identico pero con el array de direcciones
// // spliteado; sum:1 valor init

// db.clientes.aggregate([
//   { $match: {} }, // (1) Opcional: filtra documentos (aquí no filtramos nada)
//   { $unwind: '$direcciones'},
//   { $group: { _id: "$direcciones.ciudad", totalClientes: { $sum: 1 } } }, // (2) Agrupar por ciudad
//   { $sort: { totalClientes: -1 } } // (3) Ordenar de mayor a menor
// ])


// // agg - nueva collecion, id no puede ser un array, datos duplicados (ciudades)
// // group hace recorrido por cada elemento del array (direcciones) 

// db.clientes.aggregate([
//   { $match: {} }, // (1) Opcional: filtra documentos (aquí no filtramos nada)
//   { $group: { _id: "$direcciones.ciudad", totalClientes: { $sum: 1 } } }, // (2) Agrupar por ciudad
//   { $sort: { totalClientes: -1 } } // (3) Ordenar de mayor a menor
// ])

// // update One
// db.clientes.updateOne(
//   { _id: ObjectId('684009217b005774b4d861e0') },
//   { $set: { email: "laura.laura@example.com" } }
// )

// // sort 1 asc y -1 desc

// db.clientes.find(
//     {},{nombre: 1, _id: 0}).sort({nombre: 1})

// ligando AND, OR y condiciones ne

// db.clientes.find(
//     {   'direcciones.ciudad': 'Barcelona',
//         $or: [
//             {telefono:  []}, 
//             {comprass: {$ne:[]}}
//         ]
//     },{}
// )

// // leer array {$ne: []}

// db.clientes.find(
//     {telefono:  [], comprass: {$ne:[]}},{}
// )

// //  donde esxiste la propriedad X

// db.clientes.find({compras:{$exists:true}})

// // proyecciones, trae todo salvo

// db.clientes.find(
//     {},
//     {nombre:0, _id: 0, compras:0}

// )
// // proyecciones, trae todo salvo

// db.clientes.find(
//     {"compras.precio": {$lte:25}},
//     {nombre:0, _id: 0, compras:0}

// )
// // proyecciones, el id siempre viene salvo si no lo especificamos

// db.clientes.find(
//     {"compras.precio": {$lte:25}},
//     {nombre:1, _id: 0, compras:1}

// )

// // comparadores gt, gte, lt, lte

// db.clientes.find(
//     {"compras.precio": {$lte:25}}
// )


// // acceder a la propriedad direcciones y a la prop ciudad del primero que encuentra en el array de direcciones

// db.clientes.find(
//     { "direcciones.0.ciudad": "Barcelona" }
// )

// // acceder a la propriedad direcciones y a la prop ciudad

// db.clientes.find(
//     { "direcciones.ciudad": "Barcelona" }
// )

// db.clientes.find(
//     {nombre:/laura/i}
// ).limit(1)

// concatenando metodos
// db.clientes.find(
//     {nombre:/laura/i}
// ).count()

// bandera i que sea sensitive
// db.clientes.find(
//     {nombre:/laura/i}
// )

// db.clientes.find(
//     {nombre:'Laura Pérez'}
// )

// db.clientes.findOne()
// db.clientes.insertMany([
//     {
//       nombre: "Laura Gómez",
//       email: "laura.gomez@example.com",
//       telefono: ["+34 600123456", "+34 699987654"],
//       direcciones: [
//         {
//           tipo: "casa",
//           calle: "Calle Mayor 123",
//           ciudad: "Madrid",
//           pais: "España"
//         },
//         {
//           tipo: "trabajo",
//           calle: "Av. de América 45",
//           ciudad: "Madrid",
//           pais: "España"
//         }
//       ],
//       compras: [
//         { producto: "Laptop", precio: 1200, fecha: "2024-03-15" },
//         { producto: "Ratón", precio: 25, fecha: "2024-04-22" }
//       ]
//     },
//     {
//       nombre: "Carlos Ruiz",
//       email: "carlos.ruiz@example.com",
//       telefono: ["+34 611234567"],
//       direcciones: [
//         {
//           tipo: "casa",
//           calle: "Calle de Alcalá 58",
//           ciudad: "Madrid",
//           pais: "España"
//         }
//       ],
//       compras: []
//     },
//     {
//       nombre: "María López",
//       email: "maria.lopez@example.com",
//       telefono: ["+34 612345678"],
//       direcciones: [
//         {
//           tipo: "casa",
//           calle: "Calle Princesa 10",
//           ciudad: "Barcelona",
//           pais: "España"
//         }
//       ],
//       compras: [
//         { producto: "Tablet", precio: 350, fecha: "2023-11-10" }
//       ]
//     },
//     {
//     nombre: "José Martínez",
//       email: "jose.martinez@example.com",
//       telefono: ["+34 613456789"],
//       direcciones: [],
//       compras: [
//         { producto: "Monitor", precio: 200, fecha: "2024-05-01" },
//         { producto: "Teclado", precio: 50, fecha: "2024-05-02" }
//       ]
//     },
//     {
//       nombre: "Ana Torres",
//       email: "ana.torres@example.com",
//       telefono: [],
//       direcciones: [
//         {
//           tipo: "casa",
//           calle: "Rambla Catalunya 33",
//           ciudad: "Barcelona",
//           pais: "España"
//         }
//       ],
//       compras: []
//     },
//     {
//       nombre: "David Fernández",
//       email: "david.fernandez@example.com",
//       telefono: ["+34 614567890"],
//       direcciones: [
//         {
//           tipo: "trabajo",
//           calle: "Paseo de Gracia 22",
//           ciudad: "Barcelona",
//           pais: "España"
//         }
//       ],
//       compras: [
//         { producto: "Auriculares", precio: 80, fecha: "2024-02-14" }
//       ]
//     },
//     {
//     nombre: "Lucía Navarro",
//       email: "lucia.navarro@example.com",
//       telefono: ["+34 615678901"],
//       direcciones: [],
//       compras: [
//         { producto: "Smartphone", precio: 900, fecha: "2023-12-20" },
//         { producto: "Cargador", precio: 30, fecha: "2024-01-05" }
//       ]
//     },
//     {
//       nombre: "Miguel Álvarez",
//       email: "miguel.alvarez@example.com",
//       telefono: [],
//       direcciones: [],
//       compras: []
//     },
//     {
//       nombre: "Isabel Romero",
//       email: "isabel.romero@example.com",
//       telefono: ["+34 616789012"],
//       direcciones: [
//         {
//           tipo: "casa",
//           calle: "Gran Vía 80",
//           ciudad: "Valencia",
//           pais: "España"
//         }
//       ],
//       compras: [
//         { producto: "Impresora", precio: 150, fecha: "2024-06-01" }
//       ]
//     },
//     {

//       nombre: "Raúl Díaz",
//       email: "raul.diaz@example.com",
//       telefono: ["+34 617890123"],
//       direcciones: [
//         {
//           tipo: "trabajo",
//           calle: "Av. Constitución 100",
//           ciudad: "Sevilla",
//           pais: "España"
//         }
//       ],
//       compras: []
//     }
//   ])
