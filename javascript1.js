var words = [
	'Biology',
	'Paleontology',
	'Anthropology',
	'Pharmacology',
	'Microbiology']

function newWord() {
	var randomNumber = Math.floor(Math.random()*(words.length));
	document.getElementById('wordDisplay').innerHTML= words[randomNumber];

}
