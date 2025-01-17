"use strict"

// Задача №1
// Отримати в константу елемент <body>
// const bodyElement = document.body
// console.log(bodyElement)

// Задача №2
// Написати функцію, яка додає в <body> список UL
// з певною кількістю LI (кількість має передаватись як параметр функції, також мати значення за замовченням)
let addList = (volumeLi = 3) => {
	if (typeof volumeLi === "number") {
		const bodyElement = document.body
		let ulTemplate = `<ul>`
		for (let index = 0; index < volumeLi; index++) {
			ulTemplate += `<li></li>`
		}
		ulTemplate += `</ul>`
		bodyElement.insertAdjacentHTML("afterbegin", ulTemplate)
	} else {
		console.log("Volume of tag li is not a number! Enter number, please!")
	}
}
// addList(7)

// Задача №3
// Додати до елементу <body> класс loaded.
// Потім перевірити чи є клас loaded у елемента <body>
// і, якщо є, додати стиль кольору тесту зедлений.
const bodyElement = document.body
bodyElement.classList.add('loaded')
if (bodyElement.classList.contains('loaded')) {
	bodyElement.style.color = 'green'
}

// Задача №4
// Дано в html: три елементи з класом item.
// Треба отримати ці елементи в константу, кожному додати клас active, 
// та перезаписати контент всередені кожного елемента на "Елемент №(тут порядковий номер елементу починаючи з 1)".
const items = document.querySelectorAll(`.item`)
if (items.length) {
	items.forEach((element, index) => {
		element.classList.add('active')
		element.textContent = `Element #${index + 1}`
	})
}

// Задача №5
// Дано в html: текст, далі кнопка з класом button.
// Треба прокрутити скрол сторінки до кнопки
const buttonElement = document.querySelector('.button')
if (buttonElement) {
	buttonElement.scrollIntoView({
		block: "start",
		inline: "nearest",
		behavior: "smooth"
	})
}

// Задача №6
// Дано в html: посилання з класом link
// Треба додати до посилання дата атрибут зі значенням 100
// Поім отримати значення трибуту, та, якщо значення меньше 200
// пофарбувати колір тексту посилання в червоний
const link = document.querySelector('.link')
if (link) {
	link.setAttribute('data-speed', '100')
	if (parseFloat(link.dataset.speed) < 200) {
		link.style.color = 'red'
	}
}
