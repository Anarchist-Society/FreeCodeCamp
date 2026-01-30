console.log("Hello! I'm your coding fun fact guide!");

let botName = "Winbug";
let botLocation = "Roblox";
let favoriteLanguage = "C";

console.log(`My name is ${botName} and I live on ${botLocation}.`);
console.log(`My favorite programming language is ${favoriteLanguage}.`);

let codingFact = "Un dato curioso de " + favoriteLanguage + ": fue creado en los años 70 y todavía hoy es la base de muchos sistemas operativos como Unix y partes de Linux.";
console.log(codingFact);

codingFact = "Otro dato curioso de ".concat(favoriteLanguage, " es que fue creado por Dennis Ritchie");
console.log(codingFact);

codingFact = "Otro dato curioso de ".concat(favoriteLanguage, " es que el carácter nulo '\\0' es exactamente el número 0");
console.log(codingFact);

console.log(`It was fun sharing these facts with you. Goodbye! - ${botName} from ${botLocation}.`);
